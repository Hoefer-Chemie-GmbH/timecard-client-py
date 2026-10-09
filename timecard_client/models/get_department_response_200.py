from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_department_response_200_kind import GetDepartmentResponse200Kind

if TYPE_CHECKING:
    from ..models.get_department_response_200_free_fields_item import GetDepartmentResponse200FreeFieldsItem
    from ..models.get_department_response_200_time_recording_type_0 import GetDepartmentResponse200TimeRecordingType0


T = TypeVar("T", bound="GetDepartmentResponse200")


@_attrs_define
class GetDepartmentResponse200:
    """
    Attributes:
        id (int):
        name (str):
        description (None | str):
        kind (GetDepartmentResponse200Kind):
        leader_person_ids (list[int]):
        member_person_ids (list[int] | None):
        has_time_recording_profile (bool):
        is_active (bool):
        is_used (bool):
        free_fields (list[GetDepartmentResponse200FreeFieldsItem]):
        time_recording (GetDepartmentResponse200TimeRecordingType0 | None):
    """

    id: int
    name: str
    description: None | str
    kind: GetDepartmentResponse200Kind
    leader_person_ids: list[int]
    member_person_ids: list[int] | None
    has_time_recording_profile: bool
    is_active: bool
    is_used: bool
    free_fields: list[GetDepartmentResponse200FreeFieldsItem]
    time_recording: GetDepartmentResponse200TimeRecordingType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_department_response_200_time_recording_type_0 import (
            GetDepartmentResponse200TimeRecordingType0,  # noqa: PLC0415
        )

        id = self.id

        name = self.name

        description: None | str
        description = self.description

        kind = self.kind.value

        leader_person_ids = self.leader_person_ids

        member_person_ids: list[int] | None
        if isinstance(self.member_person_ids, list):
            member_person_ids = self.member_person_ids

        else:
            member_person_ids = self.member_person_ids

        has_time_recording_profile = self.has_time_recording_profile

        is_active = self.is_active

        is_used = self.is_used

        free_fields = []
        for free_fields_item_data in self.free_fields:
            free_fields_item = free_fields_item_data.to_dict()
            free_fields.append(free_fields_item)

        time_recording: dict[str, Any] | None
        if isinstance(self.time_recording, GetDepartmentResponse200TimeRecordingType0):
            time_recording = self.time_recording.to_dict()
        else:
            time_recording = self.time_recording

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "kind": kind,
                "leaderPersonIds": leader_person_ids,
                "memberPersonIds": member_person_ids,
                "hasTimeRecordingProfile": has_time_recording_profile,
                "isActive": is_active,
                "isUsed": is_used,
                "freeFields": free_fields,
                "timeRecording": time_recording,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_department_response_200_free_fields_item import (
            GetDepartmentResponse200FreeFieldsItem,  # noqa: PLC0415
        )
        from ..models.get_department_response_200_time_recording_type_0 import (
            GetDepartmentResponse200TimeRecordingType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        kind = GetDepartmentResponse200Kind(d.pop("kind"))

        leader_person_ids = cast(list[int], d.pop("leaderPersonIds"))

        def _parse_member_person_ids(data: object) -> list[int] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_person_ids_type_0 = cast(list[int], data)

                return member_person_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None, data)

        member_person_ids = _parse_member_person_ids(d.pop("memberPersonIds"))

        has_time_recording_profile = d.pop("hasTimeRecordingProfile")

        is_active = d.pop("isActive")

        is_used = d.pop("isUsed")

        free_fields = []
        _free_fields = d.pop("freeFields")
        for free_fields_item_data in _free_fields:
            free_fields_item = GetDepartmentResponse200FreeFieldsItem.from_dict(free_fields_item_data)

            free_fields.append(free_fields_item)

        def _parse_time_recording(data: object) -> GetDepartmentResponse200TimeRecordingType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_recording_type_0 = GetDepartmentResponse200TimeRecordingType0.from_dict(data)

                return time_recording_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetDepartmentResponse200TimeRecordingType0 | None, data)

        time_recording = _parse_time_recording(d.pop("timeRecording"))

        get_department_response_200 = cls(
            id=id,
            name=name,
            description=description,
            kind=kind,
            leader_person_ids=leader_person_ids,
            member_person_ids=member_person_ids,
            has_time_recording_profile=has_time_recording_profile,
            is_active=is_active,
            is_used=is_used,
            free_fields=free_fields,
            time_recording=time_recording,
        )

        return get_department_response_200
