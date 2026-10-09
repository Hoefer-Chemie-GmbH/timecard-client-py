from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_health_response_200 import GetHealthResponse200
from ...models.get_health_response_503 import GetHealthResponse503
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    deep: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["deep"] = deep

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/system/health",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetHealthResponse200 | GetHealthResponse503 | Problem | None:
    if response.status_code == 200:
        response_200 = GetHealthResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = GetHealthResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetHealthResponse200 | GetHealthResponse503 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    deep: str | Unset = UNSET,
) -> Response[GetHealthResponse200 | GetHealthResponse503 | Problem]:
    """Health check (no token required)

    Args:
        deep (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHealthResponse200 | GetHealthResponse503 | Problem]
    """

    kwargs = _get_kwargs(
        deep=deep,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    deep: str | Unset = UNSET,
) -> GetHealthResponse200 | GetHealthResponse503 | Problem | None:
    """Health check (no token required)

    Args:
        deep (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHealthResponse200 | GetHealthResponse503 | Problem
    """

    return sync_detailed(
        client=client,
        deep=deep,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    deep: str | Unset = UNSET,
) -> Response[GetHealthResponse200 | GetHealthResponse503 | Problem]:
    """Health check (no token required)

    Args:
        deep (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHealthResponse200 | GetHealthResponse503 | Problem]
    """

    kwargs = _get_kwargs(
        deep=deep,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    deep: str | Unset = UNSET,
) -> GetHealthResponse200 | GetHealthResponse503 | Problem | None:
    """Health check (no token required)

    Args:
        deep (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHealthResponse200 | GetHealthResponse503 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            deep=deep,
        )
    ).parsed
