from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_bookings_response_200 import ListBookingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    person_id: int,
    date: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["personId"] = person_id

    params["date"] = date

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/bookings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListBookingsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListBookingsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListBookingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    person_id: int,
    date: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[ListBookingsResponse200]:
    """Bookings (alias of /persons/{id}/bookings)

    Args:
        person_id (int):
        date (str | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListBookingsResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        date=date,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    person_id: int,
    date: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> ListBookingsResponse200 | None:
    """Bookings (alias of /persons/{id}/bookings)

    Args:
        person_id (int):
        date (str | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListBookingsResponse200
    """

    return sync_detailed(
        client=client,
        person_id=person_id,
        date=date,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    person_id: int,
    date: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[ListBookingsResponse200]:
    """Bookings (alias of /persons/{id}/bookings)

    Args:
        person_id (int):
        date (str | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListBookingsResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        date=date,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    person_id: int,
    date: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> ListBookingsResponse200 | None:
    """Bookings (alias of /persons/{id}/bookings)

    Args:
        person_id (int):
        date (str | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListBookingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            person_id=person_id,
            date=date,
            from_=from_,
            to=to,
        )
    ).parsed
