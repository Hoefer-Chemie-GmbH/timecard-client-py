from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0")


@_attrs_define
class GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0:
    """
    Attributes:
        start (str):
        end (str):
    """

    start: str
    end: str

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        get_working_profile_response_200_working_days_item_evaluated_time_type_0 = cls(
            start=start,
            end=end,
        )

        return get_working_profile_response_200_working_days_item_evaluated_time_type_0
