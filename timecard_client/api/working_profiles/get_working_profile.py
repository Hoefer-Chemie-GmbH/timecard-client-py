from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_working_profile_response_200 import GetWorkingProfileResponse200
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    working_profile_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/working-profiles/{working_profile_id}".format(
            working_profile_id=quote(str(working_profile_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWorkingProfileResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetWorkingProfileResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Problem.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = Problem.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetWorkingProfileResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    working_profile_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetWorkingProfileResponse200 | Problem]:
    """Working time profile details

    Args:
        working_profile_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkingProfileResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        working_profile_id=working_profile_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    working_profile_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetWorkingProfileResponse200 | Problem | None:
    """Working time profile details

    Args:
        working_profile_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkingProfileResponse200 | Problem
    """

    return sync_detailed(
        working_profile_id=working_profile_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    working_profile_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetWorkingProfileResponse200 | Problem]:
    """Working time profile details

    Args:
        working_profile_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkingProfileResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        working_profile_id=working_profile_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    working_profile_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetWorkingProfileResponse200 | Problem | None:
    """Working time profile details

    Args:
        working_profile_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkingProfileResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            working_profile_id=working_profile_id,
            client=client,
        )
    ).parsed
