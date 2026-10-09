from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_daily_balance_response_200_carry_overs_item_kind import GetDailyBalanceResponse200CarryOversItemKind
from ..models.get_daily_balance_response_200_carry_overs_item_unit import GetDailyBalanceResponse200CarryOversItemUnit

T = TypeVar("T", bound="GetDailyBalanceResponse200CarryOversItem")


@_attrs_define
class GetDailyBalanceResponse200CarryOversItem:
    """
    Attributes:
        kind (GetDailyBalanceResponse200CarryOversItemKind):
        account_name (str):
        source_account (None | str):
        unit (GetDailyBalanceResponse200CarryOversItemUnit):
        value (float):
    """

    kind: GetDailyBalanceResponse200CarryOversItemKind
    account_name: str
    source_account: None | str
    unit: GetDailyBalanceResponse200CarryOversItemUnit
    value: float

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        account_name = self.account_name

        source_account: None | str
        source_account = self.source_account

        unit = self.unit.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "accountName": account_name,
                "sourceAccount": source_account,
                "unit": unit,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = GetDailyBalanceResponse200CarryOversItemKind(d.pop("kind"))

        account_name = d.pop("accountName")

        def _parse_source_account(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_account = _parse_source_account(d.pop("sourceAccount"))

        unit = GetDailyBalanceResponse200CarryOversItemUnit(d.pop("unit"))

        value = d.pop("value")

        get_daily_balance_response_200_carry_overs_item = cls(
            kind=kind,
            account_name=account_name,
            source_account=source_account,
            unit=unit,
            value=value,
        )

        return get_daily_balance_response_200_carry_overs_item
