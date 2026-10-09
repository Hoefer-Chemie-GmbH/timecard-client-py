from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.upsert_person_by_person_no_response_200_au_period_days import (
        UpsertPersonByPersonNoResponse200AuPeriodDays,
    )
    from ..models.upsert_person_by_person_no_response_200_external_logins import (
        UpsertPersonByPersonNoResponse200ExternalLogins,
    )
    from ..models.upsert_person_by_person_no_response_200_free_fields_item import (
        UpsertPersonByPersonNoResponse200FreeFieldsItem,
    )
    from ..models.upsert_person_by_person_no_response_200_free_licences import (
        UpsertPersonByPersonNoResponse200FreeLicences,
    )
    from ..models.upsert_person_by_person_no_response_200_modules import UpsertPersonByPersonNoResponse200Modules
    from ..models.upsert_person_by_person_no_response_200_time_recording import (
        UpsertPersonByPersonNoResponse200TimeRecording,
    )


T = TypeVar("T", bound="UpsertPersonByPersonNoResponse200")


@_attrs_define
class UpsertPersonByPersonNoResponse200:
    """
    Attributes:
        id (int):
        person_no (None | str):
        is_active (bool):
        has_supervisor (bool):
        sex (str):
        title (None | str):
        first_name (str):
        last_name (str):
        name_prefix (None | str):
        birthday (None | str):
        email (None | str):
        department_id (int | None):
        group_ids (list[int]):
        is_employee (bool):
        is_access_control_person (bool):
        use_licence (bool):
        modules (UpsertPersonByPersonNoResponse200Modules):
        free_licences (UpsertPersonByPersonNoResponse200FreeLicences):
        is_timecard_user (bool):
        username (None | str):
        is_account_locked (bool):
        access_key (None | str):
        user_profile_id (int | None):
        user_profile_elevated_id (int | None):
        recording_begin (None | str):
        date_of_entry (None | str):
        date_of_termination (None | str):
        use_group_profile (bool):
        profile_group_id (int | None):
        has_time_recording_profile (bool):
        no_booking_images_allowed (bool):
        gps_tracking_required (bool):
        region_id (int | None):
        au_period_days (UpsertPersonByPersonNoResponse200AuPeriodDays):
        application_group_id (int | None):
        has_bookings (bool | None):
        external_logins (UpsertPersonByPersonNoResponse200ExternalLogins):
        free_fields (list[UpsertPersonByPersonNoResponse200FreeFieldsItem]):
        time_recording (UpsertPersonByPersonNoResponse200TimeRecording):
    """

    id: int
    person_no: None | str
    is_active: bool
    has_supervisor: bool
    sex: str
    title: None | str
    first_name: str
    last_name: str
    name_prefix: None | str
    birthday: None | str
    email: None | str
    department_id: int | None
    group_ids: list[int]
    is_employee: bool
    is_access_control_person: bool
    use_licence: bool
    modules: UpsertPersonByPersonNoResponse200Modules
    free_licences: UpsertPersonByPersonNoResponse200FreeLicences
    is_timecard_user: bool
    username: None | str
    is_account_locked: bool
    access_key: None | str
    user_profile_id: int | None
    user_profile_elevated_id: int | None
    recording_begin: None | str
    date_of_entry: None | str
    date_of_termination: None | str
    use_group_profile: bool
    profile_group_id: int | None
    has_time_recording_profile: bool
    no_booking_images_allowed: bool
    gps_tracking_required: bool
    region_id: int | None
    au_period_days: UpsertPersonByPersonNoResponse200AuPeriodDays
    application_group_id: int | None
    has_bookings: bool | None
    external_logins: UpsertPersonByPersonNoResponse200ExternalLogins
    free_fields: list[UpsertPersonByPersonNoResponse200FreeFieldsItem]
    time_recording: UpsertPersonByPersonNoResponse200TimeRecording

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        person_no: None | str
        person_no = self.person_no

        is_active = self.is_active

        has_supervisor = self.has_supervisor

        sex = self.sex

        title: None | str
        title = self.title

        first_name = self.first_name

        last_name = self.last_name

        name_prefix: None | str
        name_prefix = self.name_prefix

        birthday: None | str
        birthday = self.birthday

        email: None | str
        email = self.email

        department_id: int | None
        department_id = self.department_id

        group_ids = self.group_ids

        is_employee = self.is_employee

        is_access_control_person = self.is_access_control_person

        use_licence = self.use_licence

        modules = self.modules.to_dict()

        free_licences = self.free_licences.to_dict()

        is_timecard_user = self.is_timecard_user

        username: None | str
        username = self.username

        is_account_locked = self.is_account_locked

        access_key: None | str
        access_key = self.access_key

        user_profile_id: int | None
        user_profile_id = self.user_profile_id

        user_profile_elevated_id: int | None
        user_profile_elevated_id = self.user_profile_elevated_id

        recording_begin: None | str
        recording_begin = self.recording_begin

        date_of_entry: None | str
        date_of_entry = self.date_of_entry

        date_of_termination: None | str
        date_of_termination = self.date_of_termination

        use_group_profile = self.use_group_profile

        profile_group_id: int | None
        profile_group_id = self.profile_group_id

        has_time_recording_profile = self.has_time_recording_profile

        no_booking_images_allowed = self.no_booking_images_allowed

        gps_tracking_required = self.gps_tracking_required

        region_id: int | None
        region_id = self.region_id

        au_period_days = self.au_period_days.to_dict()

        application_group_id: int | None
        application_group_id = self.application_group_id

        has_bookings: bool | None
        has_bookings = self.has_bookings

        external_logins = self.external_logins.to_dict()

        free_fields = []
        for free_fields_item_data in self.free_fields:
            free_fields_item = free_fields_item_data.to_dict()
            free_fields.append(free_fields_item)

        time_recording = self.time_recording.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "personNo": person_no,
                "isActive": is_active,
                "hasSupervisor": has_supervisor,
                "sex": sex,
                "title": title,
                "firstName": first_name,
                "lastName": last_name,
                "namePrefix": name_prefix,
                "birthday": birthday,
                "email": email,
                "departmentId": department_id,
                "groupIds": group_ids,
                "isEmployee": is_employee,
                "isAccessControlPerson": is_access_control_person,
                "useLicence": use_licence,
                "modules": modules,
                "freeLicences": free_licences,
                "isTimecardUser": is_timecard_user,
                "username": username,
                "isAccountLocked": is_account_locked,
                "accessKey": access_key,
                "userProfileId": user_profile_id,
                "userProfileElevatedId": user_profile_elevated_id,
                "recordingBegin": recording_begin,
                "dateOfEntry": date_of_entry,
                "dateOfTermination": date_of_termination,
                "useGroupProfile": use_group_profile,
                "profileGroupId": profile_group_id,
                "hasTimeRecordingProfile": has_time_recording_profile,
                "noBookingImagesAllowed": no_booking_images_allowed,
                "gpsTrackingRequired": gps_tracking_required,
                "regionId": region_id,
                "auPeriodDays": au_period_days,
                "applicationGroupId": application_group_id,
                "hasBookings": has_bookings,
                "externalLogins": external_logins,
                "freeFields": free_fields,
                "timeRecording": time_recording,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upsert_person_by_person_no_response_200_au_period_days import (
            UpsertPersonByPersonNoResponse200AuPeriodDays,  # noqa: PLC0415
        )
        from ..models.upsert_person_by_person_no_response_200_external_logins import (
            UpsertPersonByPersonNoResponse200ExternalLogins,  # noqa: PLC0415
        )
        from ..models.upsert_person_by_person_no_response_200_free_fields_item import (
            UpsertPersonByPersonNoResponse200FreeFieldsItem,  # noqa: PLC0415
        )
        from ..models.upsert_person_by_person_no_response_200_free_licences import (
            UpsertPersonByPersonNoResponse200FreeLicences,  # noqa: PLC0415
        )
        from ..models.upsert_person_by_person_no_response_200_modules import (
            UpsertPersonByPersonNoResponse200Modules,  # noqa: PLC0415
        )
        from ..models.upsert_person_by_person_no_response_200_time_recording import (
            UpsertPersonByPersonNoResponse200TimeRecording,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_person_no(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        person_no = _parse_person_no(d.pop("personNo"))

        is_active = d.pop("isActive")

        has_supervisor = d.pop("hasSupervisor")

        sex = d.pop("sex")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        def _parse_name_prefix(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name_prefix = _parse_name_prefix(d.pop("namePrefix"))

        def _parse_birthday(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birthday = _parse_birthday(d.pop("birthday"))

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_department_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        department_id = _parse_department_id(d.pop("departmentId"))

        group_ids = cast(list[int], d.pop("groupIds"))

        is_employee = d.pop("isEmployee")

        is_access_control_person = d.pop("isAccessControlPerson")

        use_licence = d.pop("useLicence")

        modules = UpsertPersonByPersonNoResponse200Modules.from_dict(d.pop("modules"))

        free_licences = UpsertPersonByPersonNoResponse200FreeLicences.from_dict(d.pop("freeLicences"))

        is_timecard_user = d.pop("isTimecardUser")

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        is_account_locked = d.pop("isAccountLocked")

        def _parse_access_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        access_key = _parse_access_key(d.pop("accessKey"))

        def _parse_user_profile_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        user_profile_id = _parse_user_profile_id(d.pop("userProfileId"))

        def _parse_user_profile_elevated_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        user_profile_elevated_id = _parse_user_profile_elevated_id(d.pop("userProfileElevatedId"))

        def _parse_recording_begin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        recording_begin = _parse_recording_begin(d.pop("recordingBegin"))

        def _parse_date_of_entry(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        date_of_entry = _parse_date_of_entry(d.pop("dateOfEntry"))

        def _parse_date_of_termination(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        date_of_termination = _parse_date_of_termination(d.pop("dateOfTermination"))

        use_group_profile = d.pop("useGroupProfile")

        def _parse_profile_group_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        profile_group_id = _parse_profile_group_id(d.pop("profileGroupId"))

        has_time_recording_profile = d.pop("hasTimeRecordingProfile")

        no_booking_images_allowed = d.pop("noBookingImagesAllowed")

        gps_tracking_required = d.pop("gpsTrackingRequired")

        def _parse_region_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        region_id = _parse_region_id(d.pop("regionId"))

        au_period_days = UpsertPersonByPersonNoResponse200AuPeriodDays.from_dict(d.pop("auPeriodDays"))

        def _parse_application_group_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        application_group_id = _parse_application_group_id(d.pop("applicationGroupId"))

        def _parse_has_bookings(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        has_bookings = _parse_has_bookings(d.pop("hasBookings"))

        external_logins = UpsertPersonByPersonNoResponse200ExternalLogins.from_dict(d.pop("externalLogins"))

        free_fields = []
        _free_fields = d.pop("freeFields")
        for free_fields_item_data in _free_fields:
            free_fields_item = UpsertPersonByPersonNoResponse200FreeFieldsItem.from_dict(free_fields_item_data)

            free_fields.append(free_fields_item)

        time_recording = UpsertPersonByPersonNoResponse200TimeRecording.from_dict(d.pop("timeRecording"))

        upsert_person_by_person_no_response_200 = cls(
            id=id,
            person_no=person_no,
            is_active=is_active,
            has_supervisor=has_supervisor,
            sex=sex,
            title=title,
            first_name=first_name,
            last_name=last_name,
            name_prefix=name_prefix,
            birthday=birthday,
            email=email,
            department_id=department_id,
            group_ids=group_ids,
            is_employee=is_employee,
            is_access_control_person=is_access_control_person,
            use_licence=use_licence,
            modules=modules,
            free_licences=free_licences,
            is_timecard_user=is_timecard_user,
            username=username,
            is_account_locked=is_account_locked,
            access_key=access_key,
            user_profile_id=user_profile_id,
            user_profile_elevated_id=user_profile_elevated_id,
            recording_begin=recording_begin,
            date_of_entry=date_of_entry,
            date_of_termination=date_of_termination,
            use_group_profile=use_group_profile,
            profile_group_id=profile_group_id,
            has_time_recording_profile=has_time_recording_profile,
            no_booking_images_allowed=no_booking_images_allowed,
            gps_tracking_required=gps_tracking_required,
            region_id=region_id,
            au_period_days=au_period_days,
            application_group_id=application_group_id,
            has_bookings=has_bookings,
            external_logins=external_logins,
            free_fields=free_fields,
            time_recording=time_recording,
        )

        return upsert_person_by_person_no_response_200
