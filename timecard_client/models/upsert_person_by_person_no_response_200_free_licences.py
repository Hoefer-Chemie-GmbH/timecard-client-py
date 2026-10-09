from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpsertPersonByPersonNoResponse200FreeLicences")


@_attrs_define
class UpsertPersonByPersonNoResponse200FreeLicences:
    """
    Attributes:
        employee (int | None):
        access_control (int | None):
        au (int | None):
        lohn (int | None):
    """

    employee: int | None
    access_control: int | None
    au: int | None
    lohn: int | None

    def to_dict(self) -> dict[str, Any]:
        employee: int | None
        employee = self.employee

        access_control: int | None
        access_control = self.access_control

        au: int | None
        au = self.au

        lohn: int | None
        lohn = self.lohn

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "employee": employee,
                "accessControl": access_control,
                "au": au,
                "lohn": lohn,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_employee(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        employee = _parse_employee(d.pop("employee"))

        def _parse_access_control(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        access_control = _parse_access_control(d.pop("accessControl"))

        def _parse_au(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        au = _parse_au(d.pop("au"))

        def _parse_lohn(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        lohn = _parse_lohn(d.pop("lohn"))

        upsert_person_by_person_no_response_200_free_licences = cls(
            employee=employee,
            access_control=access_control,
            au=au,
            lohn=lohn,
        )

        return upsert_person_by_person_no_response_200_free_licences
