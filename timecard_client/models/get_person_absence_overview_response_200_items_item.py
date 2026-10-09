from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_person_absence_overview_response_200_items_item_days_item import (
        GetPersonAbsenceOverviewResponse200ItemsItemDaysItem,
    )


T = TypeVar("T", bound="GetPersonAbsenceOverviewResponse200ItemsItem")


@_attrs_define
class GetPersonAbsenceOverviewResponse200ItemsItem:
    """
    Attributes:
        person_id (int | None):
        person_no (None | str):
        first_name (None | str):
        last_name (None | str):
        department (None | str):
        working_profile (None | str):
        month (int | None):
        is_total (bool):
        holidays (float | None):
        sick_days (float | None):
        working_days (float | None):
        absent_days (float | None):
        office_days (float | None):
        home_office_days (float | None):
        days (list[GetPersonAbsenceOverviewResponse200ItemsItemDaysItem]):
    """

    person_id: int | None
    person_no: None | str
    first_name: None | str
    last_name: None | str
    department: None | str
    working_profile: None | str
    month: int | None
    is_total: bool
    holidays: float | None
    sick_days: float | None
    working_days: float | None
    absent_days: float | None
    office_days: float | None
    home_office_days: float | None
    days: list[GetPersonAbsenceOverviewResponse200ItemsItemDaysItem]

    def to_dict(self) -> dict[str, Any]:
        person_id: int | None
        person_id = self.person_id

        person_no: None | str
        person_no = self.person_no

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        department: None | str
        department = self.department

        working_profile: None | str
        working_profile = self.working_profile

        month: int | None
        month = self.month

        is_total = self.is_total

        holidays: float | None
        holidays = self.holidays

        sick_days: float | None
        sick_days = self.sick_days

        working_days: float | None
        working_days = self.working_days

        absent_days: float | None
        absent_days = self.absent_days

        office_days: float | None
        office_days = self.office_days

        home_office_days: float | None
        home_office_days = self.home_office_days

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "personNo": person_no,
                "firstName": first_name,
                "lastName": last_name,
                "department": department,
                "workingProfile": working_profile,
                "month": month,
                "isTotal": is_total,
                "holidays": holidays,
                "sickDays": sick_days,
                "workingDays": working_days,
                "absentDays": absent_days,
                "officeDays": office_days,
                "homeOfficeDays": home_office_days,
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_person_absence_overview_response_200_items_item_days_item import (
            GetPersonAbsenceOverviewResponse200ItemsItemDaysItem,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_person_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        person_id = _parse_person_id(d.pop("personId"))

        def _parse_person_no(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        person_no = _parse_person_no(d.pop("personNo"))

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("firstName"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("lastName"))

        def _parse_department(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        department = _parse_department(d.pop("department"))

        def _parse_working_profile(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        working_profile = _parse_working_profile(d.pop("workingProfile"))

        def _parse_month(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        month = _parse_month(d.pop("month"))

        is_total = d.pop("isTotal")

        def _parse_holidays(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        holidays = _parse_holidays(d.pop("holidays"))

        def _parse_sick_days(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        sick_days = _parse_sick_days(d.pop("sickDays"))

        def _parse_working_days(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        working_days = _parse_working_days(d.pop("workingDays"))

        def _parse_absent_days(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        absent_days = _parse_absent_days(d.pop("absentDays"))

        def _parse_office_days(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        office_days = _parse_office_days(d.pop("officeDays"))

        def _parse_home_office_days(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        home_office_days = _parse_home_office_days(d.pop("homeOfficeDays"))

        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = GetPersonAbsenceOverviewResponse200ItemsItemDaysItem.from_dict(days_item_data)

            days.append(days_item)

        get_person_absence_overview_response_200_items_item = cls(
            person_id=person_id,
            person_no=person_no,
            first_name=first_name,
            last_name=last_name,
            department=department,
            working_profile=working_profile,
            month=month,
            is_total=is_total,
            holidays=holidays,
            sick_days=sick_days,
            working_days=working_days,
            absent_days=absent_days,
            office_days=office_days,
            home_office_days=home_office_days,
            days=days,
        )

        return get_person_absence_overview_response_200_items_item
