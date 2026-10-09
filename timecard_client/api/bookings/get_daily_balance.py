from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_daily_balance_response_200 import GetDailyBalanceResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    *,
    date: str,
    month_overview: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["date"] = date

    params["monthOverview"] = month_overview

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/persons/{person_id}/daily-balance".format(
            person_id=quote(str(person_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDailyBalanceResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetDailyBalanceResponse200.from_dict(response.json())

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
) -> Response[GetDailyBalanceResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    date: str,
    month_overview: str | Unset = UNSET,
) -> Response[GetDailyBalanceResponse200 | Problem]:
    """Daily balance of a person

    Args:
        person_id (int):
        date (str):
        month_overview (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDailyBalanceResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        date=date,
        month_overview=month_overview,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    date: str,
    month_overview: str | Unset = UNSET,
) -> GetDailyBalanceResponse200 | Problem | None:
    """Daily balance of a person

    Args:
        person_id (int):
        date (str):
        month_overview (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDailyBalanceResponse200 | Problem
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        date=date,
        month_overview=month_overview,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    date: str,
    month_overview: str | Unset = UNSET,
) -> Response[GetDailyBalanceResponse200 | Problem]:
    """Daily balance of a person

    Args:
        person_id (int):
        date (str):
        month_overview (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDailyBalanceResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        date=date,
        month_overview=month_overview,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    date: str,
    month_overview: str | Unset = UNSET,
) -> GetDailyBalanceResponse200 | Problem | None:
    """Daily balance of a person

    Args:
        person_id (int):
        date (str):
        month_overview (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDailyBalanceResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            date=date,
            month_overview=month_overview,
        )
    ).parsed
