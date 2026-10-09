from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreatePersonResponse201TimeRecordingCalculationTemplates")


@_attrs_define
class CreatePersonResponse201TimeRecordingCalculationTemplates:
    """
    Attributes:
        ids (list[int]):
        names (list[str]):
        valid_from (None | str):
    """

    ids: list[int]
    names: list[str]
    valid_from: None | str

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        names = self.names

        valid_from: None | str
        valid_from = self.valid_from

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ids": ids,
                "names": names,
                "validFrom": valid_from,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[int], d.pop("ids"))

        names = cast(list[str], d.pop("names"))

        def _parse_valid_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        valid_from = _parse_valid_from(d.pop("validFrom"))

        create_person_response_201_time_recording_calculation_templates = cls(
            ids=ids,
            names=names,
            valid_from=valid_from,
        )

        return create_person_response_201_time_recording_calculation_templates
