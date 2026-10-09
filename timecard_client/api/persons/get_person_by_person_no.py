from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_person_by_person_no_response_200 import GetPersonByPersonNoResponse200
from ...types import Response


def _get_kwargs(
    person_no: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/persons/by-person-no/{person_no}".format(
            person_no=quote(str(person_no), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPersonByPersonNoResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPersonByPersonNoResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPersonByPersonNoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_no: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPersonByPersonNoResponse200]:
    """Read a person by personnel number

    Args:
        person_no (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPersonByPersonNoResponse200]
    """

    kwargs = _get_kwargs(
        person_no=person_no,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_no: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPersonByPersonNoResponse200 | None:
    """Read a person by personnel number

    Args:
        person_no (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPersonByPersonNoResponse200
    """

    return sync_detailed(
        person_no=person_no,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_no: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPersonByPersonNoResponse200]:
    """Read a person by personnel number

    Args:
        person_no (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPersonByPersonNoResponse200]
    """

    kwargs = _get_kwargs(
        person_no=person_no,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_no: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPersonByPersonNoResponse200 | None:
    """Read a person by personnel number

    Args:
        person_no (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPersonByPersonNoResponse200
    """

    return (
        await asyncio_detailed(
            person_no=person_no,
            client=client,
        )
    ).parsed
