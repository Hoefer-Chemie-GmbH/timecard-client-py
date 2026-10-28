from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_availability_response_200_items_item import ListAvailabilityResponse200ItemsItem


T = TypeVar("T", bound="ListAvailabilityResponse200")


@_attrs_define
class ListAvailabilityResponse200:
    """
    Attributes:
        from_ (str):
        to (str):
        items (list[ListAvailabilityResponse200ItemsItem]):
    """

    from_: str
    to: str
    items: list[ListAvailabilityResponse200ItemsItem]

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from": from_,
                "to": to,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_availability_response_200_items_item import (
            ListAvailabilityResponse200ItemsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ListAvailabilityResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        list_availability_response_200 = cls(
            from_=from_,
            to=to,
            items=items,
        )

        return list_availability_response_200
