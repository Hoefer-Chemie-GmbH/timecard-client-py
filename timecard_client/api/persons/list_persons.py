from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_persons_response_200 import ListPersonsResponse200
from ...models.list_persons_state import ListPersonsState
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    state: ListPersonsState | Unset = UNSET,
    department: str | Unset = UNSET,
    person_no: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_admin: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["department"] = department

    params["personNo"] = person_no

    params["search"] = search

    params["includeAdmin"] = include_admin

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/persons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListPersonsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListPersonsResponse200.from_dict(response.json())

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
) -> Response[ListPersonsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    state: ListPersonsState | Unset = UNSET,
    department: str | Unset = UNSET,
    person_no: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_admin: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
) -> Response[ListPersonsResponse200 | Problem]:
    """List persons

    Args:
        state (ListPersonsState | Unset):
        department (str | Unset):
        person_no (str | Unset):
        search (str | Unset):
        include_admin (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPersonsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        state=state,
        department=department,
        person_no=person_no,
        search=search,
        include_admin=include_admin,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    state: ListPersonsState | Unset = UNSET,
    department: str | Unset = UNSET,
    person_no: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_admin: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
) -> ListPersonsResponse200 | Problem | None:
    """List persons

    Args:
        state (ListPersonsState | Unset):
        department (str | Unset):
        person_no (str | Unset):
        search (str | Unset):
        include_admin (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPersonsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        state=state,
        department=department,
        person_no=person_no,
        search=search,
        include_admin=include_admin,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    state: ListPersonsState | Unset = UNSET,
    department: str | Unset = UNSET,
    person_no: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_admin: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
) -> Response[ListPersonsResponse200 | Problem]:
    """List persons

    Args:
        state (ListPersonsState | Unset):
        department (str | Unset):
        person_no (str | Unset):
        search (str | Unset):
        include_admin (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPersonsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        state=state,
        department=department,
        person_no=person_no,
        search=search,
        include_admin=include_admin,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    state: ListPersonsState | Unset = UNSET,
    department: str | Unset = UNSET,
    person_no: str | Unset = UNSET,
    search: str | Unset = UNSET,
    include_admin: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
) -> ListPersonsResponse200 | Problem | None:
    """List persons

    Args:
        state (ListPersonsState | Unset):
        department (str | Unset):
        person_no (str | Unset):
        search (str | Unset):
        include_admin (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPersonsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            state=state,
            department=department,
            person_no=person_no,
            search=search,
            include_admin=include_admin,
            page=page,
            page_size=page_size,
        )
    ).parsed
