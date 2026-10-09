from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_persons_response_200_items_item import ListPersonsResponse200ItemsItem


T = TypeVar("T", bound="ListPersonsResponse200")


@_attrs_define
class ListPersonsResponse200:
    """
    Attributes:
        items (list[ListPersonsResponse200ItemsItem]):
        total (int):
        page (int):
        page_size (int):
    """

    items: list[ListPersonsResponse200ItemsItem]
    total: int
    page: int
    page_size: int

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "total": total,
                "page": page,
                "pageSize": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_persons_response_200_items_item import ListPersonsResponse200ItemsItem  # noqa: PLC0415

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ListPersonsResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("pageSize")

        list_persons_response_200 = cls(
            items=items,
            total=total,
            page=page,
            page_size=page_size,
        )

        return list_persons_response_200
