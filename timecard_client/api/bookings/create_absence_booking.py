from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_absence_booking_body import CreateAbsenceBookingBody
from ...models.create_absence_booking_response_201 import CreateAbsenceBookingResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateAbsenceBookingBody,
    calculate: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["calculate"] = calculate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/absence-bookings",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAbsenceBookingResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateAbsenceBookingResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAbsenceBookingResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAbsenceBookingBody,
    calculate: str | Unset = UNSET,
) -> Response[CreateAbsenceBookingResponse201]:
    """Book an absence for a period (one or more persons); timeCard returns no booking id, the day list
    shows the booking as ABSENCE

    Args:
        calculate (str | Unset):
        body (CreateAbsenceBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAbsenceBookingResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
        calculate=calculate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAbsenceBookingBody,
    calculate: str | Unset = UNSET,
) -> CreateAbsenceBookingResponse201 | None:
    """Book an absence for a period (one or more persons); timeCard returns no booking id, the day list
    shows the booking as ABSENCE

    Args:
        calculate (str | Unset):
        body (CreateAbsenceBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAbsenceBookingResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        calculate=calculate,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAbsenceBookingBody,
    calculate: str | Unset = UNSET,
) -> Response[CreateAbsenceBookingResponse201]:
    """Book an absence for a period (one or more persons); timeCard returns no booking id, the day list
    shows the booking as ABSENCE

    Args:
        calculate (str | Unset):
        body (CreateAbsenceBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAbsenceBookingResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
        calculate=calculate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAbsenceBookingBody,
    calculate: str | Unset = UNSET,
) -> CreateAbsenceBookingResponse201 | None:
    """Book an absence for a period (one or more persons); timeCard returns no booking id, the day list
    shows the booking as ABSENCE

    Args:
        calculate (str | Unset):
        body (CreateAbsenceBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAbsenceBookingResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            calculate=calculate,
        )
    ).parsed
