from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AssignWorkingProfileResponse201")


@_attrs_define
class AssignWorkingProfileResponse201:
    """
    Attributes:
        person_ids (list[int]):
        working_profile_id (int): working time profile that applies optionally in the period
        from_ (str):
        to (str):
    """

    person_ids: list[int]
    working_profile_id: int
    from_: str
    to: str

    def to_dict(self) -> dict[str, Any]:
        person_ids = self.person_ids

        working_profile_id = self.working_profile_id

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personIds": person_ids,
                "workingProfileId": working_profile_id,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_ids = cast(list[int], d.pop("personIds"))

        working_profile_id = d.pop("workingProfileId")

        from_ = d.pop("from")

        to = d.pop("to")

        assign_working_profile_response_201 = cls(
            person_ids=person_ids,
            working_profile_id=working_profile_id,
            from_=from_,
            to=to,
        )

        return assign_working_profile_response_201
