from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_break_rule_response_200 import GetBreakRuleResponse200
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    break_rule_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/break-rules/{break_rule_id}".format(
            break_rule_id=quote(str(break_rule_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBreakRuleResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetBreakRuleResponse200.from_dict(response.json())

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
) -> Response[GetBreakRuleResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    break_rule_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBreakRuleResponse200 | Problem]:
    """Break rule details

    Args:
        break_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBreakRuleResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        break_rule_id=break_rule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    break_rule_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetBreakRuleResponse200 | Problem | None:
    """Break rule details

    Args:
        break_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBreakRuleResponse200 | Problem
    """

    return sync_detailed(
        break_rule_id=break_rule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    break_rule_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBreakRuleResponse200 | Problem]:
    """Break rule details

    Args:
        break_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBreakRuleResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        break_rule_id=break_rule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    break_rule_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetBreakRuleResponse200 | Problem | None:
    """Break rule details

    Args:
        break_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBreakRuleResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            break_rule_id=break_rule_id,
            client=client,
        )
    ).parsed
