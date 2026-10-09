from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_absence_types_response_200 import ListAbsenceTypesResponse200
from ...models.list_absence_types_usage import ListAbsenceTypesUsage
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    usage: ListAbsenceTypesUsage | Unset = ListAbsenceTypesUsage.ALL,
    person_id: int | Unset = UNSET,
    date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_usage: str | Unset = UNSET
    if not isinstance(usage, Unset):
        json_usage = usage.value

    params["usage"] = json_usage

    params["personId"] = person_id

    params["date"] = date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/absence-types",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListAbsenceTypesResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListAbsenceTypesResponse200.from_dict(response.json())

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
) -> Response[ListAbsenceTypesResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    usage: ListAbsenceTypesUsage | Unset = ListAbsenceTypesUsage.ALL,
    person_id: int | Unset = UNSET,
    date: str | Unset = UNSET,
) -> Response[ListAbsenceTypesResponse200 | Problem]:
    """Absence types

    Args:
        usage (ListAbsenceTypesUsage | Unset):  Default: ListAbsenceTypesUsage.ALL.
        person_id (int | Unset):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAbsenceTypesResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        usage=usage,
        person_id=person_id,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    usage: ListAbsenceTypesUsage | Unset = ListAbsenceTypesUsage.ALL,
    person_id: int | Unset = UNSET,
    date: str | Unset = UNSET,
) -> ListAbsenceTypesResponse200 | Problem | None:
    """Absence types

    Args:
        usage (ListAbsenceTypesUsage | Unset):  Default: ListAbsenceTypesUsage.ALL.
        person_id (int | Unset):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAbsenceTypesResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        usage=usage,
        person_id=person_id,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    usage: ListAbsenceTypesUsage | Unset = ListAbsenceTypesUsage.ALL,
    person_id: int | Unset = UNSET,
    date: str | Unset = UNSET,
) -> Response[ListAbsenceTypesResponse200 | Problem]:
    """Absence types

    Args:
        usage (ListAbsenceTypesUsage | Unset):  Default: ListAbsenceTypesUsage.ALL.
        person_id (int | Unset):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAbsenceTypesResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        usage=usage,
        person_id=person_id,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    usage: ListAbsenceTypesUsage | Unset = ListAbsenceTypesUsage.ALL,
    person_id: int | Unset = UNSET,
    date: str | Unset = UNSET,
) -> ListAbsenceTypesResponse200 | Problem | None:
    """Absence types

    Args:
        usage (ListAbsenceTypesUsage | Unset):  Default: ListAbsenceTypesUsage.ALL.
        person_id (int | Unset):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAbsenceTypesResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            usage=usage,
            person_id=person_id,
            date=date,
        )
    ).parsed
