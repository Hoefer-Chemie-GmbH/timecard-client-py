from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_free_field_response_200_lookup_type_0_item import GetFreeFieldResponse200LookupType0Item


T = TypeVar("T", bound="GetFreeFieldResponse200")


@_attrs_define
class GetFreeFieldResponse200:
    """
    Attributes:
        id (int):
        name (str):
        scope (str):
        is_active (bool):
        order_no (int | None):
        data_type (str):
        lookup (list[GetFreeFieldResponse200LookupType0Item] | None):
        is_used (bool):
    """

    id: int
    name: str
    scope: str
    is_active: bool
    order_no: int | None
    data_type: str
    lookup: list[GetFreeFieldResponse200LookupType0Item] | None
    is_used: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        scope = self.scope

        is_active = self.is_active

        order_no: int | None
        order_no = self.order_no

        data_type = self.data_type

        lookup: list[dict[str, Any]] | None
        if isinstance(self.lookup, list):
            lookup = []
            for lookup_type_0_item_data in self.lookup:
                lookup_type_0_item = lookup_type_0_item_data.to_dict()
                lookup.append(lookup_type_0_item)

        else:
            lookup = self.lookup

        is_used = self.is_used

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "scope": scope,
                "isActive": is_active,
                "orderNo": order_no,
                "dataType": data_type,
                "lookup": lookup,
                "isUsed": is_used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_free_field_response_200_lookup_type_0_item import (
            GetFreeFieldResponse200LookupType0Item,  # noqa: PLC0415
        )

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

        data_type = d.pop("dataType")

        def _parse_lookup(data: object) -> list[GetFreeFieldResponse200LookupType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lookup_type_0 = []
                _lookup_type_0 = data
                for lookup_type_0_item_data in _lookup_type_0:
                    lookup_type_0_item = GetFreeFieldResponse200LookupType0Item.from_dict(lookup_type_0_item_data)

                    lookup_type_0.append(lookup_type_0_item)

                return lookup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetFreeFieldResponse200LookupType0Item] | None, data)

        lookup = _parse_lookup(d.pop("lookup"))

        is_used = d.pop("isUsed")

        get_free_field_response_200 = cls(
            id=id,
            name=name,
            scope=scope,
            is_active=is_active,
            order_no=order_no,
            data_type=data_type,
            lookup=lookup,
            is_used=is_used,
        )

        return get_free_field_response_200
