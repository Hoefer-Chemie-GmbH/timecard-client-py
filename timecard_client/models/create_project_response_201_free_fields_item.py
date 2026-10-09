from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_project_response_201_free_fields_item_lookup_type_0_item import (
        CreateProjectResponse201FreeFieldsItemLookupType0Item,
    )


T = TypeVar("T", bound="CreateProjectResponse201FreeFieldsItem")


@_attrs_define
class CreateProjectResponse201FreeFieldsItem:
    """
    Attributes:
        entry_id (int | None):
        free_field_id (int):
        name (str):
        data_type (str):
        lookup (list[CreateProjectResponse201FreeFieldsItemLookupType0Item] | None):
        value (None | str):
    """

    entry_id: int | None
    free_field_id: int
    name: str
    data_type: str
    lookup: list[CreateProjectResponse201FreeFieldsItemLookupType0Item] | None
    value: None | str

    def to_dict(self) -> dict[str, Any]:
        entry_id: int | None
        entry_id = self.entry_id

        free_field_id = self.free_field_id

        name = self.name

        data_type = self.data_type

        lookup: list[dict[str, Any]] | None
        if isinstance(self.lookup, list):
            lookup = []
            for lookup_type_0_item_data in self.lookup:
                lookup_type_0_item = lookup_type_0_item_data.to_dict()
                lookup.append(lookup_type_0_item)

        else:
            lookup = self.lookup

        value: None | str
        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entryId": entry_id,
                "freeFieldId": free_field_id,
                "name": name,
                "dataType": data_type,
                "lookup": lookup,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_project_response_201_free_fields_item_lookup_type_0_item import (
            CreateProjectResponse201FreeFieldsItemLookupType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_entry_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        entry_id = _parse_entry_id(d.pop("entryId"))

        free_field_id = d.pop("freeFieldId")

        name = d.pop("name")

        data_type = d.pop("dataType")

        def _parse_lookup(data: object) -> list[CreateProjectResponse201FreeFieldsItemLookupType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lookup_type_0 = []
                _lookup_type_0 = data
                for lookup_type_0_item_data in _lookup_type_0:
                    lookup_type_0_item = CreateProjectResponse201FreeFieldsItemLookupType0Item.from_dict(
                        lookup_type_0_item_data
                    )

                    lookup_type_0.append(lookup_type_0_item)

                return lookup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateProjectResponse201FreeFieldsItemLookupType0Item] | None, data)

        lookup = _parse_lookup(d.pop("lookup"))

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        create_project_response_201_free_fields_item = cls(
            entry_id=entry_id,
            free_field_id=free_field_id,
            name=name,
            data_type=data_type,
            lookup=lookup,
            value=value,
        )

        return create_project_response_201_free_fields_item
