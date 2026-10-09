from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBookingBody")


@_attrs_define
class UpdateBookingBody:
    """
    Attributes:
        timestamp (datetime.datetime | Unset):
        absence_type_id (int | None | Unset):
        project_id (int | None | Unset):
        work_operation_id (int | None | Unset):
        comment (None | str | Unset):
    """

    timestamp: datetime.datetime | Unset = UNSET
    absence_type_id: int | None | Unset = UNSET
    project_id: int | None | Unset = UNSET
    work_operation_id: int | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        absence_type_id: int | None | Unset
        if isinstance(self.absence_type_id, Unset):
            absence_type_id = UNSET
        else:
            absence_type_id = self.absence_type_id

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        work_operation_id: int | None | Unset
        if isinstance(self.work_operation_id, Unset):
            work_operation_id = UNSET
        else:
            work_operation_id = self.work_operation_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if absence_type_id is not UNSET:
            field_dict["absenceTypeId"] = absence_type_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if work_operation_id is not UNSET:
            field_dict["workOperationId"] = work_operation_id
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        def _parse_absence_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        absence_type_id = _parse_absence_type_id(d.pop("absenceTypeId", UNSET))

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_work_operation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        work_operation_id = _parse_work_operation_id(d.pop("workOperationId", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        update_booking_body = cls(
            timestamp=timestamp,
            absence_type_id=absence_type_id,
            project_id=project_id,
            work_operation_id=work_operation_id,
            comment=comment,
        )

        update_booking_body.additional_properties = d
        return update_booking_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
