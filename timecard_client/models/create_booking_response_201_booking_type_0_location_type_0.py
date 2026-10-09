from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateBookingResponse201BookingType0LocationType0")


@_attrs_define
class CreateBookingResponse201BookingType0LocationType0:
    """
    Attributes:
        latitude (float):
        longitude (float):
        accuracy (float):
        link (None | str):
    """

    latitude: float
    longitude: float
    accuracy: float
    link: None | str

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        accuracy = self.accuracy

        link: None | str
        link = self.link

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
                "accuracy": accuracy,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        accuracy = d.pop("accuracy")

        def _parse_link(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        link = _parse_link(d.pop("link"))

        create_booking_response_201_booking_type_0_location_type_0 = cls(
            latitude=latitude,
            longitude=longitude,
            accuracy=accuracy,
            link=link,
        )

        return create_booking_response_201_booking_type_0_location_type_0
