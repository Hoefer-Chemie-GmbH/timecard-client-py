from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_work_operation_body import UpdateWorkOperationBody
from ...models.update_work_operation_response_200 import UpdateWorkOperationResponse200
from ...types import Response


def _get_kwargs(
    work_operation_id: int,
    *,
    body: UpdateWorkOperationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/work-operations/{work_operation_id}".format(
            work_operation_id=quote(str(work_operation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateWorkOperationResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateWorkOperationResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateWorkOperationResponse200]:
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
    body: UpdateWorkOperationBody,
) -> Response[UpdateWorkOperationResponse200]:
    """Change a work operation (read-modify-write, timeCard user right 213 update)

    Args:
        work_operation_id (int):
        body (UpdateWorkOperationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWorkOperationResponse200]
    """

    kwargs = _get_kwargs(
        work_operation_id=work_operation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_operation_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWorkOperationBody,
) -> UpdateWorkOperationResponse200 | None:
    """Change a work operation (read-modify-write, timeCard user right 213 update)

    Args:
        work_operation_id (int):
        body (UpdateWorkOperationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWorkOperationResponse200
    """

    return sync_detailed(
        work_operation_id=work_operation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    work_operation_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWorkOperationBody,
) -> Response[UpdateWorkOperationResponse200]:
    """Change a work operation (read-modify-write, timeCard user right 213 update)

    Args:
        work_operation_id (int):
        body (UpdateWorkOperationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWorkOperationResponse200]
    """

    kwargs = _get_kwargs(
        work_operation_id=work_operation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_operation_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWorkOperationBody,
) -> UpdateWorkOperationResponse200 | None:
    """Change a work operation (read-modify-write, timeCard user right 213 update)

    Args:
        work_operation_id (int):
        body (UpdateWorkOperationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWorkOperationResponse200
    """

    return (
        await asyncio_detailed(
            work_operation_id=work_operation_id,
            client=client,
            body=body,
        )
    ).parsed
