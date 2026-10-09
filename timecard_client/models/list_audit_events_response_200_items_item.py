from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_audit_events_response_200_items_item_action import ListAuditEventsResponse200ItemsItemAction
from ..models.list_audit_events_response_200_items_item_outcome import ListAuditEventsResponse200ItemsItemOutcome

if TYPE_CHECKING:
    from ..models.list_audit_events_response_200_items_item_query import ListAuditEventsResponse200ItemsItemQuery
    from ..models.list_audit_events_response_200_items_item_upstream_calls_item import (
        ListAuditEventsResponse200ItemsItemUpstreamCallsItem,
    )


T = TypeVar("T", bound="ListAuditEventsResponse200ItemsItem")


@_attrs_define
class ListAuditEventsResponse200ItemsItem:
    """
    Attributes:
        event_id (str):
        request_id (str):
        occurred_at (str):
        duration_ms (int):
        issuer_name (str):
        issuer (None | str):
        subject (str):
        principal_name (None | str):
        token_id (None | str):
        acting_user (None | str):
        source_ip (None | str):
        user_agent (None | str):
        method (str):
        route (None | str):
        path (str):
        query (ListAuditEventsResponse200ItemsItemQuery):
        action (ListAuditEventsResponse200ItemsItemAction):
        resource_type (None | str):
        resource_id (None | str):
        person_ids (list[int]):
        request_body (Any | None):
        before_state (Any | None):
        after_state (Any | None):
        upstream_calls (list[ListAuditEventsResponse200ItemsItemUpstreamCallsItem]):
        sensitive (bool):
        status_code (int):
        outcome (ListAuditEventsResponse200ItemsItemOutcome):
        error_type (None | str):
        error_detail (None | str):
        app_version (str):
    """

    event_id: str
    request_id: str
    occurred_at: str
    duration_ms: int
    issuer_name: str
    issuer: None | str
    subject: str
    principal_name: None | str
    token_id: None | str
    acting_user: None | str
    source_ip: None | str
    user_agent: None | str
    method: str
    route: None | str
    path: str
    query: ListAuditEventsResponse200ItemsItemQuery
    action: ListAuditEventsResponse200ItemsItemAction
    resource_type: None | str
    resource_id: None | str
    person_ids: list[int]
    request_body: Any | None
    before_state: Any | None
    after_state: Any | None
    upstream_calls: list[ListAuditEventsResponse200ItemsItemUpstreamCallsItem]
    sensitive: bool
    status_code: int
    outcome: ListAuditEventsResponse200ItemsItemOutcome
    error_type: None | str
    error_detail: None | str
    app_version: str

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        request_id = self.request_id

        occurred_at = self.occurred_at

        duration_ms = self.duration_ms

        issuer_name = self.issuer_name

        issuer: None | str
        issuer = self.issuer

        subject = self.subject

        principal_name: None | str
        principal_name = self.principal_name

        token_id: None | str
        token_id = self.token_id

        acting_user: None | str
        acting_user = self.acting_user

        source_ip: None | str
        source_ip = self.source_ip

        user_agent: None | str
        user_agent = self.user_agent

        method = self.method

        route: None | str
        route = self.route

        path = self.path

        query = self.query.to_dict()

        action = self.action.value

        resource_type: None | str
        resource_type = self.resource_type

        resource_id: None | str
        resource_id = self.resource_id

        person_ids = self.person_ids

        request_body: Any | None
        request_body = self.request_body

        before_state: Any | None
        before_state = self.before_state

        after_state: Any | None
        after_state = self.after_state

        upstream_calls = []
        for upstream_calls_item_data in self.upstream_calls:
            upstream_calls_item = upstream_calls_item_data.to_dict()
            upstream_calls.append(upstream_calls_item)

        sensitive = self.sensitive

        status_code = self.status_code

        outcome = self.outcome.value

        error_type: None | str
        error_type = self.error_type

        error_detail: None | str
        error_detail = self.error_detail

        app_version = self.app_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eventId": event_id,
                "requestId": request_id,
                "occurredAt": occurred_at,
                "durationMs": duration_ms,
                "issuerName": issuer_name,
                "issuer": issuer,
                "subject": subject,
                "principalName": principal_name,
                "tokenId": token_id,
                "actingUser": acting_user,
                "sourceIp": source_ip,
                "userAgent": user_agent,
                "method": method,
                "route": route,
                "path": path,
                "query": query,
                "action": action,
                "resourceType": resource_type,
                "resourceId": resource_id,
                "personIds": person_ids,
                "requestBody": request_body,
                "beforeState": before_state,
                "afterState": after_state,
                "upstreamCalls": upstream_calls,
                "sensitive": sensitive,
                "statusCode": status_code,
                "outcome": outcome,
                "errorType": error_type,
                "errorDetail": error_detail,
                "appVersion": app_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_audit_events_response_200_items_item_query import (
            ListAuditEventsResponse200ItemsItemQuery,  # noqa: PLC0415
        )
        from ..models.list_audit_events_response_200_items_item_upstream_calls_item import (
            ListAuditEventsResponse200ItemsItemUpstreamCallsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        event_id = d.pop("eventId")

        request_id = d.pop("requestId")

        occurred_at = d.pop("occurredAt")

        duration_ms = d.pop("durationMs")

        issuer_name = d.pop("issuerName")

        def _parse_issuer(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issuer = _parse_issuer(d.pop("issuer"))

        subject = d.pop("subject")

        def _parse_principal_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        principal_name = _parse_principal_name(d.pop("principalName"))

        def _parse_token_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        token_id = _parse_token_id(d.pop("tokenId"))

        def _parse_acting_user(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acting_user = _parse_acting_user(d.pop("actingUser"))

        def _parse_source_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_ip = _parse_source_ip(d.pop("sourceIp"))

        def _parse_user_agent(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_agent = _parse_user_agent(d.pop("userAgent"))

        method = d.pop("method")

        def _parse_route(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        route = _parse_route(d.pop("route"))

        path = d.pop("path")

        query = ListAuditEventsResponse200ItemsItemQuery.from_dict(d.pop("query"))

        action = ListAuditEventsResponse200ItemsItemAction(d.pop("action"))

        def _parse_resource_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resource_type = _parse_resource_type(d.pop("resourceType"))

        def _parse_resource_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resource_id = _parse_resource_id(d.pop("resourceId"))

        person_ids = cast(list[int], d.pop("personIds"))

        def _parse_request_body(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        request_body = _parse_request_body(d.pop("requestBody"))

        def _parse_before_state(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        before_state = _parse_before_state(d.pop("beforeState"))

        def _parse_after_state(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        after_state = _parse_after_state(d.pop("afterState"))

        upstream_calls = []
        _upstream_calls = d.pop("upstreamCalls")
        for upstream_calls_item_data in _upstream_calls:
            upstream_calls_item = ListAuditEventsResponse200ItemsItemUpstreamCallsItem.from_dict(
                upstream_calls_item_data
            )

            upstream_calls.append(upstream_calls_item)

        sensitive = d.pop("sensitive")

        status_code = d.pop("statusCode")

        outcome = ListAuditEventsResponse200ItemsItemOutcome(d.pop("outcome"))

        def _parse_error_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_type = _parse_error_type(d.pop("errorType"))

        def _parse_error_detail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_detail = _parse_error_detail(d.pop("errorDetail"))

        app_version = d.pop("appVersion")

        list_audit_events_response_200_items_item = cls(
            event_id=event_id,
            request_id=request_id,
            occurred_at=occurred_at,
            duration_ms=duration_ms,
            issuer_name=issuer_name,
            issuer=issuer,
            subject=subject,
            principal_name=principal_name,
            token_id=token_id,
            acting_user=acting_user,
            source_ip=source_ip,
            user_agent=user_agent,
            method=method,
            route=route,
            path=path,
            query=query,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            person_ids=person_ids,
            request_body=request_body,
            before_state=before_state,
            after_state=after_state,
            upstream_calls=upstream_calls,
            sensitive=sensitive,
            status_code=status_code,
            outcome=outcome,
            error_type=error_type,
            error_detail=error_detail,
            app_version=app_version,
        )

        return list_audit_events_response_200_items_item
