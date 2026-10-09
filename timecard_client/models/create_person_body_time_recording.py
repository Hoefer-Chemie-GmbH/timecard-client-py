from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePersonBodyTimeRecording")


@_attrs_define
class CreatePersonBodyTimeRecording:
    """
    Attributes:
        valid_from (str | Unset): valid-from date for changed profiles and accounts; defaults to today
        working_profile_id (int | Unset):
        calculation_template_ids (list[int] | Unset):
        holiday_profile_id (int | Unset):
        holiday_days_per_year (float | Unset):
        first_day_of_month (int | Unset):
    """

    valid_from: str | Unset = UNSET
    working_profile_id: int | Unset = UNSET
    calculation_template_ids: list[int] | Unset = UNSET
    holiday_profile_id: int | Unset = UNSET
    holiday_days_per_year: float | Unset = UNSET
    first_day_of_month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid_from = self.valid_from

        working_profile_id = self.working_profile_id

        calculation_template_ids: list[int] | Unset = UNSET
        if not isinstance(self.calculation_template_ids, Unset):
            calculation_template_ids = self.calculation_template_ids

        holiday_profile_id = self.holiday_profile_id

        holiday_days_per_year = self.holiday_days_per_year

        first_day_of_month = self.first_day_of_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if working_profile_id is not UNSET:
            field_dict["workingProfileId"] = working_profile_id
        if calculation_template_ids is not UNSET:
            field_dict["calculationTemplateIds"] = calculation_template_ids
        if holiday_profile_id is not UNSET:
            field_dict["holidayProfileId"] = holiday_profile_id
        if holiday_days_per_year is not UNSET:
            field_dict["holidayDaysPerYear"] = holiday_days_per_year
        if first_day_of_month is not UNSET:
            field_dict["firstDayOfMonth"] = first_day_of_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid_from = d.pop("validFrom", UNSET)

        working_profile_id = d.pop("workingProfileId", UNSET)

        calculation_template_ids = cast(list[int], d.pop("calculationTemplateIds", UNSET))

        holiday_profile_id = d.pop("holidayProfileId", UNSET)

        holiday_days_per_year = d.pop("holidayDaysPerYear", UNSET)

        first_day_of_month = d.pop("firstDayOfMonth", UNSET)

        create_person_body_time_recording = cls(
            valid_from=valid_from,
            working_profile_id=working_profile_id,
            calculation_template_ids=calculation_template_ids,
            holiday_profile_id=holiday_profile_id,
            holiday_days_per_year=holiday_days_per_year,
            first_day_of_month=first_day_of_month,
        )

        create_person_body_time_recording.additional_properties = d
        return create_person_body_time_recording

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
