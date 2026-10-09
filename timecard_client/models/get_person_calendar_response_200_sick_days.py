from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_person_calendar_response_200_sick_days_certificate_available_item import (
        GetPersonCalendarResponse200SickDaysCertificateAvailableItem,
    )
    from ..models.get_person_calendar_response_200_sick_days_certificate_missing_item import (
        GetPersonCalendarResponse200SickDaysCertificateMissingItem,
    )
    from ..models.get_person_calendar_response_200_sick_days_certificate_not_required_item import (
        GetPersonCalendarResponse200SickDaysCertificateNotRequiredItem,
    )


T = TypeVar("T", bound="GetPersonCalendarResponse200SickDays")


@_attrs_define
class GetPersonCalendarResponse200SickDays:
    """
    Attributes:
        certificate_not_required (list[GetPersonCalendarResponse200SickDaysCertificateNotRequiredItem]):
        certificate_missing (list[GetPersonCalendarResponse200SickDaysCertificateMissingItem]):
        certificate_available (list[GetPersonCalendarResponse200SickDaysCertificateAvailableItem]):
    """

    certificate_not_required: list[GetPersonCalendarResponse200SickDaysCertificateNotRequiredItem]
    certificate_missing: list[GetPersonCalendarResponse200SickDaysCertificateMissingItem]
    certificate_available: list[GetPersonCalendarResponse200SickDaysCertificateAvailableItem]

    def to_dict(self) -> dict[str, Any]:
        certificate_not_required = []
        for certificate_not_required_item_data in self.certificate_not_required:
            certificate_not_required_item = certificate_not_required_item_data.to_dict()
            certificate_not_required.append(certificate_not_required_item)

        certificate_missing = []
        for certificate_missing_item_data in self.certificate_missing:
            certificate_missing_item = certificate_missing_item_data.to_dict()
            certificate_missing.append(certificate_missing_item)

        certificate_available = []
        for certificate_available_item_data in self.certificate_available:
            certificate_available_item = certificate_available_item_data.to_dict()
            certificate_available.append(certificate_available_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "certificateNotRequired": certificate_not_required,
                "certificateMissing": certificate_missing,
                "certificateAvailable": certificate_available,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_person_calendar_response_200_sick_days_certificate_available_item import (
            GetPersonCalendarResponse200SickDaysCertificateAvailableItem,  # noqa: PLC0415
        )
        from ..models.get_person_calendar_response_200_sick_days_certificate_missing_item import (
            GetPersonCalendarResponse200SickDaysCertificateMissingItem,  # noqa: PLC0415
        )
        from ..models.get_person_calendar_response_200_sick_days_certificate_not_required_item import (
            GetPersonCalendarResponse200SickDaysCertificateNotRequiredItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        certificate_not_required = []
        _certificate_not_required = d.pop("certificateNotRequired")
        for certificate_not_required_item_data in _certificate_not_required:
            certificate_not_required_item = GetPersonCalendarResponse200SickDaysCertificateNotRequiredItem.from_dict(
                certificate_not_required_item_data
            )

            certificate_not_required.append(certificate_not_required_item)

        certificate_missing = []
        _certificate_missing = d.pop("certificateMissing")
        for certificate_missing_item_data in _certificate_missing:
            certificate_missing_item = GetPersonCalendarResponse200SickDaysCertificateMissingItem.from_dict(
                certificate_missing_item_data
            )

            certificate_missing.append(certificate_missing_item)

        certificate_available = []
        _certificate_available = d.pop("certificateAvailable")
        for certificate_available_item_data in _certificate_available:
            certificate_available_item = GetPersonCalendarResponse200SickDaysCertificateAvailableItem.from_dict(
                certificate_available_item_data
            )

            certificate_available.append(certificate_available_item)

        get_person_calendar_response_200_sick_days = cls(
            certificate_not_required=certificate_not_required,
            certificate_missing=certificate_missing,
            certificate_available=certificate_available,
        )

        return get_person_calendar_response_200_sick_days
