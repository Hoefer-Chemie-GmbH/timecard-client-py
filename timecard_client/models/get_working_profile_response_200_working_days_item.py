from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_working_profile_response_200_working_days_item_core_time_2_type_0 import (
        GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0,
    )
    from ..models.get_working_profile_response_200_working_days_item_core_time_type_0 import (
        GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0,
    )
    from ..models.get_working_profile_response_200_working_days_item_evaluated_time_type_0 import (
        GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0,
    )
    from ..models.get_working_profile_response_200_working_days_item_permitted_time_type_0 import (
        GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0,
    )


T = TypeVar("T", bound="GetWorkingProfileResponse200WorkingDaysItem")


@_attrs_define
class GetWorkingProfileResponse200WorkingDaysItem:
    """
    Attributes:
        weekday (int):
        is_day_off (bool):
        same_as_weekday (int | None):
        target_time (None | str):
        sequently (bool):
        core_time (GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0 | None):
        core_time_2 (GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0 | None):
        permitted_time (GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0 | None):
        evaluated_time (GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0 | None):
        break_rule_ids (list[int]):
    """

    weekday: int
    is_day_off: bool
    same_as_weekday: int | None
    target_time: None | str
    sequently: bool
    core_time: GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0 | None
    core_time_2: GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0 | None
    permitted_time: GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0 | None
    evaluated_time: GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0 | None
    break_rule_ids: list[int]

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_working_profile_response_200_working_days_item_core_time_2_type_0 import (
            GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0,  # noqa: PLC0415
        )
        from ..models.get_working_profile_response_200_working_days_item_core_time_type_0 import (
            GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0,  # noqa: PLC0415
        )
        from ..models.get_working_profile_response_200_working_days_item_evaluated_time_type_0 import (
            GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0,  # noqa: PLC0415
        )
        from ..models.get_working_profile_response_200_working_days_item_permitted_time_type_0 import (
            GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0,  # noqa: PLC0415
        )

        weekday = self.weekday

        is_day_off = self.is_day_off

        same_as_weekday: int | None
        same_as_weekday = self.same_as_weekday

        target_time: None | str
        target_time = self.target_time

        sequently = self.sequently

        core_time: dict[str, Any] | None
        if isinstance(self.core_time, GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0):
            core_time = self.core_time.to_dict()
        else:
            core_time = self.core_time

        core_time_2: dict[str, Any] | None
        if isinstance(self.core_time_2, GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0):
            core_time_2 = self.core_time_2.to_dict()
        else:
            core_time_2 = self.core_time_2

        permitted_time: dict[str, Any] | None
        if isinstance(self.permitted_time, GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0):
            permitted_time = self.permitted_time.to_dict()
        else:
            permitted_time = self.permitted_time

        evaluated_time: dict[str, Any] | None
        if isinstance(self.evaluated_time, GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0):
            evaluated_time = self.evaluated_time.to_dict()
        else:
            evaluated_time = self.evaluated_time

        break_rule_ids = self.break_rule_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "weekday": weekday,
                "isDayOff": is_day_off,
                "sameAsWeekday": same_as_weekday,
                "targetTime": target_time,
                "sequently": sequently,
                "coreTime": core_time,
                "coreTime2": core_time_2,
                "permittedTime": permitted_time,
                "evaluatedTime": evaluated_time,
                "breakRuleIds": break_rule_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_working_profile_response_200_working_days_item_core_time_2_type_0 import (
            GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0,  # noqa: PLC0415
        )
        from ..models.get_working_profile_response_200_working_days_item_core_time_type_0 import (
            GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0,  # noqa: PLC0415
        )
        from ..models.get_working_profile_response_200_working_days_item_evaluated_time_type_0 import (
            GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0,  # noqa: PLC0415
        )
        from ..models.get_working_profile_response_200_working_days_item_permitted_time_type_0 import (
            GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        weekday = d.pop("weekday")

        is_day_off = d.pop("isDayOff")

        def _parse_same_as_weekday(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        same_as_weekday = _parse_same_as_weekday(d.pop("sameAsWeekday"))

        def _parse_target_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_time = _parse_target_time(d.pop("targetTime"))

        sequently = d.pop("sequently")

        def _parse_core_time(data: object) -> GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                core_time_type_0 = GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0.from_dict(data)

                return core_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0 | None, data)

        core_time = _parse_core_time(d.pop("coreTime"))

        def _parse_core_time_2(data: object) -> GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                core_time_2_type_0 = GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0.from_dict(data)

                return core_time_2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0 | None, data)

        core_time_2 = _parse_core_time_2(d.pop("coreTime2"))

        def _parse_permitted_time(data: object) -> GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                permitted_time_type_0 = GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0.from_dict(data)

                return permitted_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0 | None, data)

        permitted_time = _parse_permitted_time(d.pop("permittedTime"))

        def _parse_evaluated_time(data: object) -> GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evaluated_time_type_0 = GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0.from_dict(data)

                return evaluated_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0 | None, data)

        evaluated_time = _parse_evaluated_time(d.pop("evaluatedTime"))

        break_rule_ids = cast(list[int], d.pop("breakRuleIds"))

        get_working_profile_response_200_working_days_item = cls(
            weekday=weekday,
            is_day_off=is_day_off,
            same_as_weekday=same_as_weekday,
            target_time=target_time,
            sequently=sequently,
            core_time=core_time,
            core_time_2=core_time_2,
            permitted_time=permitted_time,
            evaluated_time=evaluated_time,
            break_rule_ids=break_rule_ids,
        )

        return get_working_profile_response_200_working_days_item
