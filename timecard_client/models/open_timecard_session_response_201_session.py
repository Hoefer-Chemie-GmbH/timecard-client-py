from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="OpenTimecardSessionResponse201Session")


@_attrs_define
class OpenTimecardSessionResponse201Session:
    """
    Attributes:
        user_name (str):
        person_id (int):
        person_name (str):
        created_at (str):
        expires_at (str): the session ends at the latest at this time, earlier when idle or ended by timeCard
    """

    user_name: str
    person_id: int
    person_name: str
    created_at: str
    expires_at: str

    def to_dict(self) -> dict[str, Any]:
        user_name = self.user_name

        person_id = self.person_id

        person_name = self.person_name

        created_at = self.created_at

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userName": user_name,
                "personId": person_id,
                "personName": person_name,
                "createdAt": created_at,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_name = d.pop("userName")

        person_id = d.pop("personId")

        person_name = d.pop("personName")

        created_at = d.pop("createdAt")

        expires_at = d.pop("expiresAt")

        open_timecard_session_response_201_session = cls(
            user_name=user_name,
            person_id=person_id,
            person_name=person_name,
            created_at=created_at,
            expires_at=expires_at,
        )

        return open_timecard_session_response_201_session
