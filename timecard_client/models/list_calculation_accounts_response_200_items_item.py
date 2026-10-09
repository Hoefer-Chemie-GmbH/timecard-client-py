from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.list_calculation_accounts_response_200_items_item_unit import (
    ListCalculationAccountsResponse200ItemsItemUnit,
)

T = TypeVar("T", bound="ListCalculationAccountsResponse200ItemsItem")


@_attrs_define
class ListCalculationAccountsResponse200ItemsItem:
    """
    Attributes:
        calculation_id (int):
        name (str):
        unit (ListCalculationAccountsResponse200ItemsItemUnit):
    """

    calculation_id: int
    name: str
    unit: ListCalculationAccountsResponse200ItemsItemUnit

    def to_dict(self) -> dict[str, Any]:
        calculation_id = self.calculation_id

        name = self.name

        unit = self.unit.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "calculationId": calculation_id,
                "name": name,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calculation_id = d.pop("calculationId")

        name = d.pop("name")

        unit = ListCalculationAccountsResponse200ItemsItemUnit(d.pop("unit"))

        list_calculation_accounts_response_200_items_item = cls(
            calculation_id=calculation_id,
            name=name,
            unit=unit,
        )

        return list_calculation_accounts_response_200_items_item
