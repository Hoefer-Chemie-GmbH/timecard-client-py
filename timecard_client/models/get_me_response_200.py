from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetMeResponse200")


@_attrs_define
class GetMeResponse200:
    """
    Attributes:
        issuer_name (str):
        issuer (str):
        subject (str):
        display_name (str):
        scopes (list[str]):
        token_expires_at (str):
    """

    issuer_name: str
    issuer: str
    subject: str
    display_name: str
    scopes: list[str]
    token_expires_at: str

    def to_dict(self) -> dict[str, Any]:
        issuer_name = self.issuer_name

        issuer = self.issuer

        subject = self.subject

        display_name = self.display_name

        scopes = self.scopes

        token_expires_at = self.token_expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "issuerName": issuer_name,
                "issuer": issuer,
                "subject": subject,
                "displayName": display_name,
                "scopes": scopes,
                "tokenExpiresAt": token_expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issuer_name = d.pop("issuerName")

        issuer = d.pop("issuer")

        subject = d.pop("subject")

        display_name = d.pop("displayName")

        scopes = cast(list[str], d.pop("scopes"))

        token_expires_at = d.pop("tokenExpiresAt")

        get_me_response_200 = cls(
            issuer_name=issuer_name,
            issuer=issuer,
            subject=subject,
            display_name=display_name,
            scopes=scopes,
            token_expires_at=token_expires_at,
        )

        return get_me_response_200
