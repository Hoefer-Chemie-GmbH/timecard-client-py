from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListAbsenceTypesResponse200ItemsItem")


@_attrs_define
class ListAbsenceTypesResponse200ItemsItem:
    """
    Attributes:
        id (int):
        order_no (int):
        name (str):
        token (None | str):
        is_holiday (bool):
        color (None | str):
        has_replace_time (bool):
        weighting_type (int | None):
    """

    id: int
    order_no: int
    name: str
    token: None | str
    is_holiday: bool
    color: None | str
    has_replace_time: bool
    weighting_type: int | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        order_no = self.order_no

        name = self.name

        token: None | str
        token = self.token

        is_holiday = self.is_holiday

        color: None | str
        color = self.color

        has_replace_time = self.has_replace_time

        weighting_type: int | None
        weighting_type = self.weighting_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "orderNo": order_no,
                "name": name,
                "token": token,
                "isHoliday": is_holiday,
                "color": color,
                "hasReplaceTime": has_replace_time,
                "weightingType": weighting_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        order_no = d.pop("orderNo")

        name = d.pop("name")

        def _parse_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        token = _parse_token(d.pop("token"))

        is_holiday = d.pop("isHoliday")

        def _parse_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        color = _parse_color(d.pop("color"))

        has_replace_time = d.pop("hasReplaceTime")

        def _parse_weighting_type(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weighting_type = _parse_weighting_type(d.pop("weightingType"))

        list_absence_types_response_200_items_item = cls(
            id=id,
            order_no=order_no,
            name=name,
            token=token,
            is_holiday=is_holiday,
            color=color,
            has_replace_time=has_replace_time,
            weighting_type=weighting_type,
        )

        return list_absence_types_response_200_items_item
