from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_absence_type_response_200_free_fields_item import GetAbsenceTypeResponse200FreeFieldsItem


T = TypeVar("T", bound="GetAbsenceTypeResponse200")


@_attrs_define
class GetAbsenceTypeResponse200:
    """
    Attributes:
        id (int):
        order_no (int):
        name (str):
        token (None | str):
        is_holiday (bool):
        color (None | str):
        has_replace_time (bool):
        weighting_type (int | None):
        alt_name (None | str):
        alt_color (None | str):
        description (None | str):
        is_working_time (bool):
        only_core_time (bool):
        allowed_for_requests (bool):
        allowed_for_bookings_with_reason (bool):
        allowed_for_manual_full_day (bool):
        allowed_for_self (bool | None):
        use_pause_rule (bool):
        replace_time_state (str):
        replace_time (None | str):
        analysis_rounding (bool):
        analysis_project (bool):
        rounding_last_go (bool):
        is_used (bool):
        is_system (bool):
        restricted_department_ids (list[int]):
        restricted_group_ids (list[int]):
        browser_allowed (bool):
        terminal_allowed (bool):
        app_allowed (bool):
        presence_allowed (bool):
        also_illness (bool | None):
        reduce_illness (bool | None):
        free_fields (list[GetAbsenceTypeResponse200FreeFieldsItem]):
    """

    id: int
    order_no: int
    name: str
    token: None | str
    is_holiday: bool
    color: None | str
    has_replace_time: bool
    weighting_type: int | None
    alt_name: None | str
    alt_color: None | str
    description: None | str
    is_working_time: bool
    only_core_time: bool
    allowed_for_requests: bool
    allowed_for_bookings_with_reason: bool
    allowed_for_manual_full_day: bool
    allowed_for_self: bool | None
    use_pause_rule: bool
    replace_time_state: str
    replace_time: None | str
    analysis_rounding: bool
    analysis_project: bool
    rounding_last_go: bool
    is_used: bool
    is_system: bool
    restricted_department_ids: list[int]
    restricted_group_ids: list[int]
    browser_allowed: bool
    terminal_allowed: bool
    app_allowed: bool
    presence_allowed: bool
    also_illness: bool | None
    reduce_illness: bool | None
    free_fields: list[GetAbsenceTypeResponse200FreeFieldsItem]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        order_no = self.order_no

        name = self.name

        token: None | str
        token = self.token

        is_holiday = self.is_holiday

        color: None | str
        color = self.color

        has_replace_time = self.has_replace_time

        weighting_type: int | None
        weighting_type = self.weighting_type

        alt_name: None | str
        alt_name = self.alt_name

        alt_color: None | str
        alt_color = self.alt_color

        description: None | str
        description = self.description

        is_working_time = self.is_working_time

        only_core_time = self.only_core_time

        allowed_for_requests = self.allowed_for_requests

        allowed_for_bookings_with_reason = self.allowed_for_bookings_with_reason

        allowed_for_manual_full_day = self.allowed_for_manual_full_day

        allowed_for_self: bool | None
        allowed_for_self = self.allowed_for_self

        use_pause_rule = self.use_pause_rule

        replace_time_state = self.replace_time_state

        replace_time: None | str
        replace_time = self.replace_time

        analysis_rounding = self.analysis_rounding

        analysis_project = self.analysis_project

        rounding_last_go = self.rounding_last_go

        is_used = self.is_used

        is_system = self.is_system

        restricted_department_ids = self.restricted_department_ids

        restricted_group_ids = self.restricted_group_ids

        browser_allowed = self.browser_allowed

        terminal_allowed = self.terminal_allowed

        app_allowed = self.app_allowed

        presence_allowed = self.presence_allowed

        also_illness: bool | None
        also_illness = self.also_illness

        reduce_illness: bool | None
        reduce_illness = self.reduce_illness

        free_fields = []
        for free_fields_item_data in self.free_fields:
            free_fields_item = free_fields_item_data.to_dict()
            free_fields.append(free_fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "orderNo": order_no,
                "name": name,
                "token": token,
                "isHoliday": is_holiday,
                "color": color,
                "hasReplaceTime": has_replace_time,
                "weightingType": weighting_type,
                "altName": alt_name,
                "altColor": alt_color,
                "description": description,
                "isWorkingTime": is_working_time,
                "onlyCoreTime": only_core_time,
                "allowedForRequests": allowed_for_requests,
                "allowedForBookingsWithReason": allowed_for_bookings_with_reason,
                "allowedForManualFullDay": allowed_for_manual_full_day,
                "allowedForSelf": allowed_for_self,
                "usePauseRule": use_pause_rule,
                "replaceTimeState": replace_time_state,
                "replaceTime": replace_time,
                "analysisRounding": analysis_rounding,
                "analysisProject": analysis_project,
                "roundingLastGo": rounding_last_go,
                "isUsed": is_used,
                "isSystem": is_system,
                "restrictedDepartmentIds": restricted_department_ids,
                "restrictedGroupIds": restricted_group_ids,
                "browserAllowed": browser_allowed,
                "terminalAllowed": terminal_allowed,
                "appAllowed": app_allowed,
                "presenceAllowed": presence_allowed,
                "alsoIllness": also_illness,
                "reduceIllness": reduce_illness,
                "freeFields": free_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_absence_type_response_200_free_fields_item import (
            GetAbsenceTypeResponse200FreeFieldsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        order_no = d.pop("orderNo")

        name = d.pop("name")

        def _parse_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        token = _parse_token(d.pop("token"))

        is_holiday = d.pop("isHoliday")

        def _parse_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        color = _parse_color(d.pop("color"))

        has_replace_time = d.pop("hasReplaceTime")

        def _parse_weighting_type(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weighting_type = _parse_weighting_type(d.pop("weightingType"))

        def _parse_alt_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        alt_name = _parse_alt_name(d.pop("altName"))

        def _parse_alt_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        alt_color = _parse_alt_color(d.pop("altColor"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        is_working_time = d.pop("isWorkingTime")

        only_core_time = d.pop("onlyCoreTime")

        allowed_for_requests = d.pop("allowedForRequests")

        allowed_for_bookings_with_reason = d.pop("allowedForBookingsWithReason")

        allowed_for_manual_full_day = d.pop("allowedForManualFullDay")

        def _parse_allowed_for_self(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        allowed_for_self = _parse_allowed_for_self(d.pop("allowedForSelf"))

        use_pause_rule = d.pop("usePauseRule")

        replace_time_state = d.pop("replaceTimeState")

        def _parse_replace_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        replace_time = _parse_replace_time(d.pop("replaceTime"))

        analysis_rounding = d.pop("analysisRounding")

        analysis_project = d.pop("analysisProject")

        rounding_last_go = d.pop("roundingLastGo")

        is_used = d.pop("isUsed")

        is_system = d.pop("isSystem")

        restricted_department_ids = cast(list[int], d.pop("restrictedDepartmentIds"))

        restricted_group_ids = cast(list[int], d.pop("restrictedGroupIds"))

        browser_allowed = d.pop("browserAllowed")

        terminal_allowed = d.pop("terminalAllowed")

        app_allowed = d.pop("appAllowed")

        presence_allowed = d.pop("presenceAllowed")

        def _parse_also_illness(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        also_illness = _parse_also_illness(d.pop("alsoIllness"))

        def _parse_reduce_illness(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        reduce_illness = _parse_reduce_illness(d.pop("reduceIllness"))

        free_fields = []
        _free_fields = d.pop("freeFields")
        for free_fields_item_data in _free_fields:
            free_fields_item = GetAbsenceTypeResponse200FreeFieldsItem.from_dict(free_fields_item_data)

            free_fields.append(free_fields_item)

        get_absence_type_response_200 = cls(
            id=id,
            order_no=order_no,
            name=name,
            token=token,
            is_holiday=is_holiday,
            color=color,
            has_replace_time=has_replace_time,
            weighting_type=weighting_type,
            alt_name=alt_name,
            alt_color=alt_color,
            description=description,
            is_working_time=is_working_time,
            only_core_time=only_core_time,
            allowed_for_requests=allowed_for_requests,
            allowed_for_bookings_with_reason=allowed_for_bookings_with_reason,
            allowed_for_manual_full_day=allowed_for_manual_full_day,
            allowed_for_self=allowed_for_self,
            use_pause_rule=use_pause_rule,
            replace_time_state=replace_time_state,
            replace_time=replace_time,
            analysis_rounding=analysis_rounding,
            analysis_project=analysis_project,
            rounding_last_go=rounding_last_go,
            is_used=is_used,
            is_system=is_system,
            restricted_department_ids=restricted_department_ids,
            restricted_group_ids=restricted_group_ids,
            browser_allowed=browser_allowed,
            terminal_allowed=terminal_allowed,
            app_allowed=app_allowed,
            presence_allowed=presence_allowed,
            also_illness=also_illness,
            reduce_illness=reduce_illness,
            free_fields=free_fields,
        )

        return get_absence_type_response_200
