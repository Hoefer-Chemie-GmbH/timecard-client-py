from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetDailyBalanceResponse200EvaluationChanged")


@_attrs_define
class GetDailyBalanceResponse200EvaluationChanged:
    """
    Attributes:
        active (bool):
        period (None | str):
        reason (None | str):
    """

    active: bool
    period: None | str
    reason: None | str

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        period: None | str
        period = self.period

        reason: None | str
        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active": active,
                "period": period,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        def _parse_period(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        period = _parse_period(d.pop("period"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        get_daily_balance_response_200_evaluation_changed = cls(
            active=active,
            period=period,
            reason=reason,
        )

        return get_daily_balance_response_200_evaluation_changed
