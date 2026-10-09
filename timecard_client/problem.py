"""RFC 9457 Problem Details as the facade returns them for every error."""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from .errors import UnexpectedStatus


@dataclass
class ProblemDetails:
    type: str
    title: str
    status: int
    instance: str
    detail: str | None = None
    errors: list[dict] = field(default_factory=list)
    extra: dict = field(default_factory=dict)

    @property
    def request_id(self) -> str:
        return self.instance.removeprefix("urn:request:")


def parse_problem(err: UnexpectedStatus) -> ProblemDetails | None:
    """Reads the Problem Details body out of an ``UnexpectedStatus`` raised by a generated ``*.sync`` call."""
    try:
        body = json.loads(err.content)
    except ValueError:
        return None
    if not isinstance(body, dict) or "status" not in body or "title" not in body:
        return None
    known = {"type", "title", "status", "instance", "detail", "errors"}
    return ProblemDetails(
        type=body.get("type", "about:blank"),
        title=body["title"],
        status=int(body["status"]),
        instance=body.get("instance", ""),
        detail=body.get("detail"),
        errors=list(body.get("errors") or []),
        extra={k: v for k, v in body.items() if k not in known},
    )
