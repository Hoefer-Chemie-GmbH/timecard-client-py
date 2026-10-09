from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_absence_type_response_200 import GetAbsenceTypeResponse200
from ...types import Response


def _get_kwargs(
    absence_type_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/absence-types/{absence_type_id}".format(
            absence_type_id=quote(str(absence_type_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAbsenceTypeResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAbsenceTypeResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAbsenceTypeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    absence_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAbsenceTypeResponse200]:
    """Absence type details

    Args:
        absence_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAbsenceTypeResponse200]
    """

    kwargs = _get_kwargs(
        absence_type_id=absence_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    absence_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetAbsenceTypeResponse200 | None:
    """Absence type details

    Args:
        absence_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAbsenceTypeResponse200
    """

    return sync_detailed(
        absence_type_id=absence_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    absence_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAbsenceTypeResponse200]:
    """Absence type details

    Args:
        absence_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAbsenceTypeResponse200]
    """

    kwargs = _get_kwargs(
        absence_type_id=absence_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    absence_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetAbsenceTypeResponse200 | None:
    """Absence type details

    Args:
        absence_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAbsenceTypeResponse200
    """

    return (
        await asyncio_detailed(
            absence_type_id=absence_type_id,
            client=client,
        )
    ).parsed
