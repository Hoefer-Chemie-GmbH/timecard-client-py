from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_department_members_response_200_items_item_state import (
    ListDepartmentMembersResponse200ItemsItemState,
)

T = TypeVar("T", bound="ListDepartmentMembersResponse200ItemsItem")


@_attrs_define
class ListDepartmentMembersResponse200ItemsItem:
    """
    Attributes:
        id (int):
        person_no (None | str):
        first_name (str):
        last_name (str):
        display_name (str):
        sex (None | str):
        department (None | str):
        state (ListDepartmentMembersResponse200ItemsItemState):
        has_supervisor (bool):
        roles (list[str]):
        is_employee (bool | None):
        terminated_date (None | str):
    """

    id: int
    person_no: None | str
    first_name: str
    last_name: str
    display_name: str
    sex: None | str
    department: None | str
    state: ListDepartmentMembersResponse200ItemsItemState
    has_supervisor: bool
    roles: list[str]
    is_employee: bool | None
    terminated_date: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        person_no: None | str
        person_no = self.person_no

        first_name = self.first_name

        last_name = self.last_name

        display_name = self.display_name

        sex: None | str
        sex = self.sex

        department: None | str
        department = self.department

        state = self.state.value

        has_supervisor = self.has_supervisor

        roles = self.roles

        is_employee: bool | None
        is_employee = self.is_employee

        terminated_date: None | str
        terminated_date = self.terminated_date

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "personNo": person_no,
                "firstName": first_name,
                "lastName": last_name,
                "displayName": display_name,
                "sex": sex,
                "department": department,
                "state": state,
                "hasSupervisor": has_supervisor,
                "roles": roles,
                "isEmployee": is_employee,
                "terminatedDate": terminated_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_person_no(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        person_no = _parse_person_no(d.pop("personNo"))

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        display_name = d.pop("displayName")

        def _parse_sex(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sex = _parse_sex(d.pop("sex"))

        def _parse_department(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        department = _parse_department(d.pop("department"))

        state = ListDepartmentMembersResponse200ItemsItemState(d.pop("state"))

        has_supervisor = d.pop("hasSupervisor")

        roles = cast(list[str], d.pop("roles"))

        def _parse_is_employee(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_employee = _parse_is_employee(d.pop("isEmployee"))

        def _parse_terminated_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        terminated_date = _parse_terminated_date(d.pop("terminatedDate"))

        list_department_members_response_200_items_item = cls(
            id=id,
            person_no=person_no,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            sex=sex,
            department=department,
            state=state,
            has_supervisor=has_supervisor,
            roles=roles,
            is_employee=is_employee,
            terminated_date=terminated_date,
        )

        return list_department_members_response_200_items_item
