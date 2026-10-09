from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    calculation_id: int,
    balance_id: int,
    *,
    month: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["month"] = month

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/persons/{person_id}/calculation-accounts/{calculation_id}/balances/{balance_id}".format(
            person_id=quote(str(person_id), safe=""),
            calculation_id=quote(str(calculation_id), safe=""),
            balance_id=quote(str(balance_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    calculation_id: int,
    balance_id: int,
    *,
    client: AuthenticatedClient | Client,
    month: str | Unset = UNSET,
) -> Response[Any]:
    """Delete a manual carry-over (timeCard user right 223 delete)

    Args:
        person_id (int):
        calculation_id (int):
        balance_id (int):
        month (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        calculation_id=calculation_id,
        balance_id=balance_id,
        month=month,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    person_id: int,
    calculation_id: int,
    balance_id: int,
    *,
    client: AuthenticatedClient | Client,
    month: str | Unset = UNSET,
) -> Response[Any]:
    """Delete a manual carry-over (timeCard user right 223 delete)

    Args:
        person_id (int):
        calculation_id (int):
        balance_id (int):
        month (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        calculation_id=calculation_id,
        balance_id=balance_id,
        month=month,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
