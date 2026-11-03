from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_me_response_200_timecard_sessions import GetMeResponse200TimecardSessions

if TYPE_CHECKING:
    from ..models.get_me_response_200_timecard_session_type_0 import GetMeResponse200TimecardSessionType0
    from ..models.get_me_response_200_timecard_user_type_0 import GetMeResponse200TimecardUserType0


T = TypeVar("T", bound="GetMeResponse200")


@_attrs_define
class GetMeResponse200:
    """
    Attributes:
        issuer_name (str):
        issuer (str):
        subject (str):
        display_name (str):
        scopes (list[str]):
        departments (list[str] | None): departments whose persons the account sees; null = all persons
        timecard_user (GetMeResponse200TimecardUserType0 | None): timeCard login whose user rights apply to this
            account; null = the technical user of the facade
        timecard_sessions (GetMeResponse200TimecardSessions): whether the account may or must use pass-through timeCard
            sessions
        timecard_session (GetMeResponse200TimecardSessionType0 | None): pass-through session of this request (header
            X-Timecard-Session); its user rights apply
        token_expires_at (str):
    """

    issuer_name: str
    issuer: str
    subject: str
    display_name: str
    scopes: list[str]
    departments: list[str] | None
    timecard_user: GetMeResponse200TimecardUserType0 | None
    timecard_sessions: GetMeResponse200TimecardSessions
    timecard_session: GetMeResponse200TimecardSessionType0 | None
    token_expires_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_me_response_200_timecard_session_type_0 import (
            GetMeResponse200TimecardSessionType0,  # noqa: PLC0415
        )
        from ..models.get_me_response_200_timecard_user_type_0 import GetMeResponse200TimecardUserType0  # noqa: PLC0415

        issuer_name = self.issuer_name

        issuer = self.issuer

        subject = self.subject

        display_name = self.display_name

        scopes = self.scopes

        departments: list[str] | None
        if isinstance(self.departments, list):
            departments = self.departments

        else:
            departments = self.departments

        timecard_user: dict[str, Any] | None
        if isinstance(self.timecard_user, GetMeResponse200TimecardUserType0):
            timecard_user = self.timecard_user.to_dict()
        else:
            timecard_user = self.timecard_user

        timecard_sessions = self.timecard_sessions.value

        timecard_session: dict[str, Any] | None
        if isinstance(self.timecard_session, GetMeResponse200TimecardSessionType0):
            timecard_session = self.timecard_session.to_dict()
        else:
            timecard_session = self.timecard_session

        token_expires_at = self.token_expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "issuerName": issuer_name,
                "issuer": issuer,
                "subject": subject,
                "displayName": display_name,
                "scopes": scopes,
                "departments": departments,
                "timecardUser": timecard_user,
                "timecardSessions": timecard_sessions,
                "timecardSession": timecard_session,
                "tokenExpiresAt": token_expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_me_response_200_timecard_session_type_0 import (
            GetMeResponse200TimecardSessionType0,  # noqa: PLC0415
        )
        from ..models.get_me_response_200_timecard_user_type_0 import GetMeResponse200TimecardUserType0  # noqa: PLC0415

        d = dict(src_dict)
        issuer_name = d.pop("issuerName")

        issuer = d.pop("issuer")

        subject = d.pop("subject")

        display_name = d.pop("displayName")

        scopes = cast(list[str], d.pop("scopes"))

        def _parse_departments(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                departments_type_0 = cast(list[str], data)

                return departments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        departments = _parse_departments(d.pop("departments"))

        def _parse_timecard_user(data: object) -> GetMeResponse200TimecardUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                timecard_user_type_0 = GetMeResponse200TimecardUserType0.from_dict(data)

                return timecard_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMeResponse200TimecardUserType0 | None, data)

        timecard_user = _parse_timecard_user(d.pop("timecardUser"))

        timecard_sessions = GetMeResponse200TimecardSessions(d.pop("timecardSessions"))

        def _parse_timecard_session(data: object) -> GetMeResponse200TimecardSessionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                timecard_session_type_0 = GetMeResponse200TimecardSessionType0.from_dict(data)

                return timecard_session_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMeResponse200TimecardSessionType0 | None, data)

        timecard_session = _parse_timecard_session(d.pop("timecardSession"))

        token_expires_at = d.pop("tokenExpiresAt")

        get_me_response_200 = cls(
            issuer_name=issuer_name,
            issuer=issuer,
            subject=subject,
            display_name=display_name,
            scopes=scopes,
            departments=departments,
            timecard_user=timecard_user,
            timecard_sessions=timecard_sessions,
            timecard_session=timecard_session,
            token_expires_at=token_expires_at,
        )

        return get_me_response_200
