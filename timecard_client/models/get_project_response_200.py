from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_project_response_200_free_fields_item import GetProjectResponse200FreeFieldsItem


T = TypeVar("T", bound="GetProjectResponse200")


@_attrs_define
class GetProjectResponse200:
    """
    Attributes:
        id (int):
        name (str):
        token (None | str):
        number (int | None):
        description (None | str):
        end_date (None | str):
        is_active (bool):
        is_used (bool):
        work_operation_ids (list[int]):
        restricted_department_ids (list[int]):
        restricted_group_ids (list[int]):
        browser_allowed (bool):
        terminal_allowed (bool):
        app_allowed (bool):
        free_fields (list[GetProjectResponse200FreeFieldsItem]):
    """

    id: int
    name: str
    token: None | str
    number: int | None
    description: None | str
    end_date: None | str
    is_active: bool
    is_used: bool
    work_operation_ids: list[int]
    restricted_department_ids: list[int]
    restricted_group_ids: list[int]
    browser_allowed: bool
    terminal_allowed: bool
    app_allowed: bool
    free_fields: list[GetProjectResponse200FreeFieldsItem]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        token: None | str
        token = self.token

        number: int | None
        number = self.number

        description: None | str
        description = self.description

        end_date: None | str
        end_date = self.end_date

        is_active = self.is_active

        is_used = self.is_used

        work_operation_ids = self.work_operation_ids

        restricted_department_ids = self.restricted_department_ids

        restricted_group_ids = self.restricted_group_ids

        browser_allowed = self.browser_allowed

        terminal_allowed = self.terminal_allowed

        app_allowed = self.app_allowed

        free_fields = []
        for free_fields_item_data in self.free_fields:
            free_fields_item = free_fields_item_data.to_dict()
            free_fields.append(free_fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "token": token,
                "number": number,
                "description": description,
                "endDate": end_date,
                "isActive": is_active,
                "isUsed": is_used,
                "workOperationIds": work_operation_ids,
                "restrictedDepartmentIds": restricted_department_ids,
                "restrictedGroupIds": restricted_group_ids,
                "browserAllowed": browser_allowed,
                "terminalAllowed": terminal_allowed,
                "appAllowed": app_allowed,
                "freeFields": free_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_project_response_200_free_fields_item import (
            GetProjectResponse200FreeFieldsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        token = _parse_token(d.pop("token"))

        def _parse_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        number = _parse_number(d.pop("number"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_end_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end_date = _parse_end_date(d.pop("endDate"))

        is_active = d.pop("isActive")

        is_used = d.pop("isUsed")

        work_operation_ids = cast(list[int], d.pop("workOperationIds"))

        restricted_department_ids = cast(list[int], d.pop("restrictedDepartmentIds"))

        restricted_group_ids = cast(list[int], d.pop("restrictedGroupIds"))

        browser_allowed = d.pop("browserAllowed")

        terminal_allowed = d.pop("terminalAllowed")

        app_allowed = d.pop("appAllowed")

        free_fields = []
        _free_fields = d.pop("freeFields")
        for free_fields_item_data in _free_fields:
            free_fields_item = GetProjectResponse200FreeFieldsItem.from_dict(free_fields_item_data)

            free_fields.append(free_fields_item)

        get_project_response_200 = cls(
            id=id,
            name=name,
            token=token,
            number=number,
            description=description,
            end_date=end_date,
            is_active=is_active,
            is_used=is_used,
            work_operation_ids=work_operation_ids,
            restricted_department_ids=restricted_department_ids,
            restricted_group_ids=restricted_group_ids,
            browser_allowed=browser_allowed,
            terminal_allowed=terminal_allowed,
            app_allowed=app_allowed,
            free_fields=free_fields,
        )

        return get_project_response_200
