from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_audit_events_action import ListAuditEventsAction
from ...models.list_audit_events_format import ListAuditEventsFormat
from ...models.list_audit_events_outcome import ListAuditEventsOutcome
from ...models.list_audit_events_response_200 import ListAuditEventsResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: Any | Unset = UNSET,
    to: Any | Unset = UNSET,
    subject: str | Unset = UNSET,
    issuer_name: str | Unset = UNSET,
    action: ListAuditEventsAction | Unset = UNSET,
    outcome: ListAuditEventsOutcome | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    format_: ListAuditEventsFormat | Unset = ListAuditEventsFormat.JSON,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["subject"] = subject

    params["issuerName"] = issuer_name

    json_action: str | Unset = UNSET
    if not isinstance(action, Unset):
        json_action = action.value

    params["action"] = json_action

    json_outcome: str | Unset = UNSET
    if not isinstance(outcome, Unset):
        json_outcome = outcome.value

    params["outcome"] = json_outcome

    params["resourceType"] = resource_type

    params["resourceId"] = resource_id

    params["personId"] = person_id

    params["requestId"] = request_id

    params["page"] = page

    params["pageSize"] = page_size

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audit-events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListAuditEventsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListAuditEventsResponse200.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListAuditEventsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: Any | Unset = UNSET,
    to: Any | Unset = UNSET,
    subject: str | Unset = UNSET,
    issuer_name: str | Unset = UNSET,
    action: ListAuditEventsAction | Unset = UNSET,
    outcome: ListAuditEventsOutcome | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    format_: ListAuditEventsFormat | Unset = ListAuditEventsFormat.JSON,
) -> Response[ListAuditEventsResponse200 | Problem]:
    """Query audit events (JSON or CSV)

    Args:
        from_ (Any | Unset):
        to (Any | Unset):
        subject (str | Unset):
        issuer_name (str | Unset):
        action (ListAuditEventsAction | Unset):
        outcome (ListAuditEventsOutcome | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        person_id (int | Unset):
        request_id (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        format_ (ListAuditEventsFormat | Unset):  Default: ListAuditEventsFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAuditEventsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        subject=subject,
        issuer_name=issuer_name,
        action=action,
        outcome=outcome,
        resource_type=resource_type,
        resource_id=resource_id,
        person_id=person_id,
        request_id=request_id,
        page=page,
        page_size=page_size,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: Any | Unset = UNSET,
    to: Any | Unset = UNSET,
    subject: str | Unset = UNSET,
    issuer_name: str | Unset = UNSET,
    action: ListAuditEventsAction | Unset = UNSET,
    outcome: ListAuditEventsOutcome | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    format_: ListAuditEventsFormat | Unset = ListAuditEventsFormat.JSON,
) -> ListAuditEventsResponse200 | Problem | None:
    """Query audit events (JSON or CSV)

    Args:
        from_ (Any | Unset):
        to (Any | Unset):
        subject (str | Unset):
        issuer_name (str | Unset):
        action (ListAuditEventsAction | Unset):
        outcome (ListAuditEventsOutcome | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        person_id (int | Unset):
        request_id (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        format_ (ListAuditEventsFormat | Unset):  Default: ListAuditEventsFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAuditEventsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        subject=subject,
        issuer_name=issuer_name,
        action=action,
        outcome=outcome,
        resource_type=resource_type,
        resource_id=resource_id,
        person_id=person_id,
        request_id=request_id,
        page=page,
        page_size=page_size,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: Any | Unset = UNSET,
    to: Any | Unset = UNSET,
    subject: str | Unset = UNSET,
    issuer_name: str | Unset = UNSET,
    action: ListAuditEventsAction | Unset = UNSET,
    outcome: ListAuditEventsOutcome | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    format_: ListAuditEventsFormat | Unset = ListAuditEventsFormat.JSON,
) -> Response[ListAuditEventsResponse200 | Problem]:
    """Query audit events (JSON or CSV)

    Args:
        from_ (Any | Unset):
        to (Any | Unset):
        subject (str | Unset):
        issuer_name (str | Unset):
        action (ListAuditEventsAction | Unset):
        outcome (ListAuditEventsOutcome | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        person_id (int | Unset):
        request_id (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        format_ (ListAuditEventsFormat | Unset):  Default: ListAuditEventsFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAuditEventsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        subject=subject,
        issuer_name=issuer_name,
        action=action,
        outcome=outcome,
        resource_type=resource_type,
        resource_id=resource_id,
        person_id=person_id,
        request_id=request_id,
        page=page,
        page_size=page_size,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: Any | Unset = UNSET,
    to: Any | Unset = UNSET,
    subject: str | Unset = UNSET,
    issuer_name: str | Unset = UNSET,
    action: ListAuditEventsAction | Unset = UNSET,
    outcome: ListAuditEventsOutcome | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    request_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    format_: ListAuditEventsFormat | Unset = ListAuditEventsFormat.JSON,
) -> ListAuditEventsResponse200 | Problem | None:
    """Query audit events (JSON or CSV)

    Args:
        from_ (Any | Unset):
        to (Any | Unset):
        subject (str | Unset):
        issuer_name (str | Unset):
        action (ListAuditEventsAction | Unset):
        outcome (ListAuditEventsOutcome | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        person_id (int | Unset):
        request_id (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        format_ (ListAuditEventsFormat | Unset):  Default: ListAuditEventsFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAuditEventsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            subject=subject,
            issuer_name=issuer_name,
            action=action,
            outcome=outcome,
            resource_type=resource_type,
            resource_id=resource_id,
            person_id=person_id,
            request_id=request_id,
            page=page,
            page_size=page_size,
            format_=format_,
        )
    ).parsed
