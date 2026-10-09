"""Google ID tokens for a service account, as the facade expects them (audience = public URL of the facade)."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Protocol

import google.auth.transport.requests
from google.oauth2 import service_account

from .client import AuthenticatedClient

RENEW_BEFORE_SECONDS = 60


class TokenSource(Protocol):
    """Any source of bearer tokens: a GoogleIdTokenSource, the metadata server, or a fixed token for tests."""

    def token(self) -> str: ...


class GoogleIdTokenSource:
    """Mints and caches ID tokens; call ``token()`` before each request or use ``authenticated_client``."""

    def __init__(self, key: dict | str | Path, audience: str) -> None:
        info = key if isinstance(key, dict) else json.loads(Path(key).read_text(encoding="utf-8"))
        self._credentials = service_account.IDTokenCredentials.from_service_account_info(info, target_audience=audience)
        self._request = google.auth.transport.requests.Request()

    def token(self) -> str:
        expiry = self._credentials.expiry
        if not self._credentials.token or expiry is None or (expiry.timestamp() - time.time()) < RENEW_BEFORE_SECONDS:
            self._credentials.refresh(self._request)
        return self._credentials.token  # type: ignore[return-value]


class RefreshingClient(AuthenticatedClient):
    """AuthenticatedClient that asks its token source for the bearer token before every request."""

    def __init__(self, base_url: str, token_source: TokenSource, acting_user: str | None = None, **kwargs) -> None:
        headers = dict(kwargs.pop("headers", {}))
        if acting_user:
            headers["X-Acting-User"] = acting_user
        super().__init__(base_url=base_url, token=token_source.token(), headers=headers, **kwargs)
        self._token_source = token_source

    def get_httpx_client(self):  # noqa: D102 – refreshes the token lazily
        self.token = self._token_source.token()
        self._headers["Authorization"] = f"{self.prefix} {self.token}"
        return super().get_httpx_client()

    def get_async_httpx_client(self):  # noqa: D102
        self.token = self._token_source.token()
        self._headers["Authorization"] = f"{self.prefix} {self.token}"
        return super().get_async_httpx_client()


def authenticated_client(base_url: str, key: dict | str | Path, acting_user: str | None = None, **kwargs) -> RefreshingClient:
    """Convenience: client for ``base_url`` authenticated with the service account ``key`` (dict, path or JSON string).

    Raises ``timecard_client.errors.UnexpectedStatus`` for every error status unless ``raise_on_unexpected_status=False`` is passed;
    the generated ``sync`` functions would otherwise return ``None``, because the specification lists success statuses only.
    """
    kwargs.setdefault("raise_on_unexpected_status", True)
    return RefreshingClient(base_url=base_url, token_source=GoogleIdTokenSource(key, audience=base_url), acting_user=acting_user, **kwargs)
