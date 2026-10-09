from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_work_operations_response_200_items_item import ListWorkOperationsResponse200ItemsItem


T = TypeVar("T", bound="ListWorkOperationsResponse200")


@_attrs_define
class ListWorkOperationsResponse200:
    """
    Attributes:
        items (list[ListWorkOperationsResponse200ItemsItem]):
    """

    items: list[ListWorkOperationsResponse200ItemsItem]

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
        from ..models.list_work_operations_response_200_items_item import (
            ListWorkOperationsResponse200ItemsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ListWorkOperationsResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        list_work_operations_response_200 = cls(
            items=items,
        )

        return list_work_operations_response_200
