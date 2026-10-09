from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.replace_carry_over_body import ReplaceCarryOverBody
from ...models.replace_carry_over_response_200 import ReplaceCarryOverResponse200
from ...types import Response


def _get_kwargs(
    person_id: int,
    calculation_id: int,
    balance_id: int,
    *,
    body: ReplaceCarryOverBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/persons/{person_id}/calculation-accounts/{calculation_id}/balances/{balance_id}".format(
            person_id=quote(str(person_id), safe=""),
            calculation_id=quote(str(calculation_id), safe=""),
            balance_id=quote(str(balance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | ReplaceCarryOverResponse200 | None:
    if response.status_code == 200:
        response_200 = ReplaceCarryOverResponse200.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

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
) -> Response[Problem | ReplaceCarryOverResponse200]:
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
    body: ReplaceCarryOverBody,
) -> Response[Problem | ReplaceCarryOverResponse200]:
    """Replace a manual carry-over (the carry-over must exist in the month of balanceDate)

    Args:
        person_id (int):
        calculation_id (int):
        balance_id (int):
        body (ReplaceCarryOverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | ReplaceCarryOverResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        calculation_id=calculation_id,
        balance_id=balance_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    calculation_id: int,
    balance_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ReplaceCarryOverBody,
) -> Problem | ReplaceCarryOverResponse200 | None:
    """Replace a manual carry-over (the carry-over must exist in the month of balanceDate)

    Args:
        person_id (int):
        calculation_id (int):
        balance_id (int):
        body (ReplaceCarryOverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | ReplaceCarryOverResponse200
    """

    return sync_detailed(
        person_id=person_id,
        calculation_id=calculation_id,
        balance_id=balance_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    calculation_id: int,
    balance_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ReplaceCarryOverBody,
) -> Response[Problem | ReplaceCarryOverResponse200]:
    """Replace a manual carry-over (the carry-over must exist in the month of balanceDate)

    Args:
        person_id (int):
        calculation_id (int):
        balance_id (int):
        body (ReplaceCarryOverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | ReplaceCarryOverResponse200]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        calculation_id=calculation_id,
        balance_id=balance_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    calculation_id: int,
    balance_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ReplaceCarryOverBody,
) -> Problem | ReplaceCarryOverResponse200 | None:
    """Replace a manual carry-over (the carry-over must exist in the month of balanceDate)

    Args:
        person_id (int):
        calculation_id (int):
        balance_id (int):
        body (ReplaceCarryOverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | ReplaceCarryOverResponse200
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            calculation_id=calculation_id,
            balance_id=balance_id,
            client=client,
            body=body,
        )
    ).parsed
