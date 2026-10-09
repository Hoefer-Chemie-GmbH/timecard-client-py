from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetDailyBalanceResponse200ProjectsItem")


@_attrs_define
class GetDailyBalanceResponse200ProjectsItem:
    """
    Attributes:
        project_id (int):
        work_operation_id (int | None):
        name (str):
        work_operation_name (None | str):
        duration_seconds (int):
    """

    project_id: int
    work_operation_id: int | None
    name: str
    work_operation_name: None | str
    duration_seconds: int

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        work_operation_id: int | None
        work_operation_id = self.work_operation_id

        name = self.name

        work_operation_name: None | str
        work_operation_name = self.work_operation_name

        duration_seconds = self.duration_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "projectId": project_id,
                "workOperationId": work_operation_id,
                "name": name,
                "workOperationName": work_operation_name,
                "durationSeconds": duration_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        def _parse_work_operation_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        work_operation_id = _parse_work_operation_id(d.pop("workOperationId"))

        name = d.pop("name")

        def _parse_work_operation_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        work_operation_name = _parse_work_operation_name(d.pop("workOperationName"))

        duration_seconds = d.pop("durationSeconds")

        get_daily_balance_response_200_projects_item = cls(
            project_id=project_id,
            work_operation_id=work_operation_id,
            name=name,
            work_operation_name=work_operation_name,
            duration_seconds=duration_seconds,
        )

        return get_daily_balance_response_200_projects_item
