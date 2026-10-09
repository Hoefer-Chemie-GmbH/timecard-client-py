"""Google ID tokens for a service account, as the facade expects them (audience = public URL of the facade)."""

from __future__ import annotations

import json
import time
from pathlib import Path

import google.auth.transport.requests
from google.oauth2 import service_account

from .client import AuthenticatedClient

RENEW_BEFORE_SECONDS = 60


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
    """AuthenticatedClient whose bearer token is renewed from a GoogleIdTokenSource before it expires."""

    def __init__(self, base_url: str, token_source: GoogleIdTokenSource, acting_user: str | None = None, **kwargs) -> None:
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
    """Convenience: client for ``base_url`` authenticated with the service account ``key`` (dict, path or JSON string)."""
    return RefreshingClient(base_url=base_url, token_source=GoogleIdTokenSource(key, audience=base_url), acting_user=acting_user, **kwargs)
