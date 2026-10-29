from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_presence_status_response_200_items_item_status import ListPresenceStatusResponse200ItemsItemStatus

T = TypeVar("T", bound="ListPresenceStatusResponse200ItemsItem")


@_attrs_define
class ListPresenceStatusResponse200ItemsItem:
    """
    Attributes:
        person_id (int):
        person_no (None | str):
        status (ListPresenceStatusResponse200ItemsItemStatus):
    """

    person_id: int
    person_no: None | str
    status: ListPresenceStatusResponse200ItemsItemStatus

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        person_no: None | str
        person_no = self.person_no

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "personNo": person_no,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = d.pop("personId")

        def _parse_person_no(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        person_no = _parse_person_no(d.pop("personNo"))

        status = ListPresenceStatusResponse200ItemsItemStatus(d.pop("status"))

        list_presence_status_response_200_items_item = cls(
            person_id=person_id,
            person_no=person_no,
            status=status,
        )

        return list_presence_status_response_200_items_item
