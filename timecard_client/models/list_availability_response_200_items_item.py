from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_availability_response_200_items_item_days_item import (
        ListAvailabilityResponse200ItemsItemDaysItem,
    )


T = TypeVar("T", bound="ListAvailabilityResponse200ItemsItem")


@_attrs_define
class ListAvailabilityResponse200ItemsItem:
    """
    Attributes:
        person_id (int):
        days (list[ListAvailabilityResponse200ItemsItemDaysItem]):
    """

    person_id: int
    days: list[ListAvailabilityResponse200ItemsItemDaysItem]

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_availability_response_200_items_item_days_item import (
            ListAvailabilityResponse200ItemsItemDaysItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        person_id = d.pop("personId")

        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = ListAvailabilityResponse200ItemsItemDaysItem.from_dict(days_item_data)

            days.append(days_item)

        list_availability_response_200_items_item = cls(
            person_id=person_id,
            days=days,
        )

        return list_availability_response_200_items_item
