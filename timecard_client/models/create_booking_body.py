from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_booking_body_type import CreateBookingBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_booking_body_location import CreateBookingBodyLocation


T = TypeVar("T", bound="CreateBookingBody")


@_attrs_define
class CreateBookingBody:
    """
    Attributes:
        person_id (int):
        type_ (CreateBookingBodyType):
        timestamp (datetime.datetime | Unset): RFC 3339 with offset; without it timeCard books the server time
        absence_type_id (int | Unset): only for CLOCK_OUT_WITH_REASON and CLOCK_IN_WITH_REASON
        project_id (int | Unset): only for PROJECT_START
        work_operation_id (int | Unset): only for PROJECT_START
        comment (str | Unset):
        location (CreateBookingBodyLocation | Unset):
    """

    person_id: int
    type_: CreateBookingBodyType
    timestamp: datetime.datetime | Unset = UNSET
    absence_type_id: int | Unset = UNSET
    project_id: int | Unset = UNSET
    work_operation_id: int | Unset = UNSET
    comment: str | Unset = UNSET
    location: CreateBookingBodyLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        type_ = self.type_.value

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        absence_type_id = self.absence_type_id

        project_id = self.project_id

        work_operation_id = self.work_operation_id

        comment = self.comment

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "personId": person_id,
                "type": type_,
            }
        )
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
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_booking_body_location import CreateBookingBodyLocation  # noqa: PLC0415

        d = dict(src_dict)
        person_id = d.pop("personId")

        type_ = CreateBookingBodyType(d.pop("type"))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        absence_type_id = d.pop("absenceTypeId", UNSET)

        project_id = d.pop("projectId", UNSET)

        work_operation_id = d.pop("workOperationId", UNSET)

        comment = d.pop("comment", UNSET)

        _location = d.pop("location", UNSET)
        location: CreateBookingBodyLocation | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = CreateBookingBodyLocation.from_dict(_location)

        create_booking_body = cls(
            person_id=person_id,
            type_=type_,
            timestamp=timestamp,
            absence_type_id=absence_type_id,
            project_id=project_id,
            work_operation_id=work_operation_id,
            comment=comment,
            location=location,
        )

        create_booking_body.additional_properties = d
        return create_booking_body

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
