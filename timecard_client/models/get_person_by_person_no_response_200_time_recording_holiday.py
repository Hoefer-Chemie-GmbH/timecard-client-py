from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetPersonByPersonNoResponse200TimeRecordingHoliday")


@_attrs_define
class GetPersonByPersonNoResponse200TimeRecordingHoliday:
    """
    Attributes:
        profile_id (int | None):
        profile_name (None | str):
        days_per_year (float):
        days_first_year (float):
        valid_from (None | str):
    """

    profile_id: int | None
    profile_name: None | str
    days_per_year: float
    days_first_year: float
    valid_from: None | str

    def to_dict(self) -> dict[str, Any]:
        profile_id: int | None
        profile_id = self.profile_id

        profile_name: None | str
        profile_name = self.profile_name

        days_per_year = self.days_per_year

        days_first_year = self.days_first_year

        valid_from: None | str
        valid_from = self.valid_from

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "profileId": profile_id,
                "profileName": profile_name,
                "daysPerYear": days_per_year,
                "daysFirstYear": days_first_year,
                "validFrom": valid_from,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_profile_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        profile_id = _parse_profile_id(d.pop("profileId"))

        def _parse_profile_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_name = _parse_profile_name(d.pop("profileName"))

        days_per_year = d.pop("daysPerYear")

        days_first_year = d.pop("daysFirstYear")

        def _parse_valid_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        valid_from = _parse_valid_from(d.pop("validFrom"))

        get_person_by_person_no_response_200_time_recording_holiday = cls(
            profile_id=profile_id,
            profile_name=profile_name,
            days_per_year=days_per_year,
            days_first_year=days_first_year,
            valid_from=valid_from,
        )

        return get_person_by_person_no_response_200_time_recording_holiday
