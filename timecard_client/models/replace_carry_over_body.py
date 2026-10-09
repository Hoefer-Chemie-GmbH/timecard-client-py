from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplaceCarryOverBody")


@_attrs_define
class ReplaceCarryOverBody:
    """
    Attributes:
        balance_date (str): day the carry-over is booked on
        value (float): in the unit of the calculation account: days or seconds
        reason (None | str | Unset):
        add_to_total (bool | Unset):  Default: True.
    """

    balance_date: str
    value: float
    reason: None | str | Unset = UNSET
    add_to_total: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_date = self.balance_date

        value = self.value

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        add_to_total = self.add_to_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balanceDate": balance_date,
                "value": value,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if add_to_total is not UNSET:
            field_dict["addToTotal"] = add_to_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance_date = d.pop("balanceDate")

        value = d.pop("value")

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        add_to_total = d.pop("addToTotal", UNSET)

        replace_carry_over_body = cls(
            balance_date=balance_date,
            value=value,
            reason=reason,
            add_to_total=add_to_total,
        )

        replace_carry_over_body.additional_properties = d
        return replace_carry_over_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
