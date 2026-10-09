from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_booking_body import CreateBookingBody
from ...models.create_booking_response_201 import CreateBookingResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateBookingBody,
    calculate: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["calculate"] = calculate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/bookings",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateBookingResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateBookingResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateBookingResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBookingBody,
    calculate: str | Unset = UNSET,
) -> Response[CreateBookingResponse201]:
    """Create a time or project booking

    Args:
        calculate (str | Unset):
        body (CreateBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBookingResponse201]
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
    body: CreateBookingBody,
    calculate: str | Unset = UNSET,
) -> CreateBookingResponse201 | None:
    """Create a time or project booking

    Args:
        calculate (str | Unset):
        body (CreateBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBookingResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        calculate=calculate,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBookingBody,
    calculate: str | Unset = UNSET,
) -> Response[CreateBookingResponse201]:
    """Create a time or project booking

    Args:
        calculate (str | Unset):
        body (CreateBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBookingResponse201]
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
    body: CreateBookingBody,
    calculate: str | Unset = UNSET,
) -> CreateBookingResponse201 | None:
    """Create a time or project booking

    Args:
        calculate (str | Unset):
        body (CreateBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBookingResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            calculate=calculate,
        )
    ).parsed
