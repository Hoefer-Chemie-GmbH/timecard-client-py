from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_booking_response_200 import GetBookingResponse200
from ...types import Response


def _get_kwargs(
    booking_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/bookings/{booking_id}".format(
            booking_id=quote(str(booking_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBookingResponse200 | None:
    if response.status_code == 200:
        response_200 = GetBookingResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBookingResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    booking_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBookingResponse200]:
    """Booking details (recorded bookings only; calculated breaks and system bookings return 404)

    Args:
        booking_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBookingResponse200]
    """

    kwargs = _get_kwargs(
        booking_id=booking_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    booking_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetBookingResponse200 | None:
    """Booking details (recorded bookings only; calculated breaks and system bookings return 404)

    Args:
        booking_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBookingResponse200
    """

    return sync_detailed(
        booking_id=booking_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    booking_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBookingResponse200]:
    """Booking details (recorded bookings only; calculated breaks and system bookings return 404)

    Args:
        booking_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBookingResponse200]
    """

    kwargs = _get_kwargs(
        booking_id=booking_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    booking_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetBookingResponse200 | None:
    """Booking details (recorded bookings only; calculated breaks and system bookings return 404)

    Args:
        booking_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBookingResponse200
    """

    return (
        await asyncio_detailed(
            booking_id=booking_id,
            client=client,
        )
    ).parsed
