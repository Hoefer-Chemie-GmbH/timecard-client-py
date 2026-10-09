from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_working_profiles_response_200 import ListWorkingProfilesResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active_only: str | Unset = UNSET,
    correction_only: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["activeOnly"] = active_only

    params["correctionOnly"] = correction_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/working-profiles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListWorkingProfilesResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListWorkingProfilesResponse200.from_dict(response.json())

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
) -> Response[ListWorkingProfilesResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    active_only: str | Unset = UNSET,
    correction_only: str | Unset = UNSET,
) -> Response[ListWorkingProfilesResponse200 | Problem]:
    """Working time profiles

    Args:
        active_only (str | Unset):
        correction_only (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWorkingProfilesResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        active_only=active_only,
        correction_only=correction_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    active_only: str | Unset = UNSET,
    correction_only: str | Unset = UNSET,
) -> ListWorkingProfilesResponse200 | Problem | None:
    """Working time profiles

    Args:
        active_only (str | Unset):
        correction_only (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWorkingProfilesResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        active_only=active_only,
        correction_only=correction_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    active_only: str | Unset = UNSET,
    correction_only: str | Unset = UNSET,
) -> Response[ListWorkingProfilesResponse200 | Problem]:
    """Working time profiles

    Args:
        active_only (str | Unset):
        correction_only (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWorkingProfilesResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        active_only=active_only,
        correction_only=correction_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    active_only: str | Unset = UNSET,
    correction_only: str | Unset = UNSET,
) -> ListWorkingProfilesResponse200 | Problem | None:
    """Working time profiles

    Args:
        active_only (str | Unset):
        correction_only (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWorkingProfilesResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            active_only=active_only,
            correction_only=correction_only,
        )
    ).parsed
