"""Photo upload (``PUT /v1/persons/{personId}/photo``). The generator skips this endpoint because the body is raw ``image/jpeg``."""

from __future__ import annotations

from .client import AuthenticatedClient
from .errors import UnexpectedStatus


def put_person_photo(client: AuthenticatedClient, person_id: int, jpeg: bytes) -> None:
    """Stores or replaces the photo of a person; ``jpeg`` must be JPEG data (at most 2 MB)."""
    response = client.get_httpx_client().request(
        "PUT", f"/v1/persons/{person_id}/photo", content=jpeg, headers={"Content-Type": "image/jpeg"}
    )
    if response.status_code != 204:
        raise UnexpectedStatus(response.status_code, response.content)
