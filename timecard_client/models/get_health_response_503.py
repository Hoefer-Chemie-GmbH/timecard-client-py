from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.get_health_response_503_audit_db import GetHealthResponse503AuditDb
from ..models.get_health_response_503_status import GetHealthResponse503Status
from ..models.get_health_response_503_timecard import GetHealthResponse503Timecard

T = TypeVar("T", bound="GetHealthResponse503")


@_attrs_define
class GetHealthResponse503:
    """
    Attributes:
        status (GetHealthResponse503Status):
        timecard (GetHealthResponse503Timecard):
        audit_db (GetHealthResponse503AuditDb):
        version (str):
    """

    status: GetHealthResponse503Status
    timecard: GetHealthResponse503Timecard
    audit_db: GetHealthResponse503AuditDb
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
        status = GetHealthResponse503Status(d.pop("status"))

        timecard = GetHealthResponse503Timecard(d.pop("timecard"))

        audit_db = GetHealthResponse503AuditDb(d.pop("auditDb"))

        version = d.pop("version")

        get_health_response_503 = cls(
            status=status,
            timecard=timecard,
            audit_db=audit_db,
            version=version,
        )

        return get_health_response_503
