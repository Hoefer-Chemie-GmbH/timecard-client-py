from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="LookupPresenceBody")


@_attrs_define
class LookupPresenceBody:
    """
    Attributes:
        person_ids (list[int]): person ids to look up
    """

    person_ids: list[int]

    def to_dict(self) -> dict[str, Any]:
        person_ids = self.person_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personIds": person_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_ids = cast(list[int], d.pop("personIds"))

        lookup_presence_body = cls(
            person_ids=person_ids,
        )

        return lookup_presence_body
