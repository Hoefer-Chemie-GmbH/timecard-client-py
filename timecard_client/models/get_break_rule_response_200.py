from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetBreakRuleResponse200")


@_attrs_define
class GetBreakRuleResponse200:
    """
    Attributes:
        id (int):
        name (str):
        type_ (str):
        description (None | str):
        duration_minutes (int | None):
        first_time (None | str):
        second_time (None | str):
        create_at_begin (bool):
        with_breathing_time (bool):
        complete_present (bool | None):
        is_used (bool):
        is_active (bool):
    """

    id: int
    name: str
    type_: str
    description: None | str
    duration_minutes: int | None
    first_time: None | str
    second_time: None | str
    create_at_begin: bool
    with_breathing_time: bool
    complete_present: bool | None
    is_used: bool
    is_active: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        description: None | str
        description = self.description

        duration_minutes: int | None
        duration_minutes = self.duration_minutes

        first_time: None | str
        first_time = self.first_time

        second_time: None | str
        second_time = self.second_time

        create_at_begin = self.create_at_begin

        with_breathing_time = self.with_breathing_time

        complete_present: bool | None
        complete_present = self.complete_present

        is_used = self.is_used

        is_active = self.is_active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "description": description,
                "durationMinutes": duration_minutes,
                "firstTime": first_time,
                "secondTime": second_time,
                "createAtBegin": create_at_begin,
                "withBreathingTime": with_breathing_time,
                "completePresent": complete_present,
                "isUsed": is_used,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_duration_minutes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_minutes = _parse_duration_minutes(d.pop("durationMinutes"))

        def _parse_first_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_time = _parse_first_time(d.pop("firstTime"))

        def _parse_second_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        second_time = _parse_second_time(d.pop("secondTime"))

        create_at_begin = d.pop("createAtBegin")

        with_breathing_time = d.pop("withBreathingTime")

        def _parse_complete_present(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        complete_present = _parse_complete_present(d.pop("completePresent"))

        is_used = d.pop("isUsed")

        is_active = d.pop("isActive")

        get_break_rule_response_200 = cls(
            id=id,
            name=name,
            type_=type_,
            description=description,
            duration_minutes=duration_minutes,
            first_time=first_time,
            second_time=second_time,
            create_at_begin=create_at_begin,
            with_breathing_time=with_breathing_time,
            complete_present=complete_present,
            is_used=is_used,
            is_active=is_active,
        )

        return get_break_rule_response_200
