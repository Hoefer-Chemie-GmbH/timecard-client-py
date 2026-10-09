from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_group_members_response_200_items_item import ListGroupMembersResponse200ItemsItem


T = TypeVar("T", bound="ListGroupMembersResponse200")


@_attrs_define
class ListGroupMembersResponse200:
    """
    Attributes:
        items (list[ListGroupMembersResponse200ItemsItem]):
    """

    items: list[ListGroupMembersResponse200ItemsItem]

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
        from ..models.list_group_members_response_200_items_item import (
            ListGroupMembersResponse200ItemsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ListGroupMembersResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        list_group_members_response_200 = cls(
            items=items,
        )

        return list_group_members_response_200
