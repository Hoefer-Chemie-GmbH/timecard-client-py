from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.get_health_response_200_audit_db import GetHealthResponse200AuditDb
from ..models.get_health_response_200_status import GetHealthResponse200Status
from ..models.get_health_response_200_timecard import GetHealthResponse200Timecard

T = TypeVar("T", bound="GetHealthResponse200")


@_attrs_define
class GetHealthResponse200:
    """
    Attributes:
        status (GetHealthResponse200Status):
        timecard (GetHealthResponse200Timecard):
        audit_db (GetHealthResponse200AuditDb):
        version (str):
    """

    status: GetHealthResponse200Status
    timecard: GetHealthResponse200Timecard
    audit_db: GetHealthResponse200AuditDb
    version: str

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        timecard = self.timecard.value

        audit_db = self.audit_db.value

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "timecard": timecard,
                "auditDb": audit_db,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = GetHealthResponse200Status(d.pop("status"))

        timecard = GetHealthResponse200Timecard(d.pop("timecard"))

        audit_db = GetHealthResponse200AuditDb(d.pop("auditDb"))

        version = d.pop("version")

        get_health_response_200 = cls(
            status=status,
            timecard=timecard,
            audit_db=audit_db,
            version=version,
        )

        return get_health_response_200
