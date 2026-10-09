from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_person_body_sex import CreatePersonBodySex
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_person_body_free_fields_item import CreatePersonBodyFreeFieldsItem
    from ..models.create_person_body_time_recording import CreatePersonBodyTimeRecording


T = TypeVar("T", bound="CreatePersonBody")


@_attrs_define
class CreatePersonBody:
    """
    Attributes:
        first_name (str):
        last_name (str):
        person_no (None | str | Unset): personnel number; always written as PersonalNoAlpha
        sex (CreatePersonBodySex | Unset):
        title (None | str | Unset):
        name_prefix (None | str | Unset):
        name_affix (None | str | Unset):
        birthday (None | str | Unset):
        email (None | str | Unset):
        department_id (int | None | Unset):
        group_ids (list[int] | Unset):
        date_of_entry (None | str | Unset):
        date_of_termination (None | str | Unset):
        recording_begin (None | str | Unset):
        is_employee (bool | Unset): time recording; together with useLicence consumes an employee licence
        use_licence (bool | Unset):
        is_access_control_person (bool | Unset):
        access_key (None | str | Unset):
        region_id (int | None | Unset):
        free_fields (list[CreatePersonBodyFreeFieldsItem] | Unset):
        time_recording (CreatePersonBodyTimeRecording | Unset):
    """

    first_name: str
    last_name: str
    person_no: None | str | Unset = UNSET
    sex: CreatePersonBodySex | Unset = UNSET
    title: None | str | Unset = UNSET
    name_prefix: None | str | Unset = UNSET
    name_affix: None | str | Unset = UNSET
    birthday: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    department_id: int | None | Unset = UNSET
    group_ids: list[int] | Unset = UNSET
    date_of_entry: None | str | Unset = UNSET
    date_of_termination: None | str | Unset = UNSET
    recording_begin: None | str | Unset = UNSET
    is_employee: bool | Unset = UNSET
    use_licence: bool | Unset = UNSET
    is_access_control_person: bool | Unset = UNSET
    access_key: None | str | Unset = UNSET
    region_id: int | None | Unset = UNSET
    free_fields: list[CreatePersonBodyFreeFieldsItem] | Unset = UNSET
    time_recording: CreatePersonBodyTimeRecording | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        person_no: None | str | Unset
        if isinstance(self.person_no, Unset):
            person_no = UNSET
        else:
            person_no = self.person_no

        sex: str | Unset = UNSET
        if not isinstance(self.sex, Unset):
            sex = self.sex.value

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        name_prefix: None | str | Unset
        if isinstance(self.name_prefix, Unset):
            name_prefix = UNSET
        else:
            name_prefix = self.name_prefix

        name_affix: None | str | Unset
        if isinstance(self.name_affix, Unset):
            name_affix = UNSET
        else:
            name_affix = self.name_affix

        birthday: None | str | Unset
        if isinstance(self.birthday, Unset):
            birthday = UNSET
        else:
            birthday = self.birthday

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        department_id: int | None | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        else:
            department_id = self.department_id

        group_ids: list[int] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        date_of_entry: None | str | Unset
        if isinstance(self.date_of_entry, Unset):
            date_of_entry = UNSET
        else:
            date_of_entry = self.date_of_entry

        date_of_termination: None | str | Unset
        if isinstance(self.date_of_termination, Unset):
            date_of_termination = UNSET
        else:
            date_of_termination = self.date_of_termination

        recording_begin: None | str | Unset
        if isinstance(self.recording_begin, Unset):
            recording_begin = UNSET
        else:
            recording_begin = self.recording_begin

        is_employee = self.is_employee

        use_licence = self.use_licence

        is_access_control_person = self.is_access_control_person

        access_key: None | str | Unset
        if isinstance(self.access_key, Unset):
            access_key = UNSET
        else:
            access_key = self.access_key

        region_id: int | None | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        free_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.free_fields, Unset):
            free_fields = []
            for free_fields_item_data in self.free_fields:
                free_fields_item = free_fields_item_data.to_dict()
                free_fields.append(free_fields_item)

        time_recording: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_recording, Unset):
            time_recording = self.time_recording.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
            }
        )
        if person_no is not UNSET:
            field_dict["personNo"] = person_no
        if sex is not UNSET:
            field_dict["sex"] = sex
        if title is not UNSET:
            field_dict["title"] = title
        if name_prefix is not UNSET:
            field_dict["namePrefix"] = name_prefix
        if name_affix is not UNSET:
            field_dict["nameAffix"] = name_affix
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if email is not UNSET:
            field_dict["email"] = email
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if date_of_entry is not UNSET:
            field_dict["dateOfEntry"] = date_of_entry
        if date_of_termination is not UNSET:
            field_dict["dateOfTermination"] = date_of_termination
        if recording_begin is not UNSET:
            field_dict["recordingBegin"] = recording_begin
        if is_employee is not UNSET:
            field_dict["isEmployee"] = is_employee
        if use_licence is not UNSET:
            field_dict["useLicence"] = use_licence
        if is_access_control_person is not UNSET:
            field_dict["isAccessControlPerson"] = is_access_control_person
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if free_fields is not UNSET:
            field_dict["freeFields"] = free_fields
        if time_recording is not UNSET:
            field_dict["timeRecording"] = time_recording

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_person_body_free_fields_item import CreatePersonBodyFreeFieldsItem  # noqa: PLC0415
        from ..models.create_person_body_time_recording import CreatePersonBodyTimeRecording  # noqa: PLC0415

        d = dict(src_dict)
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        def _parse_person_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_no = _parse_person_no(d.pop("personNo", UNSET))

        _sex = d.pop("sex", UNSET)
        sex: CreatePersonBodySex | Unset
        if isinstance(_sex, Unset):
            sex = UNSET
        else:
            sex = CreatePersonBodySex(_sex)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_name_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_prefix = _parse_name_prefix(d.pop("namePrefix", UNSET))

        def _parse_name_affix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_affix = _parse_name_affix(d.pop("nameAffix", UNSET))

        def _parse_birthday(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        birthday = _parse_birthday(d.pop("birthday", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_department_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        department_id = _parse_department_id(d.pop("departmentId", UNSET))

        group_ids = cast(list[int], d.pop("groupIds", UNSET))

        def _parse_date_of_entry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_entry = _parse_date_of_entry(d.pop("dateOfEntry", UNSET))

        def _parse_date_of_termination(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_termination = _parse_date_of_termination(d.pop("dateOfTermination", UNSET))

        def _parse_recording_begin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recording_begin = _parse_recording_begin(d.pop("recordingBegin", UNSET))

        is_employee = d.pop("isEmployee", UNSET)

        use_licence = d.pop("useLicence", UNSET)

        is_access_control_person = d.pop("isAccessControlPerson", UNSET)

        def _parse_access_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_key = _parse_access_key(d.pop("accessKey", UNSET))

        def _parse_region_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        _free_fields = d.pop("freeFields", UNSET)
        free_fields: list[CreatePersonBodyFreeFieldsItem] | Unset = UNSET
        if _free_fields is not UNSET:
            free_fields = []
            for free_fields_item_data in _free_fields:
                free_fields_item = CreatePersonBodyFreeFieldsItem.from_dict(free_fields_item_data)

                free_fields.append(free_fields_item)

        _time_recording = d.pop("timeRecording", UNSET)
        time_recording: CreatePersonBodyTimeRecording | Unset
        if isinstance(_time_recording, Unset):
            time_recording = UNSET
        else:
            time_recording = CreatePersonBodyTimeRecording.from_dict(_time_recording)

        create_person_body = cls(
            first_name=first_name,
            last_name=last_name,
            person_no=person_no,
            sex=sex,
            title=title,
            name_prefix=name_prefix,
            name_affix=name_affix,
            birthday=birthday,
            email=email,
            department_id=department_id,
            group_ids=group_ids,
            date_of_entry=date_of_entry,
            date_of_termination=date_of_termination,
            recording_begin=recording_begin,
            is_employee=is_employee,
            use_licence=use_licence,
            is_access_control_person=is_access_control_person,
            access_key=access_key,
            region_id=region_id,
            free_fields=free_fields,
            time_recording=time_recording,
        )

        create_person_body.additional_properties = d
        return create_person_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
