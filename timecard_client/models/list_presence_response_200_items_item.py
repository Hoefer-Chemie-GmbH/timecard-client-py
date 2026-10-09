from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_presence_response_200_items_item_status import ListPresenceResponse200ItemsItemStatus

T = TypeVar("T", bound="ListPresenceResponse200ItemsItem")


@_attrs_define
class ListPresenceResponse200ItemsItem:
    """
    Attributes:
        person_id (int):
        person_no (None | str):
        first_name (str):
        last_name (str):
        department (None | str):
        status (ListPresenceResponse200ItemsItemStatus):
        reason (None | str):
        first_clock_in (None | str):
        location (None | str):
    """

    person_id: int
    person_no: None | str
    first_name: str
    last_name: str
    department: None | str
    status: ListPresenceResponse200ItemsItemStatus
    reason: None | str
    first_clock_in: None | str
    location: None | str

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        person_no: None | str
        person_no = self.person_no

        first_name = self.first_name

        last_name = self.last_name

        department: None | str
        department = self.department

        status = self.status.value

        reason: None | str
        reason = self.reason

        first_clock_in: None | str
        first_clock_in = self.first_clock_in

        location: None | str
        location = self.location

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "personNo": person_no,
                "firstName": first_name,
                "lastName": last_name,
                "department": department,
                "status": status,
                "reason": reason,
                "firstClockIn": first_clock_in,
                "location": location,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = d.pop("personId")

        def _parse_person_no(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        person_no = _parse_person_no(d.pop("personNo"))

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        def _parse_department(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        department = _parse_department(d.pop("department"))

        status = ListPresenceResponse200ItemsItemStatus(d.pop("status"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        def _parse_first_clock_in(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_clock_in = _parse_first_clock_in(d.pop("firstClockIn"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        list_presence_response_200_items_item = cls(
            person_id=person_id,
            person_no=person_no,
            first_name=first_name,
            last_name=last_name,
            department=department,
            status=status,
            reason=reason,
            first_clock_in=first_clock_in,
            location=location,
        )

        return list_presence_response_200_items_item
