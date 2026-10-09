from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetDailyBalanceResponse200WorkingProfile")


@_attrs_define
class GetDailyBalanceResponse200WorkingProfile:
    """
    Attributes:
        name (None | str):
        is_optional (bool):
        is_monthly_target (bool):
        from_group (bool):
        missing (bool):
    """

    name: None | str
    is_optional: bool
    is_monthly_target: bool
    from_group: bool
    missing: bool

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        is_optional = self.is_optional

        is_monthly_target = self.is_monthly_target

        from_group = self.from_group

        missing = self.missing

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "isOptional": is_optional,
                "isMonthlyTarget": is_monthly_target,
                "fromGroup": from_group,
                "missing": missing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        is_optional = d.pop("isOptional")

        is_monthly_target = d.pop("isMonthlyTarget")

        from_group = d.pop("fromGroup")

        missing = d.pop("missing")

        get_daily_balance_response_200_working_profile = cls(
            name=name,
            is_optional=is_optional,
            is_monthly_target=is_monthly_target,
            from_group=from_group,
            missing=missing,
        )

        return get_daily_balance_response_200_working_profile
