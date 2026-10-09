from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListDepartmentsResponse200ItemsItem")


@_attrs_define
class ListDepartmentsResponse200ItemsItem:
    """
    Attributes:
        id (int):
        name (str):
        is_active (bool):
    """

    id: int
    name: str
    is_active: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_active = self.is_active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_active = d.pop("isActive")

        list_departments_response_200_items_item = cls(
            id=id,
            name=name,
            is_active=is_active,
        )

        return list_departments_response_200_items_item
