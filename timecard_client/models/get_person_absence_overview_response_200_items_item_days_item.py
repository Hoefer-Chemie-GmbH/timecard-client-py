from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_person_absence_overview_response_200_items_item_days_item_entries_item import (
        GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem,
    )


T = TypeVar("T", bound="GetPersonAbsenceOverviewResponse200ItemsItemDaysItem")


@_attrs_define
class GetPersonAbsenceOverviewResponse200ItemsItemDaysItem:
    """
    Attributes:
        day (int):
        date (None | str):
        entries (list[GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem]):
    """

    day: int
    date: None | str
    entries: list[GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem]

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        date: None | str
        date = self.date

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "day": day,
                "date": date,
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_person_absence_overview_response_200_items_item_days_item_entries_item import (
            GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        day = d.pop("day")

        def _parse_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        date = _parse_date(d.pop("date"))

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        get_person_absence_overview_response_200_items_item_days_item = cls(
            day=day,
            date=date,
            entries=entries,
        )

        return get_person_absence_overview_response_200_items_item_days_item
