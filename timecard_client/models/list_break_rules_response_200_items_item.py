from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListBreakRulesResponse200ItemsItem")


@_attrs_define
class ListBreakRulesResponse200ItemsItem:
    """
    Attributes:
        id (int):
        name (str):
        type_ (str):
    """

    id: int
    name: str
    type_: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        list_break_rules_response_200_items_item = cls(
            id=id,
            name=name,
            type_=type_,
        )

        return list_break_rules_response_200_items_item
