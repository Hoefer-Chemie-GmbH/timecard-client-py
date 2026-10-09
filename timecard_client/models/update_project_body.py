from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProjectBody")


@_attrs_define
class UpdateProjectBody:
    """
    Attributes:
        name (str | Unset):
        token (None | str | Unset): short code shown in the UI
        number (int | None | Unset): unique number shown in the UI; null for none
        description (None | str | Unset):
        end_date (None | str | Unset): last day the project can be booked; null for open-ended
        is_active (bool | Unset):
        work_operation_ids (list[int] | Unset): work operations that may be booked on the project
        restricted_department_ids (list[int] | Unset):
        restricted_group_ids (list[int] | Unset):
        browser_allowed (bool | Unset):
        terminal_allowed (bool | Unset):
        app_allowed (bool | Unset):
    """

    name: str | Unset = UNSET
    token: None | str | Unset = UNSET
    number: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    work_operation_ids: list[int] | Unset = UNSET
    restricted_department_ids: list[int] | Unset = UNSET
    restricted_group_ids: list[int] | Unset = UNSET
    browser_allowed: bool | Unset = UNSET
    terminal_allowed: bool | Unset = UNSET
    app_allowed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        number: int | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        is_active = self.is_active

        work_operation_ids: list[int] | Unset = UNSET
        if not isinstance(self.work_operation_ids, Unset):
            work_operation_ids = self.work_operation_ids

        restricted_department_ids: list[int] | Unset = UNSET
        if not isinstance(self.restricted_department_ids, Unset):
            restricted_department_ids = self.restricted_department_ids

        restricted_group_ids: list[int] | Unset = UNSET
        if not isinstance(self.restricted_group_ids, Unset):
            restricted_group_ids = self.restricted_group_ids

        browser_allowed = self.browser_allowed

        terminal_allowed = self.terminal_allowed

        app_allowed = self.app_allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if token is not UNSET:
            field_dict["token"] = token
        if number is not UNSET:
            field_dict["number"] = number
        if description is not UNSET:
            field_dict["description"] = description
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if work_operation_ids is not UNSET:
            field_dict["workOperationIds"] = work_operation_ids
        if restricted_department_ids is not UNSET:
            field_dict["restrictedDepartmentIds"] = restricted_department_ids
        if restricted_group_ids is not UNSET:
            field_dict["restrictedGroupIds"] = restricted_group_ids
        if browser_allowed is not UNSET:
            field_dict["browserAllowed"] = browser_allowed
        if terminal_allowed is not UNSET:
            field_dict["terminalAllowed"] = terminal_allowed
        if app_allowed is not UNSET:
            field_dict["appAllowed"] = app_allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

        def _parse_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        is_active = d.pop("isActive", UNSET)

        work_operation_ids = cast(list[int], d.pop("workOperationIds", UNSET))

        restricted_department_ids = cast(list[int], d.pop("restrictedDepartmentIds", UNSET))

        restricted_group_ids = cast(list[int], d.pop("restrictedGroupIds", UNSET))

        browser_allowed = d.pop("browserAllowed", UNSET)

        terminal_allowed = d.pop("terminalAllowed", UNSET)

        app_allowed = d.pop("appAllowed", UNSET)

        update_project_body = cls(
            name=name,
            token=token,
            number=number,
            description=description,
            end_date=end_date,
            is_active=is_active,
            work_operation_ids=work_operation_ids,
            restricted_department_ids=restricted_department_ids,
            restricted_group_ids=restricted_group_ids,
            browser_allowed=browser_allowed,
            terminal_allowed=terminal_allowed,
            app_allowed=app_allowed,
        )

        update_project_body.additional_properties = d
        return update_project_body

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
