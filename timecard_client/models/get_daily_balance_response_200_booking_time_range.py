from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetDailyBalanceResponse200BookingTimeRange")


@_attrs_define
class GetDailyBalanceResponse200BookingTimeRange:
    """
    Attributes:
        start (None | str):
        end (None | str):
        shifted (bool):
    """

    start: None | str
    end: None | str
    shifted: bool

    def to_dict(self) -> dict[str, Any]:
        start: None | str
        start = self.start

        end: None | str
        end = self.end

        shifted = self.shifted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "end": end,
                "shifted": shifted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_start(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        start = _parse_start(d.pop("start"))

        def _parse_end(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end = _parse_end(d.pop("end"))

        shifted = d.pop("shifted")

        get_daily_balance_response_200_booking_time_range = cls(
            start=start,
            end=end,
            shifted=shifted,
        )

        return get_daily_balance_response_200_booking_time_range
