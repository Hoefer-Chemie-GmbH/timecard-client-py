from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpsertPersonByPersonNoResponse200FreeFieldsItemLookupType0Item")


@_attrs_define
class UpsertPersonByPersonNoResponse200FreeFieldsItemLookupType0Item:
    """
    Attributes:
        key (str):
        label (str):
    """

    key: str
    label: str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        upsert_person_by_person_no_response_200_free_fields_item_lookup_type_0_item = cls(
            key=key,
            label=label,
        )

        return upsert_person_by_person_no_response_200_free_fields_item_lookup_type_0_item
