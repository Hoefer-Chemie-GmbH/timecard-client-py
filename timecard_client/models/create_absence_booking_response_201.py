from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateAbsenceBookingResponse201")


@_attrs_define
class CreateAbsenceBookingResponse201:
    """
    Attributes:
        person_ids (list[int]):
        absence_type_id (int):
        from_ (str):
        to (str):
        booking_id (int | None):
    """

    person_ids: list[int]
    absence_type_id: int
    from_: str
    to: str
    booking_id: int | None

    def to_dict(self) -> dict[str, Any]:
        person_ids = self.person_ids

        absence_type_id = self.absence_type_id

        from_ = self.from_

        to = self.to

        booking_id: int | None
        booking_id = self.booking_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personIds": person_ids,
                "absenceTypeId": absence_type_id,
                "from": from_,
                "to": to,
                "bookingId": booking_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_ids = cast(list[int], d.pop("personIds"))

        absence_type_id = d.pop("absenceTypeId")

        from_ = d.pop("from")

        to = d.pop("to")

        def _parse_booking_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        booking_id = _parse_booking_id(d.pop("bookingId"))

        create_absence_booking_response_201 = cls(
            person_ids=person_ids,
            absence_type_id=absence_type_id,
            from_=from_,
            to=to,
            booking_id=booking_id,
        )

        return create_absence_booking_response_201
