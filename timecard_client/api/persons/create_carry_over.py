from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_carry_over_body import CreateCarryOverBody
from ...models.create_carry_over_response_201 import CreateCarryOverResponse201
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    calculation_id: int,
    *,
    body: CreateCarryOverBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/persons/{person_id}/calculation-accounts/{calculation_id}/balances".format(
            person_id=quote(str(person_id), safe=""),
            calculation_id=quote(str(calculation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateCarryOverResponse201 | Problem | None:
    if response.status_code == 201:
        response_201 = CreateCarryOverResponse201.from_dict(response.json())

        return response_201

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
) -> Response[CreateCarryOverResponse201 | Problem]:
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
    body: CreateCarryOverBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateCarryOverResponse201 | Problem]:
    """Create a manual carry-over (timeCard user right 223 create)

    Args:
        person_id (int):
        calculation_id (int):
        idempotency_key (str | Unset):
        body (CreateCarryOverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCarryOverResponse201 | Problem]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        calculation_id=calculation_id,
        body=body,
        idempotency_key=idempotency_key,
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
    body: CreateCarryOverBody,
    idempotency_key: str | Unset = UNSET,
) -> CreateCarryOverResponse201 | Problem | None:
    """Create a manual carry-over (timeCard user right 223 create)

    Args:
        person_id (int):
        calculation_id (int):
        idempotency_key (str | Unset):
        body (CreateCarryOverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCarryOverResponse201 | Problem
    """

    return sync_detailed(
        person_id=person_id,
        calculation_id=calculation_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    calculation_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateCarryOverBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateCarryOverResponse201 | Problem]:
    """Create a manual carry-over (timeCard user right 223 create)

    Args:
        person_id (int):
        calculation_id (int):
        idempotency_key (str | Unset):
        body (CreateCarryOverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCarryOverResponse201 | Problem]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        calculation_id=calculation_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    calculation_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateCarryOverBody,
    idempotency_key: str | Unset = UNSET,
) -> CreateCarryOverResponse201 | Problem | None:
    """Create a manual carry-over (timeCard user right 223 create)

    Args:
        person_id (int):
        calculation_id (int):
        idempotency_key (str | Unset):
        body (CreateCarryOverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCarryOverResponse201 | Problem
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            calculation_id=calculation_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
