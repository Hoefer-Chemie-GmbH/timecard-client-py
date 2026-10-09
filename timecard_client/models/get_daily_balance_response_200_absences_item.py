from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetDailyBalanceResponse200AbsencesItem")


@_attrs_define
class GetDailyBalanceResponse200AbsencesItem:
    """
    Attributes:
        absence_type_id (int):
        name (str):
        duration_seconds (int):
    """

    absence_type_id: int
    name: str
    duration_seconds: int

    def to_dict(self) -> dict[str, Any]:
        absence_type_id = self.absence_type_id

        name = self.name

        duration_seconds = self.duration_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "absenceTypeId": absence_type_id,
                "name": name,
                "durationSeconds": duration_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        absence_type_id = d.pop("absenceTypeId")

        name = d.pop("name")

        duration_seconds = d.pop("durationSeconds")

        get_daily_balance_response_200_absences_item = cls(
            absence_type_id=absence_type_id,
            name=name,
            duration_seconds=duration_seconds,
        )

        return get_daily_balance_response_200_absences_item
