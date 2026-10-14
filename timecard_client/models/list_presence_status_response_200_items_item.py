from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.list_presence_status_response_200_items_item_status import ListPresenceStatusResponse200ItemsItemStatus

T = TypeVar("T", bound="ListPresenceStatusResponse200ItemsItem")


@_attrs_define
class ListPresenceStatusResponse200ItemsItem:
    """
    Attributes:
        person_id (int):
        status (ListPresenceStatusResponse200ItemsItemStatus):
    """

    person_id: int
    status: ListPresenceStatusResponse200ItemsItemStatus

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = d.pop("personId")

        status = ListPresenceStatusResponse200ItemsItemStatus(d.pop("status"))

        list_presence_status_response_200_items_item = cls(
            person_id=person_id,
            status=status,
        )

        return list_presence_status_response_200_items_item
