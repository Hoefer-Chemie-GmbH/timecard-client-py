from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.lookup_presence_response_200_items_item import LookupPresenceResponse200ItemsItem


T = TypeVar("T", bound="LookupPresenceResponse200")


@_attrs_define
class LookupPresenceResponse200:
    """
    Attributes:
        items (list[LookupPresenceResponse200ItemsItem]):
    """

    items: list[LookupPresenceResponse200ItemsItem]

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_presence_response_200_items_item import LookupPresenceResponse200ItemsItem  # noqa: PLC0415

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = LookupPresenceResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        lookup_presence_response_200 = cls(
            items=items,
        )

        return lookup_presence_response_200
