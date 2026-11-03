from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetMeResponse200TimecardUserType0")


@_attrs_define
class GetMeResponse200TimecardUserType0:
    """
    Attributes:
        key (str): key of the timeCard login in the configuration of the facade
        user_name (str): timeCard user name
        person_id (int): timeCard person of the login
        person_name (str):
    """

    key: str
    user_name: str
    person_id: int
    person_name: str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        user_name = self.user_name

        person_id = self.person_id

        person_name = self.person_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "userName": user_name,
                "personId": person_id,
                "personName": person_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        user_name = d.pop("userName")

        person_id = d.pop("personId")

        person_name = d.pop("personName")

        get_me_response_200_timecard_user_type_0 = cls(
            key=key,
            user_name=user_name,
            person_id=person_id,
            person_name=person_name,
        )

        return get_me_response_200_timecard_user_type_0
