from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListAuditEventsResponse200ItemsItemUpstreamCallsItem")


@_attrs_define
class ListAuditEventsResponse200ItemsItemUpstreamCallsItem:
    """
    Attributes:
        method (str):
        path (str):
        status (int):
        duration_ms (int):
    """

    method: str
    path: str
    status: int
    duration_ms: int

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        path = self.path

        status = self.status

        duration_ms = self.duration_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
                "path": path,
                "status": status,
                "durationMs": duration_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = d.pop("method")

        path = d.pop("path")

        status = d.pop("status")

        duration_ms = d.pop("durationMs")

        list_audit_events_response_200_items_item_upstream_calls_item = cls(
            method=method,
            path=path,
            status=status,
            duration_ms=duration_ms,
        )

        return list_audit_events_response_200_items_item_upstream_calls_item
