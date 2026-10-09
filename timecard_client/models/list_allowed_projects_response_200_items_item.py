from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListAllowedProjectsResponse200ItemsItem")


@_attrs_define
class ListAllowedProjectsResponse200ItemsItem:
    """
    Attributes:
        id (int):
        name (str):
        number (int | None):
        token (None | str):
        working_time_dependent (bool):
        is_active (bool):
    """

    id: int
    name: str
    number: int | None
    token: None | str
    working_time_dependent: bool
    is_active: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        number: int | None
        number = self.number

        token: None | str
        token = self.token

        working_time_dependent = self.working_time_dependent

        is_active = self.is_active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "number": number,
                "token": token,
                "workingTimeDependent": working_time_dependent,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        number = _parse_number(d.pop("number"))

        def _parse_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        token = _parse_token(d.pop("token"))

        working_time_dependent = d.pop("workingTimeDependent")

        is_active = d.pop("isActive")

        list_allowed_projects_response_200_items_item = cls(
            id=id,
            name=name,
            number=number,
            token=token,
            working_time_dependent=working_time_dependent,
            is_active=is_active,
        )

        return list_allowed_projects_response_200_items_item
