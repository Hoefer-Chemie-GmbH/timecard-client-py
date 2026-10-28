from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.list_availability_response_200_items_item_days_item_status import (
    ListAvailabilityResponse200ItemsItemDaysItemStatus,
)

T = TypeVar("T", bound="ListAvailabilityResponse200ItemsItemDaysItem")


@_attrs_define
class ListAvailabilityResponse200ItemsItemDaysItem:
    """
    Attributes:
        date (str):
        status (ListAvailabilityResponse200ItemsItemDaysItemStatus):
    """

    date: str
    status: ListAvailabilityResponse200ItemsItemDaysItemStatus

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        status = ListAvailabilityResponse200ItemsItemDaysItemStatus(d.pop("status"))

        list_availability_response_200_items_item_days_item = cls(
            date=date,
            status=status,
        )

        return list_availability_response_200_items_item_days_item
