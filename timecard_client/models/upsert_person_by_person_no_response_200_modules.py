from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpsertPersonByPersonNoResponse200Modules")


@_attrs_define
class UpsertPersonByPersonNoResponse200Modules:
    """
    Attributes:
        au (bool):
        lohn (bool):
        exch_sync_calendar (bool):
        exch_sync_auto_responder (bool):
    """

    au: bool
    lohn: bool
    exch_sync_calendar: bool
    exch_sync_auto_responder: bool

    def to_dict(self) -> dict[str, Any]:
        au = self.au

        lohn = self.lohn

        exch_sync_calendar = self.exch_sync_calendar

        exch_sync_auto_responder = self.exch_sync_auto_responder

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "au": au,
                "lohn": lohn,
                "exchSyncCalendar": exch_sync_calendar,
                "exchSyncAutoResponder": exch_sync_auto_responder,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        au = d.pop("au")

        lohn = d.pop("lohn")

        exch_sync_calendar = d.pop("exchSyncCalendar")

        exch_sync_auto_responder = d.pop("exchSyncAutoResponder")

        upsert_person_by_person_no_response_200_modules = cls(
            au=au,
            lohn=lohn,
            exch_sync_calendar=exch_sync_calendar,
            exch_sync_auto_responder=exch_sync_auto_responder,
        )

        return upsert_person_by_person_no_response_200_modules
