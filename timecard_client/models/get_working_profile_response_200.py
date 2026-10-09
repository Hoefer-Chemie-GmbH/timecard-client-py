from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_working_profile_response_200_free_fields_item import GetWorkingProfileResponse200FreeFieldsItem
    from ..models.get_working_profile_response_200_working_days_item import GetWorkingProfileResponse200WorkingDaysItem


T = TypeVar("T", bound="GetWorkingProfileResponse200")


@_attrs_define
class GetWorkingProfileResponse200:
    """
    Attributes:
        id (int):
        name (str):
        type_ (str):
        is_active (bool):
        token (None | str):
        description (None | str):
        color (None | str):
        rounding (int):
        allowed_for_correction_requests (bool):
        is_crossover (bool):
        exclude_min (None | str):
        exclude_max (None | str):
        is_used (bool):
        target_time_week_seconds (int | None):
        disable_stop_time (bool | None):
        free_fields (list[GetWorkingProfileResponse200FreeFieldsItem]):
        working_days (list[GetWorkingProfileResponse200WorkingDaysItem]):
    """

    id: int
    name: str
    type_: str
    is_active: bool
    token: None | str
    description: None | str
    color: None | str
    rounding: int
    allowed_for_correction_requests: bool
    is_crossover: bool
    exclude_min: None | str
    exclude_max: None | str
    is_used: bool
    target_time_week_seconds: int | None
    disable_stop_time: bool | None
    free_fields: list[GetWorkingProfileResponse200FreeFieldsItem]
    working_days: list[GetWorkingProfileResponse200WorkingDaysItem]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        is_active = self.is_active

        token: None | str
        token = self.token

        description: None | str
        description = self.description

        color: None | str
        color = self.color

        rounding = self.rounding

        allowed_for_correction_requests = self.allowed_for_correction_requests

        is_crossover = self.is_crossover

        exclude_min: None | str
        exclude_min = self.exclude_min

        exclude_max: None | str
        exclude_max = self.exclude_max

        is_used = self.is_used

        target_time_week_seconds: int | None
        target_time_week_seconds = self.target_time_week_seconds

        disable_stop_time: bool | None
        disable_stop_time = self.disable_stop_time

        free_fields = []
        for free_fields_item_data in self.free_fields:
            free_fields_item = free_fields_item_data.to_dict()
            free_fields.append(free_fields_item)

        working_days = []
        for working_days_item_data in self.working_days:
            working_days_item = working_days_item_data.to_dict()
            working_days.append(working_days_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "isActive": is_active,
                "token": token,
                "description": description,
                "color": color,
                "rounding": rounding,
                "allowedForCorrectionRequests": allowed_for_correction_requests,
                "isCrossover": is_crossover,
                "excludeMin": exclude_min,
                "excludeMax": exclude_max,
                "isUsed": is_used,
                "targetTimeWeekSeconds": target_time_week_seconds,
                "disableStopTime": disable_stop_time,
                "freeFields": free_fields,
                "workingDays": working_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_working_profile_response_200_free_fields_item import (
            GetWorkingProfileResponse200FreeFieldsItem,  # noqa: PLC0415
        )
        from ..models.get_working_profile_response_200_working_days_item import (
            GetWorkingProfileResponse200WorkingDaysItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        is_active = d.pop("isActive")

        def _parse_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        token = _parse_token(d.pop("token"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        color = _parse_color(d.pop("color"))

        rounding = d.pop("rounding")

        allowed_for_correction_requests = d.pop("allowedForCorrectionRequests")

        is_crossover = d.pop("isCrossover")

        def _parse_exclude_min(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        exclude_min = _parse_exclude_min(d.pop("excludeMin"))

        def _parse_exclude_max(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        exclude_max = _parse_exclude_max(d.pop("excludeMax"))

        is_used = d.pop("isUsed")

        def _parse_target_time_week_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        target_time_week_seconds = _parse_target_time_week_seconds(d.pop("targetTimeWeekSeconds"))

        def _parse_disable_stop_time(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        disable_stop_time = _parse_disable_stop_time(d.pop("disableStopTime"))

        free_fields = []
        _free_fields = d.pop("freeFields")
        for free_fields_item_data in _free_fields:
            free_fields_item = GetWorkingProfileResponse200FreeFieldsItem.from_dict(free_fields_item_data)

            free_fields.append(free_fields_item)

        working_days = []
        _working_days = d.pop("workingDays")
        for working_days_item_data in _working_days:
            working_days_item = GetWorkingProfileResponse200WorkingDaysItem.from_dict(working_days_item_data)

            working_days.append(working_days_item)

        get_working_profile_response_200 = cls(
            id=id,
            name=name,
            type_=type_,
            is_active=is_active,
            token=token,
            description=description,
            color=color,
            rounding=rounding,
            allowed_for_correction_requests=allowed_for_correction_requests,
            is_crossover=is_crossover,
            exclude_min=exclude_min,
            exclude_max=exclude_max,
            is_used=is_used,
            target_time_week_seconds=target_time_week_seconds,
            disable_stop_time=disable_stop_time,
            free_fields=free_fields,
            working_days=working_days,
        )

        return get_working_profile_response_200
