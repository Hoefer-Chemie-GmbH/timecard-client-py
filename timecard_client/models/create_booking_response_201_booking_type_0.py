from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_booking_response_201_booking_type_0_location_type_0 import (
        CreateBookingResponse201BookingType0LocationType0,
    )


T = TypeVar("T", bound="CreateBookingResponse201BookingType0")


@_attrs_define
class CreateBookingResponse201BookingType0:
    """
    Attributes:
        id (int):
        type_ (str):
        timestamp (None | str):
        is_active (bool):
        is_month_closed (bool):
        creator (None | str):
        absence_type_id (int | None):
        absence_type_name (None | str):
        duration (None | str):
        project_id (int | None):
        project_name (None | str):
        work_operation_id (int | None):
        work_operation_name (None | str):
        comment (None | str):
        location (CreateBookingResponse201BookingType0LocationType0 | None):
    """

    id: int
    type_: str
    timestamp: None | str
    is_active: bool
    is_month_closed: bool
    creator: None | str
    absence_type_id: int | None
    absence_type_name: None | str
    duration: None | str
    project_id: int | None
    project_name: None | str
    work_operation_id: int | None
    work_operation_name: None | str
    comment: None | str
    location: CreateBookingResponse201BookingType0LocationType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_booking_response_201_booking_type_0_location_type_0 import (
            CreateBookingResponse201BookingType0LocationType0,  # noqa: PLC0415
        )

        id = self.id

        type_ = self.type_

        timestamp: None | str
        timestamp = self.timestamp

        is_active = self.is_active

        is_month_closed = self.is_month_closed

        creator: None | str
        creator = self.creator

        absence_type_id: int | None
        absence_type_id = self.absence_type_id

        absence_type_name: None | str
        absence_type_name = self.absence_type_name

        duration: None | str
        duration = self.duration

        project_id: int | None
        project_id = self.project_id

        project_name: None | str
        project_name = self.project_name

        work_operation_id: int | None
        work_operation_id = self.work_operation_id

        work_operation_name: None | str
        work_operation_name = self.work_operation_name

        comment: None | str
        comment = self.comment

        location: dict[str, Any] | None
        if isinstance(self.location, CreateBookingResponse201BookingType0LocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "timestamp": timestamp,
                "isActive": is_active,
                "isMonthClosed": is_month_closed,
                "creator": creator,
                "absenceTypeId": absence_type_id,
                "absenceTypeName": absence_type_name,
                "duration": duration,
                "projectId": project_id,
                "projectName": project_name,
                "workOperationId": work_operation_id,
                "workOperationName": work_operation_name,
                "comment": comment,
                "location": location,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_booking_response_201_booking_type_0_location_type_0 import (
            CreateBookingResponse201BookingType0LocationType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        def _parse_timestamp(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timestamp = _parse_timestamp(d.pop("timestamp"))

        is_active = d.pop("isActive")

        is_month_closed = d.pop("isMonthClosed")

        def _parse_creator(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        creator = _parse_creator(d.pop("creator"))

        def _parse_absence_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        absence_type_id = _parse_absence_type_id(d.pop("absenceTypeId"))

        def _parse_absence_type_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        absence_type_name = _parse_absence_type_name(d.pop("absenceTypeName"))

        def _parse_duration(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        duration = _parse_duration(d.pop("duration"))

        def _parse_project_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        project_id = _parse_project_id(d.pop("projectId"))

        def _parse_project_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        project_name = _parse_project_name(d.pop("projectName"))

        def _parse_work_operation_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        work_operation_id = _parse_work_operation_id(d.pop("workOperationId"))

        def _parse_work_operation_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        work_operation_name = _parse_work_operation_name(d.pop("workOperationName"))

        def _parse_comment(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        comment = _parse_comment(d.pop("comment"))

        def _parse_location(data: object) -> CreateBookingResponse201BookingType0LocationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = CreateBookingResponse201BookingType0LocationType0.from_dict(data)

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateBookingResponse201BookingType0LocationType0 | None, data)

        location = _parse_location(d.pop("location"))

        create_booking_response_201_booking_type_0 = cls(
            id=id,
            type_=type_,
            timestamp=timestamp,
            is_active=is_active,
            is_month_closed=is_month_closed,
            creator=creator,
            absence_type_id=absence_type_id,
            absence_type_name=absence_type_name,
            duration=duration,
            project_id=project_id,
            project_name=project_name,
            work_operation_id=work_operation_id,
            work_operation_name=work_operation_name,
            comment=comment,
            location=location,
        )

        return create_booking_response_201_booking_type_0
