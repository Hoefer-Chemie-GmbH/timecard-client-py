from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_free_field_response_200 import GetFreeFieldResponse200
from ...types import Response


def _get_kwargs(
    free_field_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/free-fields/{free_field_id}".format(
            free_field_id=quote(str(free_field_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetFreeFieldResponse200 | None:
    if response.status_code == 200:
        response_200 = GetFreeFieldResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetFreeFieldResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    free_field_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetFreeFieldResponse200]:
    """Free field details

    Args:
        free_field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFreeFieldResponse200]
    """

    kwargs = _get_kwargs(
        free_field_id=free_field_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    free_field_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetFreeFieldResponse200 | None:
    """Free field details

    Args:
        free_field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFreeFieldResponse200
    """

    return sync_detailed(
        free_field_id=free_field_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    free_field_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetFreeFieldResponse200]:
    """Free field details

    Args:
        free_field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFreeFieldResponse200]
    """

    kwargs = _get_kwargs(
        free_field_id=free_field_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    free_field_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetFreeFieldResponse200 | None:
    """Free field details

    Args:
        free_field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFreeFieldResponse200
    """

    return (
        await asyncio_detailed(
            free_field_id=free_field_id,
            client=client,
        )
    ).parsed
