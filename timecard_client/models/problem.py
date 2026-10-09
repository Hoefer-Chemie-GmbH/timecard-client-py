from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.problem_errors_item import ProblemErrorsItem
    from ..models.problem_upstream import ProblemUpstream


T = TypeVar("T", bound="Problem")


@_attrs_define
class Problem:
    """Problem Details (RFC 9457). Quote `instance` when reporting a problem.

    Attributes:
        type_ (str): problem type; its last path segment names it, e.g. `validation`, `unauthorized`, `rate-limited`,
            `upstream`
        title (str): short summary of the problem type
        status (int): HTTP status code
        instance (str): `urn:request:<id>`; the id is also sent as the response header `X-Request-Id`
        detail (str | Unset): explanation of this occurrence
        errors (list[ProblemErrorsItem] | Unset): schema violations (type `validation`)
        upstream (ProblemUpstream | Unset): the call to the time recording system that failed, with its status, code and
            message
    """

    type_: str
    title: str
    status: int
    instance: str
    detail: str | Unset = UNSET
    errors: list[ProblemErrorsItem] | Unset = UNSET
    upstream: ProblemUpstream | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        status = self.status

        instance = self.instance

        detail = self.detail

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        upstream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upstream, Unset):
            upstream = self.upstream.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "status": status,
                "instance": instance,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors
        if upstream is not UNSET:
            field_dict["upstream"] = upstream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.problem_errors_item import ProblemErrorsItem  # noqa: PLC0415
        from ..models.problem_upstream import ProblemUpstream  # noqa: PLC0415

        d = dict(src_dict)
        type_ = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        instance = d.pop("instance")

        detail = d.pop("detail", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ProblemErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ProblemErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _upstream = d.pop("upstream", UNSET)
        upstream: ProblemUpstream | Unset
        if isinstance(_upstream, Unset):
            upstream = UNSET
        else:
            upstream = ProblemUpstream.from_dict(_upstream)

        problem = cls(
            type_=type_,
            title=title,
            status=status,
            instance=instance,
            detail=detail,
            errors=errors,
            upstream=upstream,
        )

        problem.additional_properties = d
        return problem

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
