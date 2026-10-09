from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetPersonByPersonNoResponse200TimeRecordingSupervisorsItem")


@_attrs_define
class GetPersonByPersonNoResponse200TimeRecordingSupervisorsItem:
    """
    Attributes:
        type_ (int):
        department_id (int | None):
        group_id (int | None):
        person_id (int | None):
        global_ (bool):
    """

    type_: int
    department_id: int | None
    group_id: int | None
    person_id: int | None
    global_: bool

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        department_id: int | None
        department_id = self.department_id

        group_id: int | None
        group_id = self.group_id

        person_id: int | None
        person_id = self.person_id

        global_ = self.global_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "departmentId": department_id,
                "groupId": group_id,
                "personId": person_id,
                "global": global_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        def _parse_department_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        department_id = _parse_department_id(d.pop("departmentId"))

        def _parse_group_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        group_id = _parse_group_id(d.pop("groupId"))

        def _parse_person_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        person_id = _parse_person_id(d.pop("personId"))

        global_ = d.pop("global")

        get_person_by_person_no_response_200_time_recording_supervisors_item = cls(
            type_=type_,
            department_id=department_id,
            group_id=group_id,
            person_id=person_id,
            global_=global_,
        )

        return get_person_by_person_no_response_200_time_recording_supervisors_item
