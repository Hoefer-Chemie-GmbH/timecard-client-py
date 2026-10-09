from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListCalculationTemplatesResponse200ItemsItem")


@_attrs_define
class ListCalculationTemplatesResponse200ItemsItem:
    """
    Attributes:
        id (int):
        order_no (int):
        name (str):
        type_ (str):
        last_change (None | str):
        is_active (bool):
        is_system_account (bool):
        is_default_month_overview (bool | None):
    """

    id: int
    order_no: int
    name: str
    type_: str
    last_change: None | str
    is_active: bool
    is_system_account: bool
    is_default_month_overview: bool | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        order_no = self.order_no

        name = self.name

        type_ = self.type_

        last_change: None | str
        last_change = self.last_change

        is_active = self.is_active

        is_system_account = self.is_system_account

        is_default_month_overview: bool | None
        is_default_month_overview = self.is_default_month_overview

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "orderNo": order_no,
                "name": name,
                "type": type_,
                "lastChange": last_change,
                "isActive": is_active,
                "isSystemAccount": is_system_account,
                "isDefaultMonthOverview": is_default_month_overview,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        order_no = d.pop("orderNo")

        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_last_change(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_change = _parse_last_change(d.pop("lastChange"))

        is_active = d.pop("isActive")

        is_system_account = d.pop("isSystemAccount")

        def _parse_is_default_month_overview(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_default_month_overview = _parse_is_default_month_overview(d.pop("isDefaultMonthOverview"))

        list_calculation_templates_response_200_items_item = cls(
            id=id,
            order_no=order_no,
            name=name,
            type_=type_,
            last_change=last_change,
            is_active=is_active,
            is_system_account=is_system_account,
            is_default_month_overview=is_default_month_overview,
        )

        return list_calculation_templates_response_200_items_item
