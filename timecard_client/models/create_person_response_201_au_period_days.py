from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreatePersonResponse201AuPeriodDays")


@_attrs_define
class CreatePersonResponse201AuPeriodDays:
    """
    Attributes:
        default (int):
        person (int | None):
    """

    default: int
    person: int | None

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        person: int | None
        person = self.person

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "default": default,
                "person": person,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default = d.pop("default")

        def _parse_person(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        person = _parse_person(d.pop("person"))

        create_person_response_201_au_period_days = cls(
            default=default,
            person=person,
        )

        return create_person_response_201_au_period_days
