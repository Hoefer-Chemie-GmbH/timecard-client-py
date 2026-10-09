from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_absence_booking_body_weekdays_item import CreateAbsenceBookingBodyWeekdaysItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAbsenceBookingBody")


@_attrs_define
class CreateAbsenceBookingBody:
    """
    Attributes:
        person_ids (list[int]):
        absence_type_id (int):
        from_ (str):
        to (str):
        weekdays (list[CreateAbsenceBookingBodyWeekdaysItem] | Unset):
        include_free_days (bool | Unset): also book on days off according to the working time profile Default: False.
        half_day (bool | Unset):  Default: False.
        percent (int | Unset): share of the day in percent; mutually exclusive with halfDay
        start_time (str | Unset):
        comment (str | Unset):  Default: ''.
    """

    person_ids: list[int]
    absence_type_id: int
    from_: str
    to: str
    weekdays: list[CreateAbsenceBookingBodyWeekdaysItem] | Unset = UNSET
    include_free_days: bool | Unset = False
    half_day: bool | Unset = False
    percent: int | Unset = UNSET
    start_time: str | Unset = UNSET
    comment: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_ids = self.person_ids

        absence_type_id = self.absence_type_id

        from_ = self.from_

        to = self.to

        weekdays: list[str] | Unset = UNSET
        if not isinstance(self.weekdays, Unset):
            weekdays = []
            for weekdays_item_data in self.weekdays:
                weekdays_item = weekdays_item_data.value
                weekdays.append(weekdays_item)

        include_free_days = self.include_free_days

        half_day = self.half_day

        percent = self.percent

        start_time = self.start_time

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "personIds": person_ids,
                "absenceTypeId": absence_type_id,
                "from": from_,
                "to": to,
            }
        )
        if weekdays is not UNSET:
            field_dict["weekdays"] = weekdays
        if include_free_days is not UNSET:
            field_dict["includeFreeDays"] = include_free_days
        if half_day is not UNSET:
            field_dict["halfDay"] = half_day
        if percent is not UNSET:
            field_dict["percent"] = percent
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_ids = cast(list[int], d.pop("personIds"))

        absence_type_id = d.pop("absenceTypeId")

        from_ = d.pop("from")

        to = d.pop("to")

        _weekdays = d.pop("weekdays", UNSET)
        weekdays: list[CreateAbsenceBookingBodyWeekdaysItem] | Unset = UNSET
        if _weekdays is not UNSET:
            weekdays = []
            for weekdays_item_data in _weekdays:
                weekdays_item = CreateAbsenceBookingBodyWeekdaysItem(weekdays_item_data)

                weekdays.append(weekdays_item)

        include_free_days = d.pop("includeFreeDays", UNSET)

        half_day = d.pop("halfDay", UNSET)

        percent = d.pop("percent", UNSET)

        start_time = d.pop("startTime", UNSET)

        comment = d.pop("comment", UNSET)

        create_absence_booking_body = cls(
            person_ids=person_ids,
            absence_type_id=absence_type_id,
            from_=from_,
            to=to,
            weekdays=weekdays,
            include_free_days=include_free_days,
            half_day=half_day,
            percent=percent,
            start_time=start_time,
            comment=comment,
        )

        create_absence_booking_body.additional_properties = d
        return create_absence_booking_body

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
