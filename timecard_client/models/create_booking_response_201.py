from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_booking_response_201_booking_type_0 import CreateBookingResponse201BookingType0


T = TypeVar("T", bound="CreateBookingResponse201")


@_attrs_define
class CreateBookingResponse201:
    """
    Attributes:
        id (int | None):
        booking (CreateBookingResponse201BookingType0 | None):
    """

    id: int | None
    booking: CreateBookingResponse201BookingType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_booking_response_201_booking_type_0 import (
            CreateBookingResponse201BookingType0,  # noqa: PLC0415
        )

        id: int | None
        id = self.id

        booking: dict[str, Any] | None
        if isinstance(self.booking, CreateBookingResponse201BookingType0):
            booking = self.booking.to_dict()
        else:
            booking = self.booking

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "booking": booking,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_booking_response_201_booking_type_0 import (
            CreateBookingResponse201BookingType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        id = _parse_id(d.pop("id"))

        def _parse_booking(data: object) -> CreateBookingResponse201BookingType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                booking_type_0 = CreateBookingResponse201BookingType0.from_dict(data)

                return booking_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateBookingResponse201BookingType0 | None, data)

        booking = _parse_booking(d.pop("booking"))

        create_booking_response_201 = cls(
            id=id,
            booking=booking,
        )

        return create_booking_response_201
