from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.open_timecard_session_response_201_session import OpenTimecardSessionResponse201Session


T = TypeVar("T", bound="OpenTimecardSessionResponse201")


@_attrs_define
class OpenTimecardSessionResponse201:
    """
    Attributes:
        session_id (str): send as header X-Timecard-Session
        session (OpenTimecardSessionResponse201Session):
    """

    session_id: str
    session: OpenTimecardSessionResponse201Session

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        session = self.session.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sessionId": session_id,
                "session": session,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_timecard_session_response_201_session import (
            OpenTimecardSessionResponse201Session,  # noqa: PLC0415
        )

        d = dict(src_dict)
        session_id = d.pop("sessionId")

        session = OpenTimecardSessionResponse201Session.from_dict(d.pop("session"))

        open_timecard_session_response_201 = cls(
            session_id=session_id,
            session=session,
        )

        return open_timecard_session_response_201
