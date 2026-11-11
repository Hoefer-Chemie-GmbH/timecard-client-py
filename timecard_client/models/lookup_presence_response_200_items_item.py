from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.lookup_presence_response_200_items_item_status import LookupPresenceResponse200ItemsItemStatus

T = TypeVar("T", bound="LookupPresenceResponse200ItemsItem")


@_attrs_define
class LookupPresenceResponse200ItemsItem:
    """
    Attributes:
        person_id (int):
        status (LookupPresenceResponse200ItemsItemStatus):
    """

    person_id: int
    status: LookupPresenceResponse200ItemsItemStatus

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

        status = LookupPresenceResponse200ItemsItemStatus(d.pop("status"))

        lookup_presence_response_200_items_item = cls(
            person_id=person_id,
            status=status,
        )

        return lookup_presence_response_200_items_item
