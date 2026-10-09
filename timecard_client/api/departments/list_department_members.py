from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_department_members_response_200 import ListDepartmentMembersResponse200
from ...types import Response


def _get_kwargs(
    department_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/departments/{department_id}/members".format(
            department_id=quote(str(department_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListDepartmentMembersResponse200 | None:
    if response.status_code == 200:
        response_200 = ListDepartmentMembersResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListDepartmentMembersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    department_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListDepartmentMembersResponse200]:
    """Members as of today (without the leader unless the leader is a member)

    Args:
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDepartmentMembersResponse200]
    """

    kwargs = _get_kwargs(
        department_id=department_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    department_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ListDepartmentMembersResponse200 | None:
    """Members as of today (without the leader unless the leader is a member)

    Args:
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDepartmentMembersResponse200
    """

    return sync_detailed(
        department_id=department_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    department_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListDepartmentMembersResponse200]:
    """Members as of today (without the leader unless the leader is a member)

    Args:
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDepartmentMembersResponse200]
    """

    kwargs = _get_kwargs(
        department_id=department_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    department_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ListDepartmentMembersResponse200 | None:
    """Members as of today (without the leader unless the leader is a member)

    Args:
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDepartmentMembersResponse200
    """

    return (
        await asyncio_detailed(
            department_id=department_id,
            client=client,
        )
    ).parsed
