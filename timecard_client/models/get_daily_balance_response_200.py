from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_daily_balance_response_200_absences_item import GetDailyBalanceResponse200AbsencesItem
    from ..models.get_daily_balance_response_200_booking_time_range import GetDailyBalanceResponse200BookingTimeRange
    from ..models.get_daily_balance_response_200_calculations_item import GetDailyBalanceResponse200CalculationsItem
    from ..models.get_daily_balance_response_200_carry_overs_item import GetDailyBalanceResponse200CarryOversItem
    from ..models.get_daily_balance_response_200_evaluation_changed import GetDailyBalanceResponse200EvaluationChanged
    from ..models.get_daily_balance_response_200_projects_item import GetDailyBalanceResponse200ProjectsItem
    from ..models.get_daily_balance_response_200_working_profile import GetDailyBalanceResponse200WorkingProfile


T = TypeVar("T", bound="GetDailyBalanceResponse200")


@_attrs_define
class GetDailyBalanceResponse200:
    """
    Attributes:
        person_id (int):
        date (str):
        available (bool):
        is_today (bool):
        is_before_recording_begin (bool):
        is_month_closed (bool):
        booking_time_range (GetDailyBalanceResponse200BookingTimeRange):
        first_clock_in (None | str):
        last_clock_out (None | str):
        target_time_seconds (int | None): null when timeCard reports no value, e.g. on days without a working time or an
            optional profile without bookings
        working_time_seconds (int | None):
        presence_time_seconds (int | None):
        break_time_seconds (int | None):
        interruption_seconds (int | None):
        inconsistent (bool):
        inconsistent_reason (None | str):
        core_time_violation (bool):
        missing_bookings (bool):
        permitted_time_violation (bool):
        auto_breaks_ignored (bool):
        evaluation_changed (GetDailyBalanceResponse200EvaluationChanged):
        holiday_ban (bool):
        has_open_correction_request (bool):
        working_profile (GetDailyBalanceResponse200WorkingProfile):
        notifications (list[str]):
        absences (list[GetDailyBalanceResponse200AbsencesItem]):
        projects (list[GetDailyBalanceResponse200ProjectsItem]):
        carry_overs (list[GetDailyBalanceResponse200CarryOversItem]):
        calculations (list[GetDailyBalanceResponse200CalculationsItem]):
    """

    person_id: int
    date: str
    available: bool
    is_today: bool
    is_before_recording_begin: bool
    is_month_closed: bool
    booking_time_range: GetDailyBalanceResponse200BookingTimeRange
    first_clock_in: None | str
    last_clock_out: None | str
    target_time_seconds: int | None
    working_time_seconds: int | None
    presence_time_seconds: int | None
    break_time_seconds: int | None
    interruption_seconds: int | None
    inconsistent: bool
    inconsistent_reason: None | str
    core_time_violation: bool
    missing_bookings: bool
    permitted_time_violation: bool
    auto_breaks_ignored: bool
    evaluation_changed: GetDailyBalanceResponse200EvaluationChanged
    holiday_ban: bool
    has_open_correction_request: bool
    working_profile: GetDailyBalanceResponse200WorkingProfile
    notifications: list[str]
    absences: list[GetDailyBalanceResponse200AbsencesItem]
    projects: list[GetDailyBalanceResponse200ProjectsItem]
    carry_overs: list[GetDailyBalanceResponse200CarryOversItem]
    calculations: list[GetDailyBalanceResponse200CalculationsItem]

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        date = self.date

        available = self.available

        is_today = self.is_today

        is_before_recording_begin = self.is_before_recording_begin

        is_month_closed = self.is_month_closed

        booking_time_range = self.booking_time_range.to_dict()

        first_clock_in: None | str
        first_clock_in = self.first_clock_in

        last_clock_out: None | str
        last_clock_out = self.last_clock_out

        target_time_seconds: int | None
        target_time_seconds = self.target_time_seconds

        working_time_seconds: int | None
        working_time_seconds = self.working_time_seconds

        presence_time_seconds: int | None
        presence_time_seconds = self.presence_time_seconds

        break_time_seconds: int | None
        break_time_seconds = self.break_time_seconds

        interruption_seconds: int | None
        interruption_seconds = self.interruption_seconds

        inconsistent = self.inconsistent

        inconsistent_reason: None | str
        inconsistent_reason = self.inconsistent_reason

        core_time_violation = self.core_time_violation

        missing_bookings = self.missing_bookings

        permitted_time_violation = self.permitted_time_violation

        auto_breaks_ignored = self.auto_breaks_ignored

        evaluation_changed = self.evaluation_changed.to_dict()

        holiday_ban = self.holiday_ban

        has_open_correction_request = self.has_open_correction_request

        working_profile = self.working_profile.to_dict()

        notifications = self.notifications

        absences = []
        for absences_item_data in self.absences:
            absences_item = absences_item_data.to_dict()
            absences.append(absences_item)

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        carry_overs = []
        for carry_overs_item_data in self.carry_overs:
            carry_overs_item = carry_overs_item_data.to_dict()
            carry_overs.append(carry_overs_item)

        calculations = []
        for calculations_item_data in self.calculations:
            calculations_item = calculations_item_data.to_dict()
            calculations.append(calculations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "date": date,
                "available": available,
                "isToday": is_today,
                "isBeforeRecordingBegin": is_before_recording_begin,
                "isMonthClosed": is_month_closed,
                "bookingTimeRange": booking_time_range,
                "firstClockIn": first_clock_in,
                "lastClockOut": last_clock_out,
                "targetTimeSeconds": target_time_seconds,
                "workingTimeSeconds": working_time_seconds,
                "presenceTimeSeconds": presence_time_seconds,
                "breakTimeSeconds": break_time_seconds,
                "interruptionSeconds": interruption_seconds,
                "inconsistent": inconsistent,
                "inconsistentReason": inconsistent_reason,
                "coreTimeViolation": core_time_violation,
                "missingBookings": missing_bookings,
                "permittedTimeViolation": permitted_time_violation,
                "autoBreaksIgnored": auto_breaks_ignored,
                "evaluationChanged": evaluation_changed,
                "holidayBan": holiday_ban,
                "hasOpenCorrectionRequest": has_open_correction_request,
                "workingProfile": working_profile,
                "notifications": notifications,
                "absences": absences,
                "projects": projects,
                "carryOvers": carry_overs,
                "calculations": calculations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_daily_balance_response_200_absences_item import (
            GetDailyBalanceResponse200AbsencesItem,  # noqa: PLC0415
        )
        from ..models.get_daily_balance_response_200_booking_time_range import (
            GetDailyBalanceResponse200BookingTimeRange,  # noqa: PLC0415
        )
        from ..models.get_daily_balance_response_200_calculations_item import (
            GetDailyBalanceResponse200CalculationsItem,  # noqa: PLC0415
        )
        from ..models.get_daily_balance_response_200_carry_overs_item import (
            GetDailyBalanceResponse200CarryOversItem,  # noqa: PLC0415
        )
        from ..models.get_daily_balance_response_200_evaluation_changed import (
            GetDailyBalanceResponse200EvaluationChanged,  # noqa: PLC0415
        )
        from ..models.get_daily_balance_response_200_projects_item import (
            GetDailyBalanceResponse200ProjectsItem,  # noqa: PLC0415
        )
        from ..models.get_daily_balance_response_200_working_profile import (
            GetDailyBalanceResponse200WorkingProfile,  # noqa: PLC0415
        )

        d = dict(src_dict)
        person_id = d.pop("personId")

        date = d.pop("date")

        available = d.pop("available")

        is_today = d.pop("isToday")

        is_before_recording_begin = d.pop("isBeforeRecordingBegin")

        is_month_closed = d.pop("isMonthClosed")

        booking_time_range = GetDailyBalanceResponse200BookingTimeRange.from_dict(d.pop("bookingTimeRange"))

        def _parse_first_clock_in(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_clock_in = _parse_first_clock_in(d.pop("firstClockIn"))

        def _parse_last_clock_out(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_clock_out = _parse_last_clock_out(d.pop("lastClockOut"))

        def _parse_target_time_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        target_time_seconds = _parse_target_time_seconds(d.pop("targetTimeSeconds"))

        def _parse_working_time_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        working_time_seconds = _parse_working_time_seconds(d.pop("workingTimeSeconds"))

        def _parse_presence_time_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        presence_time_seconds = _parse_presence_time_seconds(d.pop("presenceTimeSeconds"))

        def _parse_break_time_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        break_time_seconds = _parse_break_time_seconds(d.pop("breakTimeSeconds"))

        def _parse_interruption_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        interruption_seconds = _parse_interruption_seconds(d.pop("interruptionSeconds"))

        inconsistent = d.pop("inconsistent")

        def _parse_inconsistent_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        inconsistent_reason = _parse_inconsistent_reason(d.pop("inconsistentReason"))

        core_time_violation = d.pop("coreTimeViolation")

        missing_bookings = d.pop("missingBookings")

        permitted_time_violation = d.pop("permittedTimeViolation")

        auto_breaks_ignored = d.pop("autoBreaksIgnored")

        evaluation_changed = GetDailyBalanceResponse200EvaluationChanged.from_dict(d.pop("evaluationChanged"))

        holiday_ban = d.pop("holidayBan")

        has_open_correction_request = d.pop("hasOpenCorrectionRequest")

        working_profile = GetDailyBalanceResponse200WorkingProfile.from_dict(d.pop("workingProfile"))

        notifications = cast(list[str], d.pop("notifications"))

        absences = []
        _absences = d.pop("absences")
        for absences_item_data in _absences:
            absences_item = GetDailyBalanceResponse200AbsencesItem.from_dict(absences_item_data)

            absences.append(absences_item)

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = GetDailyBalanceResponse200ProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        carry_overs = []
        _carry_overs = d.pop("carryOvers")
        for carry_overs_item_data in _carry_overs:
            carry_overs_item = GetDailyBalanceResponse200CarryOversItem.from_dict(carry_overs_item_data)

            carry_overs.append(carry_overs_item)

        calculations = []
        _calculations = d.pop("calculations")
        for calculations_item_data in _calculations:
            calculations_item = GetDailyBalanceResponse200CalculationsItem.from_dict(calculations_item_data)

            calculations.append(calculations_item)

        get_daily_balance_response_200 = cls(
            person_id=person_id,
            date=date,
            available=available,
            is_today=is_today,
            is_before_recording_begin=is_before_recording_begin,
            is_month_closed=is_month_closed,
            booking_time_range=booking_time_range,
            first_clock_in=first_clock_in,
            last_clock_out=last_clock_out,
            target_time_seconds=target_time_seconds,
            working_time_seconds=working_time_seconds,
            presence_time_seconds=presence_time_seconds,
            break_time_seconds=break_time_seconds,
            interruption_seconds=interruption_seconds,
            inconsistent=inconsistent,
            inconsistent_reason=inconsistent_reason,
            core_time_violation=core_time_violation,
            missing_bookings=missing_bookings,
            permitted_time_violation=permitted_time_violation,
            auto_breaks_ignored=auto_breaks_ignored,
            evaluation_changed=evaluation_changed,
            holiday_ban=holiday_ban,
            has_open_correction_request=has_open_correction_request,
            working_profile=working_profile,
            notifications=notifications,
            absences=absences,
            projects=projects,
            carry_overs=carry_overs,
            calculations=calculations,
        )

        return get_daily_balance_response_200
