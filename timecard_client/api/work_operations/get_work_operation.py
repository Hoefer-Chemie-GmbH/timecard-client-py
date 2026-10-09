from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_work_operation_response_200 import GetWorkOperationResponse200
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    work_operation_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/work-operations/{work_operation_id}".format(
            work_operation_id=quote(str(work_operation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWorkOperationResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetWorkOperationResponse200.from_dict(response.json())

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
) -> Response[GetWorkOperationResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    work_operation_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetWorkOperationResponse200 | Problem]:
    """Work operation details

    Args:
        work_operation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkOperationResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        work_operation_id=work_operation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_operation_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetWorkOperationResponse200 | Problem | None:
    """Work operation details

    Args:
        work_operation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkOperationResponse200 | Problem
    """

    return sync_detailed(
        work_operation_id=work_operation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    work_operation_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetWorkOperationResponse200 | Problem]:
    """Work operation details

    Args:
        work_operation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkOperationResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        work_operation_id=work_operation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_operation_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetWorkOperationResponse200 | Problem | None:
    """Work operation details

    Args:
        work_operation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkOperationResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            work_operation_id=work_operation_id,
            client=client,
        )
    ).parsed
