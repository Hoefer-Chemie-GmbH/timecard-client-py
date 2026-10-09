from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetPersonCalendarResponse200PublicHolidaysItem")


@_attrs_define
class GetPersonCalendarResponse200PublicHolidaysItem:
    """
    Attributes:
        date (str):
        name (None | str):
        color (None | str):
        requested (bool):
        also_illness (bool):
    """

    date: str
    name: None | str
    color: None | str
    requested: bool
    also_illness: bool

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        name: None | str
        name = self.name

        color: None | str
        color = self.color

        requested = self.requested

        also_illness = self.also_illness

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "name": name,
                "color": color,
                "requested": requested,
                "alsoIllness": also_illness,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        color = _parse_color(d.pop("color"))

        requested = d.pop("requested")

        also_illness = d.pop("alsoIllness")

        get_person_calendar_response_200_public_holidays_item = cls(
            date=date,
            name=name,
            color=color,
            requested=requested,
            also_illness=also_illness,
        )

        return get_person_calendar_response_200_public_holidays_item
