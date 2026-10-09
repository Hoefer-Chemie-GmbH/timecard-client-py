from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListWorkingProfilesResponse200ItemsItem")


@_attrs_define
class ListWorkingProfilesResponse200ItemsItem:
    """
    Attributes:
        id (int):
        name (str):
        type_ (str):
        is_active (bool):
    """

    id: int
    name: str
    type_: str
    is_active: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        is_active = self.is_active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        is_active = d.pop("isActive")

        list_working_profiles_response_200_items_item = cls(
            id=id,
            name=name,
            type_=type_,
            is_active=is_active,
        )

        return list_working_profiles_response_200_items_item
