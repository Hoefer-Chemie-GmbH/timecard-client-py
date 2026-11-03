from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAuditEventResponse200UpstreamCallsItem")


@_attrs_define
class GetAuditEventResponse200UpstreamCallsItem:
    """
    Attributes:
        method (str):
        path (str):
        status (int):
        duration_ms (int):
        timecard_user (str | Unset): delegated timeCard user that made the call; absent = technical user
        timecard_session (str | Unset): timeCard user of the pass-through session that made the call
    """

    method: str
    path: str
    status: int
    duration_ms: int
    timecard_user: str | Unset = UNSET
    timecard_session: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        path = self.path

        status = self.status

        duration_ms = self.duration_ms

        timecard_user = self.timecard_user

        timecard_session = self.timecard_session

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
                "path": path,
                "status": status,
                "durationMs": duration_ms,
            }
        )
        if timecard_user is not UNSET:
            field_dict["timecardUser"] = timecard_user
        if timecard_session is not UNSET:
            field_dict["timecardSession"] = timecard_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = d.pop("method")

        path = d.pop("path")

        status = d.pop("status")

        duration_ms = d.pop("durationMs")

        timecard_user = d.pop("timecardUser", UNSET)

        timecard_session = d.pop("timecardSession", UNSET)

        get_audit_event_response_200_upstream_calls_item = cls(
            method=method,
            path=path,
            status=status,
            duration_ms=duration_ms,
            timecard_user=timecard_user,
            timecard_session=timecard_session,
        )

        return get_audit_event_response_200_upstream_calls_item
