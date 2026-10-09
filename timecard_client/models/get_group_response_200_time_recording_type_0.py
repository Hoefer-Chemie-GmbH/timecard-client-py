from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetGroupResponse200TimeRecordingType0")


@_attrs_define
class GetGroupResponse200TimeRecordingType0:
    """
    Attributes:
        working_profile_id (int | None):
        working_profile_name (None | str):
        calculation_template_ids (list[int]):
        holiday_profile_id (int | None):
        holiday_profile_name (None | str):
    """

    working_profile_id: int | None
    working_profile_name: None | str
    calculation_template_ids: list[int]
    holiday_profile_id: int | None
    holiday_profile_name: None | str

    def to_dict(self) -> dict[str, Any]:
        working_profile_id: int | None
        working_profile_id = self.working_profile_id

        working_profile_name: None | str
        working_profile_name = self.working_profile_name

        calculation_template_ids = self.calculation_template_ids

        holiday_profile_id: int | None
        holiday_profile_id = self.holiday_profile_id

        holiday_profile_name: None | str
        holiday_profile_name = self.holiday_profile_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workingProfileId": working_profile_id,
                "workingProfileName": working_profile_name,
                "calculationTemplateIds": calculation_template_ids,
                "holidayProfileId": holiday_profile_id,
                "holidayProfileName": holiday_profile_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_working_profile_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        working_profile_id = _parse_working_profile_id(d.pop("workingProfileId"))

        def _parse_working_profile_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        working_profile_name = _parse_working_profile_name(d.pop("workingProfileName"))

        calculation_template_ids = cast(list[int], d.pop("calculationTemplateIds"))

        def _parse_holiday_profile_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        holiday_profile_id = _parse_holiday_profile_id(d.pop("holidayProfileId"))

        def _parse_holiday_profile_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        holiday_profile_name = _parse_holiday_profile_name(d.pop("holidayProfileName"))

        get_group_response_200_time_recording_type_0 = cls(
            working_profile_id=working_profile_id,
            working_profile_name=working_profile_name,
            calculation_template_ids=calculation_template_ids,
            holiday_profile_id=holiday_profile_id,
            holiday_profile_name=holiday_profile_name,
        )

        return get_group_response_200_time_recording_type_0
