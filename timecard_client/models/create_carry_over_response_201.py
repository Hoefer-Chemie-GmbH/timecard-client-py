from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_carry_over_response_201_unit import CreateCarryOverResponse201Unit

T = TypeVar("T", bound="CreateCarryOverResponse201")


@_attrs_define
class CreateCarryOverResponse201:
    """
    Attributes:
        id (int):
        person_id (int):
        calculation_id (int):
        calc_account_id (int | None):
        balance_date (str):
        unit (CreateCarryOverResponse201Unit):
        value (float):
        formatted_value (None | str):
        reason (None | str):
        add_to_total (bool):
    """

    id: int
    person_id: int
    calculation_id: int
    calc_account_id: int | None
    balance_date: str
    unit: CreateCarryOverResponse201Unit
    value: float
    formatted_value: None | str
    reason: None | str
    add_to_total: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        person_id = self.person_id

        calculation_id = self.calculation_id

        calc_account_id: int | None
        calc_account_id = self.calc_account_id

        balance_date = self.balance_date

        unit = self.unit.value

        value = self.value

        formatted_value: None | str
        formatted_value = self.formatted_value

        reason: None | str
        reason = self.reason

        add_to_total = self.add_to_total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "personId": person_id,
                "calculationId": calculation_id,
                "calcAccountId": calc_account_id,
                "balanceDate": balance_date,
                "unit": unit,
                "value": value,
                "formattedValue": formatted_value,
                "reason": reason,
                "addToTotal": add_to_total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        person_id = d.pop("personId")

        calculation_id = d.pop("calculationId")

        def _parse_calc_account_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        calc_account_id = _parse_calc_account_id(d.pop("calcAccountId"))

        balance_date = d.pop("balanceDate")

        unit = CreateCarryOverResponse201Unit(d.pop("unit"))

        value = d.pop("value")

        def _parse_formatted_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        formatted_value = _parse_formatted_value(d.pop("formattedValue"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        add_to_total = d.pop("addToTotal")

        create_carry_over_response_201 = cls(
            id=id,
            person_id=person_id,
            calculation_id=calculation_id,
            calc_account_id=calc_account_id,
            balance_date=balance_date,
            unit=unit,
            value=value,
            formatted_value=formatted_value,
            reason=reason,
            add_to_total=add_to_total,
        )

        return create_carry_over_response_201
