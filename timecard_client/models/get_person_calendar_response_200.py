from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_person_calendar_response_200_absent_days_item import GetPersonCalendarResponse200AbsentDaysItem
    from ..models.get_person_calendar_response_200_public_holidays_item import (
        GetPersonCalendarResponse200PublicHolidaysItem,
    )
    from ..models.get_person_calendar_response_200_sick_days import GetPersonCalendarResponse200SickDays


T = TypeVar("T", bound="GetPersonCalendarResponse200")


@_attrs_define
class GetPersonCalendarResponse200:
    """
    Attributes:
        person_id (int):
        public_holidays (list[GetPersonCalendarResponse200PublicHolidaysItem]):
        absent_days (list[GetPersonCalendarResponse200AbsentDaysItem]):
        sick_days (GetPersonCalendarResponse200SickDays):
        inconsistent_days (list[str]):
        missing_booking_days (list[str]):
        core_time_violation_days (list[str]):
        permitted_time_violation_days (list[str]):
        correct_booking_days (list[str]):
        notification_days (list[str]):
    """

    person_id: int
    public_holidays: list[GetPersonCalendarResponse200PublicHolidaysItem]
    absent_days: list[GetPersonCalendarResponse200AbsentDaysItem]
    sick_days: GetPersonCalendarResponse200SickDays
    inconsistent_days: list[str]
    missing_booking_days: list[str]
    core_time_violation_days: list[str]
    permitted_time_violation_days: list[str]
    correct_booking_days: list[str]
    notification_days: list[str]

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        public_holidays = []
        for public_holidays_item_data in self.public_holidays:
            public_holidays_item = public_holidays_item_data.to_dict()
            public_holidays.append(public_holidays_item)

        absent_days = []
        for absent_days_item_data in self.absent_days:
            absent_days_item = absent_days_item_data.to_dict()
            absent_days.append(absent_days_item)

        sick_days = self.sick_days.to_dict()

        inconsistent_days = self.inconsistent_days

        missing_booking_days = self.missing_booking_days

        core_time_violation_days = self.core_time_violation_days

        permitted_time_violation_days = self.permitted_time_violation_days

        correct_booking_days = self.correct_booking_days

        notification_days = self.notification_days

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "publicHolidays": public_holidays,
                "absentDays": absent_days,
                "sickDays": sick_days,
                "inconsistentDays": inconsistent_days,
                "missingBookingDays": missing_booking_days,
                "coreTimeViolationDays": core_time_violation_days,
                "permittedTimeViolationDays": permitted_time_violation_days,
                "correctBookingDays": correct_booking_days,
                "notificationDays": notification_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_person_calendar_response_200_absent_days_item import (
            GetPersonCalendarResponse200AbsentDaysItem,  # noqa: PLC0415
        )
        from ..models.get_person_calendar_response_200_public_holidays_item import (
            GetPersonCalendarResponse200PublicHolidaysItem,  # noqa: PLC0415
        )
        from ..models.get_person_calendar_response_200_sick_days import (
            GetPersonCalendarResponse200SickDays,  # noqa: PLC0415
        )

        d = dict(src_dict)
        person_id = d.pop("personId")

        public_holidays = []
        _public_holidays = d.pop("publicHolidays")
        for public_holidays_item_data in _public_holidays:
            public_holidays_item = GetPersonCalendarResponse200PublicHolidaysItem.from_dict(public_holidays_item_data)

            public_holidays.append(public_holidays_item)

        absent_days = []
        _absent_days = d.pop("absentDays")
        for absent_days_item_data in _absent_days:
            absent_days_item = GetPersonCalendarResponse200AbsentDaysItem.from_dict(absent_days_item_data)

            absent_days.append(absent_days_item)

        sick_days = GetPersonCalendarResponse200SickDays.from_dict(d.pop("sickDays"))

        inconsistent_days = cast(list[str], d.pop("inconsistentDays"))

        missing_booking_days = cast(list[str], d.pop("missingBookingDays"))

        core_time_violation_days = cast(list[str], d.pop("coreTimeViolationDays"))

        permitted_time_violation_days = cast(list[str], d.pop("permittedTimeViolationDays"))

        correct_booking_days = cast(list[str], d.pop("correctBookingDays"))

        notification_days = cast(list[str], d.pop("notificationDays"))

        get_person_calendar_response_200 = cls(
            person_id=person_id,
            public_holidays=public_holidays,
            absent_days=absent_days,
            sick_days=sick_days,
            inconsistent_days=inconsistent_days,
            missing_booking_days=missing_booking_days,
            core_time_violation_days=core_time_violation_days,
            permitted_time_violation_days=permitted_time_violation_days,
            correct_booking_days=correct_booking_days,
            notification_days=notification_days,
        )

        return get_person_calendar_response_200
