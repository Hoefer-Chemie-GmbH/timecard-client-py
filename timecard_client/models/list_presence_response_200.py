from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_presence_response_200_items_item import ListPresenceResponse200ItemsItem


T = TypeVar("T", bound="ListPresenceResponse200")


@_attrs_define
class ListPresenceResponse200:
    """
    Attributes:
        as_of (str):
        items (list[ListPresenceResponse200ItemsItem]):
    """

    as_of: str
    items: list[ListPresenceResponse200ItemsItem]

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asOf": as_of,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_presence_response_200_items_item import ListPresenceResponse200ItemsItem  # noqa: PLC0415

        d = dict(src_dict)
        as_of = d.pop("asOf")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ListPresenceResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        list_presence_response_200 = cls(
            as_of=as_of,
            items=items,
        )

        return list_presence_response_200
