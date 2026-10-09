from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_carry_overs_response_200 import ListCarryOversResponse200
from ...types import UNSET, Response


def _get_kwargs(
    person_id: int,
    calculation_id: int,
    *,
    month: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["month"] = month

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/persons/{person_id}/calculation-accounts/{calculation_id}/balances".format(
            person_id=quote(str(person_id), safe=""),
            calculation_id=quote(str(calculation_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListCarryOversResponse200 | None:
    if response.status_code == 200:
        response_200 = ListCarryOversResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListCarryOversResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    calculation_id: int,
    *,
    client: AuthenticatedClient | Client,
    month: str,
) -> Response[ListCarryOversResponse200]:
    """Manual carry-overs of a month

    Args:
        person_id (int):
        calculation_id (int):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCarryOversResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        calculation_id=calculation_id,
        month=month,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    calculation_id: int,
    *,
    client: AuthenticatedClient | Client,
    month: str,
) -> ListCarryOversResponse200 | None:
    """Manual carry-overs of a month

    Args:
        person_id (int):
        calculation_id (int):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCarryOversResponse200
    """

    return sync_detailed(
        person_id=person_id,
        calculation_id=calculation_id,
        client=client,
        month=month,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    calculation_id: int,
    *,
    client: AuthenticatedClient | Client,
    month: str,
) -> Response[ListCarryOversResponse200]:
    """Manual carry-overs of a month

    Args:
        person_id (int):
        calculation_id (int):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCarryOversResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        calculation_id=calculation_id,
        month=month,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    calculation_id: int,
    *,
    client: AuthenticatedClient | Client,
    month: str,
) -> ListCarryOversResponse200 | None:
    """Manual carry-overs of a month

    Args:
        person_id (int):
        calculation_id (int):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCarryOversResponse200
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            calculation_id=calculation_id,
            client=client,
            month=month,
        )
    ).parsed
