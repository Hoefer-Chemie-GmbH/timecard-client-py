from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetVersionResponse200")


@_attrs_define
class GetVersionResponse200:
    """
    Attributes:
        facade_version (str):
        timecard_version (str):
    """

    facade_version: str
    timecard_version: str

    def to_dict(self) -> dict[str, Any]:
        facade_version = self.facade_version

        timecard_version = self.timecard_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "facadeVersion": facade_version,
                "timecardVersion": timecard_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        facade_version = d.pop("facadeVersion")

        timecard_version = d.pop("timecardVersion")

        get_version_response_200 = cls(
            facade_version=facade_version,
            timecard_version=timecard_version,
        )

        return get_version_response_200
