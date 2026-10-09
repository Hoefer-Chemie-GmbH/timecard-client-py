from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignWorkingProfileBody")


@_attrs_define
class AssignWorkingProfileBody:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_ids = self.person_ids

        working_profile_id = self.working_profile_id

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        assign_working_profile_body = cls(
            person_ids=person_ids,
            working_profile_id=working_profile_id,
            from_=from_,
            to=to,
        )

        assign_working_profile_body.additional_properties = d
        return assign_working_profile_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
