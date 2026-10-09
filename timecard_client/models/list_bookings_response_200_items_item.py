from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListBookingsResponse200ItemsItem")


@_attrs_define
class ListBookingsResponse200ItemsItem:
    """
    Attributes:
        id (int):
        person_id (int):
        timestamp (None | str):
        type_ (str):
        time (None | str):
        half_day (bool):
        reason (None | str):
        info (None | str):
        color (None | str):
        inconsistency (None | str):
        comment (None | str):
        absence_type_id (int | None):
        project_id (int | None):
        work_operation_id (int | None):
        has_replace_time (bool | None):
        valid (bool | None):
    """

    id: int
    person_id: int
    timestamp: None | str
    type_: str
    time: None | str
    half_day: bool
    reason: None | str
    info: None | str
    color: None | str
    inconsistency: None | str
    comment: None | str
    absence_type_id: int | None
    project_id: int | None
    work_operation_id: int | None
    has_replace_time: bool | None
    valid: bool | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        person_id = self.person_id

        timestamp: None | str
        timestamp = self.timestamp

        type_ = self.type_

        time: None | str
        time = self.time

        half_day = self.half_day

        reason: None | str
        reason = self.reason

        info: None | str
        info = self.info

        color: None | str
        color = self.color

        inconsistency: None | str
        inconsistency = self.inconsistency

        comment: None | str
        comment = self.comment

        absence_type_id: int | None
        absence_type_id = self.absence_type_id

        project_id: int | None
        project_id = self.project_id

        work_operation_id: int | None
        work_operation_id = self.work_operation_id

        has_replace_time: bool | None
        has_replace_time = self.has_replace_time

        valid: bool | None
        valid = self.valid

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "personId": person_id,
                "timestamp": timestamp,
                "type": type_,
                "time": time,
                "halfDay": half_day,
                "reason": reason,
                "info": info,
                "color": color,
                "inconsistency": inconsistency,
                "comment": comment,
                "absenceTypeId": absence_type_id,
                "projectId": project_id,
                "workOperationId": work_operation_id,
                "hasReplaceTime": has_replace_time,
                "valid": valid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        person_id = d.pop("personId")

        def _parse_timestamp(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timestamp = _parse_timestamp(d.pop("timestamp"))

        type_ = d.pop("type")

        def _parse_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        time = _parse_time(d.pop("time"))

        half_day = d.pop("halfDay")

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        def _parse_info(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        info = _parse_info(d.pop("info"))

        def _parse_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        color = _parse_color(d.pop("color"))

        def _parse_inconsistency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        inconsistency = _parse_inconsistency(d.pop("inconsistency"))

        def _parse_comment(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        comment = _parse_comment(d.pop("comment"))

        def _parse_absence_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        absence_type_id = _parse_absence_type_id(d.pop("absenceTypeId"))

        def _parse_project_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        project_id = _parse_project_id(d.pop("projectId"))

        def _parse_work_operation_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        work_operation_id = _parse_work_operation_id(d.pop("workOperationId"))

        def _parse_has_replace_time(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        has_replace_time = _parse_has_replace_time(d.pop("hasReplaceTime"))

        def _parse_valid(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        valid = _parse_valid(d.pop("valid"))

        list_bookings_response_200_items_item = cls(
            id=id,
            person_id=person_id,
            timestamp=timestamp,
            type_=type_,
            time=time,
            half_day=half_day,
            reason=reason,
            info=info,
            color=color,
            inconsistency=inconsistency,
            comment=comment,
            absence_type_id=absence_type_id,
            project_id=project_id,
            work_operation_id=work_operation_id,
            has_replace_time=has_replace_time,
            valid=valid,
        )

        return list_bookings_response_200_items_item
