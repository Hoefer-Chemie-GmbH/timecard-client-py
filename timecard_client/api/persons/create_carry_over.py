from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_carry_over_body import CreateCarryOverBody
from ...models.create_carry_over_response_201 import CreateCarryOverResponse201
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
) -> CreateCarryOverResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateCarryOverResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateCarryOverResponse201]:
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
) -> Response[CreateCarryOverResponse201]:
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
        Response[CreateCarryOverResponse201]
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
) -> CreateCarryOverResponse201 | None:
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
        CreateCarryOverResponse201
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
) -> Response[CreateCarryOverResponse201]:
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
        Response[CreateCarryOverResponse201]
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
) -> CreateCarryOverResponse201 | None:
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
        CreateCarryOverResponse201
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
