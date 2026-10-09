from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_calculation_accounts_response_200 import ListCalculationAccountsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    *,
    date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["date"] = date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/persons/{person_id}/calculation-accounts".format(
            person_id=quote(str(person_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListCalculationAccountsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListCalculationAccountsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListCalculationAccountsResponse200]:
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
    date: str | Unset = UNSET,
) -> Response[ListCalculationAccountsResponse200]:
    """Calculation accounts of the person at a date

    Args:
        person_id (int):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCalculationAccountsResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
) -> ListCalculationAccountsResponse200 | None:
    """Calculation accounts of the person at a date

    Args:
        person_id (int):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCalculationAccountsResponse200
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        date=date,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
) -> Response[ListCalculationAccountsResponse200]:
    """Calculation accounts of the person at a date

    Args:
        person_id (int):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCalculationAccountsResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
) -> ListCalculationAccountsResponse200 | None:
    """Calculation accounts of the person at a date

    Args:
        person_id (int):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCalculationAccountsResponse200
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            date=date,
        )
    ).parsed
