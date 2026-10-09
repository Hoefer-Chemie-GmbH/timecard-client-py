from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem")


@_attrs_define
class GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem:
    """
    Attributes:
        reason (str):
        fraction (float):
        color (None | str):
    """

    reason: str
    fraction: float
    color: None | str

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        fraction = self.fraction

        color: None | str
        color = self.color

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reason": reason,
                "fraction": fraction,
                "color": color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        fraction = d.pop("fraction")

        def _parse_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        color = _parse_color(d.pop("color"))

        get_person_absence_overview_response_200_items_item_days_item_entries_item = cls(
            reason=reason,
            fraction=fraction,
            color=color,
        )

        return get_person_absence_overview_response_200_items_item_days_item_entries_item
