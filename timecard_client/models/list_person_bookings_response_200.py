from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_person_bookings_response_200_items_item import ListPersonBookingsResponse200ItemsItem


T = TypeVar("T", bound="ListPersonBookingsResponse200")


@_attrs_define
class ListPersonBookingsResponse200:
    """
    Attributes:
        items (list[ListPersonBookingsResponse200ItemsItem]):
        total (int):
        from_ (str):
        to (str):
    """

    items: list[ListPersonBookingsResponse200ItemsItem]
    total: int
    from_: str
    to: str

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total = self.total

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "total": total,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_person_bookings_response_200_items_item import (
            ListPersonBookingsResponse200ItemsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ListPersonBookingsResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        total = d.pop("total")

        from_ = d.pop("from")

        to = d.pop("to")

        list_person_bookings_response_200 = cls(
            items=items,
            total=total,
            from_=from_,
            to=to,
        )

        return list_person_bookings_response_200
