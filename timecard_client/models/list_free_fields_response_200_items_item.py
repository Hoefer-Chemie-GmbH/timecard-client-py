from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListFreeFieldsResponse200ItemsItem")


@_attrs_define
class ListFreeFieldsResponse200ItemsItem:
    """
    Attributes:
        id (int):
        name (str):
        scope (str):
        is_active (bool):
        order_no (int | None):
    """

    id: int
    name: str
    scope: str
    is_active: bool
    order_no: int | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        scope = self.scope

        is_active = self.is_active

        order_no: int | None
        order_no = self.order_no

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "scope": scope,
                "isActive": is_active,
                "orderNo": order_no,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        scope = d.pop("scope")

        is_active = d.pop("isActive")

        def _parse_order_no(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        order_no = _parse_order_no(d.pop("orderNo"))

        list_free_fields_response_200_items_item = cls(
            id=id,
            name=name,
            scope=scope,
            is_active=is_active,
            order_no=order_no,
        )

        return list_free_fields_response_200_items_item
