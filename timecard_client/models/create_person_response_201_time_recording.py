from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_person_response_201_time_recording_calculation_templates import (
        CreatePersonResponse201TimeRecordingCalculationTemplates,
    )
    from ..models.create_person_response_201_time_recording_holiday import CreatePersonResponse201TimeRecordingHoliday
    from ..models.create_person_response_201_time_recording_supervisors_item import (
        CreatePersonResponse201TimeRecordingSupervisorsItem,
    )
    from ..models.create_person_response_201_time_recording_working_profile import (
        CreatePersonResponse201TimeRecordingWorkingProfile,
    )


T = TypeVar("T", bound="CreatePersonResponse201TimeRecording")


@_attrs_define
class CreatePersonResponse201TimeRecording:
    """
    Attributes:
        working_profile (CreatePersonResponse201TimeRecordingWorkingProfile):
        calculation_templates (CreatePersonResponse201TimeRecordingCalculationTemplates):
        holiday (CreatePersonResponse201TimeRecordingHoliday):
        first_day_of_month (int):
        has_open_requests (bool | None):
        supervisors (list[CreatePersonResponse201TimeRecordingSupervisorsItem]):
    """

    working_profile: CreatePersonResponse201TimeRecordingWorkingProfile
    calculation_templates: CreatePersonResponse201TimeRecordingCalculationTemplates
    holiday: CreatePersonResponse201TimeRecordingHoliday
    first_day_of_month: int
    has_open_requests: bool | None
    supervisors: list[CreatePersonResponse201TimeRecordingSupervisorsItem]

    def to_dict(self) -> dict[str, Any]:
        working_profile = self.working_profile.to_dict()

        calculation_templates = self.calculation_templates.to_dict()

        holiday = self.holiday.to_dict()

        first_day_of_month = self.first_day_of_month

        has_open_requests: bool | None
        has_open_requests = self.has_open_requests

        supervisors = []
        for supervisors_item_data in self.supervisors:
            supervisors_item = supervisors_item_data.to_dict()
            supervisors.append(supervisors_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workingProfile": working_profile,
                "calculationTemplates": calculation_templates,
                "holiday": holiday,
                "firstDayOfMonth": first_day_of_month,
                "hasOpenRequests": has_open_requests,
                "supervisors": supervisors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_person_response_201_time_recording_calculation_templates import (
            CreatePersonResponse201TimeRecordingCalculationTemplates,  # noqa: PLC0415
        )
        from ..models.create_person_response_201_time_recording_holiday import (
            CreatePersonResponse201TimeRecordingHoliday,  # noqa: PLC0415
        )
        from ..models.create_person_response_201_time_recording_supervisors_item import (
            CreatePersonResponse201TimeRecordingSupervisorsItem,  # noqa: PLC0415
        )
        from ..models.create_person_response_201_time_recording_working_profile import (
            CreatePersonResponse201TimeRecordingWorkingProfile,  # noqa: PLC0415
        )

        d = dict(src_dict)
        working_profile = CreatePersonResponse201TimeRecordingWorkingProfile.from_dict(d.pop("workingProfile"))

        calculation_templates = CreatePersonResponse201TimeRecordingCalculationTemplates.from_dict(
            d.pop("calculationTemplates")
        )

        holiday = CreatePersonResponse201TimeRecordingHoliday.from_dict(d.pop("holiday"))

        first_day_of_month = d.pop("firstDayOfMonth")

        def _parse_has_open_requests(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        has_open_requests = _parse_has_open_requests(d.pop("hasOpenRequests"))

        supervisors = []
        _supervisors = d.pop("supervisors")
        for supervisors_item_data in _supervisors:
            supervisors_item = CreatePersonResponse201TimeRecordingSupervisorsItem.from_dict(supervisors_item_data)

            supervisors.append(supervisors_item)

        create_person_response_201_time_recording = cls(
            working_profile=working_profile,
            calculation_templates=calculation_templates,
            holiday=holiday,
            first_day_of_month=first_day_of_month,
            has_open_requests=has_open_requests,
            supervisors=supervisors,
        )

        return create_person_response_201_time_recording
