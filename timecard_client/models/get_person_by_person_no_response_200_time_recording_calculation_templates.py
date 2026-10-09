from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetPersonByPersonNoResponse200TimeRecordingCalculationTemplates")


@_attrs_define
class GetPersonByPersonNoResponse200TimeRecordingCalculationTemplates:
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

        get_person_by_person_no_response_200_time_recording_calculation_templates = cls(
            ids=ids,
            names=names,
            valid_from=valid_from,
        )

        return get_person_by_person_no_response_200_time_recording_calculation_templates
