from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_daily_balance_response_200_calculations_item_unit import (
    GetDailyBalanceResponse200CalculationsItemUnit,
)

T = TypeVar("T", bound="GetDailyBalanceResponse200CalculationsItem")


@_attrs_define
class GetDailyBalanceResponse200CalculationsItem:
    """
    Attributes:
        calculation_id (int):
        name (str):
        period (str):
        unit (GetDailyBalanceResponse200CalculationsItemUnit):
        is_holiday (bool):
        absence_name (None | str):
        range_from (None | str):
        range_to (None | str):
        range_text (None | str):
        start_value (float):
        target_value (float | None):
        total_value (float):
        carry_over (float):
        current_value (float):
        taken_in_range (float | None):
        available (float | None):
        taken (float | None):
        requested (float | None):
        approved (float | None):
        pending_change_or_cancel (float | None):
    """

    calculation_id: int
    name: str
    period: str
    unit: GetDailyBalanceResponse200CalculationsItemUnit
    is_holiday: bool
    absence_name: None | str
    range_from: None | str
    range_to: None | str
    range_text: None | str
    start_value: float
    target_value: float | None
    total_value: float
    carry_over: float
    current_value: float
    taken_in_range: float | None
    available: float | None
    taken: float | None
    requested: float | None
    approved: float | None
    pending_change_or_cancel: float | None

    def to_dict(self) -> dict[str, Any]:
        calculation_id = self.calculation_id

        name = self.name

        period = self.period

        unit = self.unit.value

        is_holiday = self.is_holiday

        absence_name: None | str
        absence_name = self.absence_name

        range_from: None | str
        range_from = self.range_from

        range_to: None | str
        range_to = self.range_to

        range_text: None | str
        range_text = self.range_text

        start_value = self.start_value

        target_value: float | None
        target_value = self.target_value

        total_value = self.total_value

        carry_over = self.carry_over

        current_value = self.current_value

        taken_in_range: float | None
        taken_in_range = self.taken_in_range

        available: float | None
        available = self.available

        taken: float | None
        taken = self.taken

        requested: float | None
        requested = self.requested

        approved: float | None
        approved = self.approved

        pending_change_or_cancel: float | None
        pending_change_or_cancel = self.pending_change_or_cancel

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "calculationId": calculation_id,
                "name": name,
                "period": period,
                "unit": unit,
                "isHoliday": is_holiday,
                "absenceName": absence_name,
                "rangeFrom": range_from,
                "rangeTo": range_to,
                "rangeText": range_text,
                "startValue": start_value,
                "targetValue": target_value,
                "totalValue": total_value,
                "carryOver": carry_over,
                "currentValue": current_value,
                "takenInRange": taken_in_range,
                "available": available,
                "taken": taken,
                "requested": requested,
                "approved": approved,
                "pendingChangeOrCancel": pending_change_or_cancel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calculation_id = d.pop("calculationId")

        name = d.pop("name")

        period = d.pop("period")

        unit = GetDailyBalanceResponse200CalculationsItemUnit(d.pop("unit"))

        is_holiday = d.pop("isHoliday")

        def _parse_absence_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        absence_name = _parse_absence_name(d.pop("absenceName"))

        def _parse_range_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        range_from = _parse_range_from(d.pop("rangeFrom"))

        def _parse_range_to(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        range_to = _parse_range_to(d.pop("rangeTo"))

        def _parse_range_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        range_text = _parse_range_text(d.pop("rangeText"))

        start_value = d.pop("startValue")

        def _parse_target_value(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        target_value = _parse_target_value(d.pop("targetValue"))

        total_value = d.pop("totalValue")

        carry_over = d.pop("carryOver")

        current_value = d.pop("currentValue")

        def _parse_taken_in_range(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        taken_in_range = _parse_taken_in_range(d.pop("takenInRange"))

        def _parse_available(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        available = _parse_available(d.pop("available"))

        def _parse_taken(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        taken = _parse_taken(d.pop("taken"))

        def _parse_requested(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        requested = _parse_requested(d.pop("requested"))

        def _parse_approved(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        approved = _parse_approved(d.pop("approved"))

        def _parse_pending_change_or_cancel(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        pending_change_or_cancel = _parse_pending_change_or_cancel(d.pop("pendingChangeOrCancel"))

        get_daily_balance_response_200_calculations_item = cls(
            calculation_id=calculation_id,
            name=name,
            period=period,
            unit=unit,
            is_holiday=is_holiday,
            absence_name=absence_name,
            range_from=range_from,
            range_to=range_to,
            range_text=range_text,
            start_value=start_value,
            target_value=target_value,
            total_value=total_value,
            carry_over=carry_over,
            current_value=current_value,
            taken_in_range=taken_in_range,
            available=available,
            taken=taken,
            requested=requested,
            approved=approved,
            pending_change_or_cancel=pending_change_or_cancel,
        )

        return get_daily_balance_response_200_calculations_item
