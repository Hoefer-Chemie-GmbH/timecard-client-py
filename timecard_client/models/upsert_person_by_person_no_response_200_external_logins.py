from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpsertPersonByPersonNoResponse200ExternalLogins")


@_attrs_define
class UpsertPersonByPersonNoResponse200ExternalLogins:
    """
    Attributes:
        domain_user_name (None | str):
        entra_user_name (None | str):
    """

    domain_user_name: None | str
    entra_user_name: None | str

    def to_dict(self) -> dict[str, Any]:
        domain_user_name: None | str
        domain_user_name = self.domain_user_name

        entra_user_name: None | str
        entra_user_name = self.entra_user_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domainUserName": domain_user_name,
                "entraUserName": entra_user_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_domain_user_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_user_name = _parse_domain_user_name(d.pop("domainUserName"))

        def _parse_entra_user_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        entra_user_name = _parse_entra_user_name(d.pop("entraUserName"))

        upsert_person_by_person_no_response_200_external_logins = cls(
            domain_user_name=domain_user_name,
            entra_user_name=entra_user_name,
        )

        return upsert_person_by_person_no_response_200_external_logins
