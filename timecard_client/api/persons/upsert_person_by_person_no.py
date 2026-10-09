from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.upsert_person_by_person_no_body import UpsertPersonByPersonNoBody
from ...models.upsert_person_by_person_no_response_200 import UpsertPersonByPersonNoResponse200
from ...models.upsert_person_by_person_no_response_201 import UpsertPersonByPersonNoResponse201
from ...types import Response


def _get_kwargs(
    person_no: str,
    *,
    body: UpsertPersonByPersonNoBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/persons/by-person-no/{person_no}".format(
            person_no=quote(str(person_no), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201 | None:
    if response.status_code == 200:
        response_200 = UpsertPersonByPersonNoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = UpsertPersonByPersonNoResponse201.from_dict(response.json())

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
) -> Response[Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_no: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertPersonByPersonNoBody,
) -> Response[Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201]:
    """Create or update a person by personnel number (upsert for HR synchronisation)

    Args:
        person_no (str):
        body (UpsertPersonByPersonNoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201]
    """

    kwargs = _get_kwargs(
        person_no=person_no,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_no: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertPersonByPersonNoBody,
) -> Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201 | None:
    """Create or update a person by personnel number (upsert for HR synchronisation)

    Args:
        person_no (str):
        body (UpsertPersonByPersonNoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201
    """

    return sync_detailed(
        person_no=person_no,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    person_no: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertPersonByPersonNoBody,
) -> Response[Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201]:
    """Create or update a person by personnel number (upsert for HR synchronisation)

    Args:
        person_no (str):
        body (UpsertPersonByPersonNoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201]
    """

    kwargs = _get_kwargs(
        person_no=person_no,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_no: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertPersonByPersonNoBody,
) -> Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201 | None:
    """Create or update a person by personnel number (upsert for HR synchronisation)

    Args:
        person_no (str):
        body (UpsertPersonByPersonNoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpsertPersonByPersonNoResponse200 | UpsertPersonByPersonNoResponse201
    """

    return (
        await asyncio_detailed(
            person_no=person_no,
            client=client,
            body=body,
        )
    ).parsed
