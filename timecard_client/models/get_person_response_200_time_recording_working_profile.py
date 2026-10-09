from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetPersonResponse200TimeRecordingWorkingProfile")


@_attrs_define
class GetPersonResponse200TimeRecordingWorkingProfile:
    """
    Attributes:
        id (int | None):
        name (None | str):
        valid_from (None | str):
    """

    id: int | None
    name: None | str
    valid_from: None | str

    def to_dict(self) -> dict[str, Any]:
        id: int | None
        id = self.id

        name: None | str
        name = self.name

        valid_from: None | str
        valid_from = self.valid_from

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "validFrom": valid_from,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        id = _parse_id(d.pop("id"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_valid_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        valid_from = _parse_valid_from(d.pop("validFrom"))

        get_person_response_200_time_recording_working_profile = cls(
            id=id,
            name=name,
            valid_from=valid_from,
        )

        return get_person_response_200_time_recording_working_profile
