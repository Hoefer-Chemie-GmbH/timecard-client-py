from timecard_client.errors import UnexpectedStatus
from timecard_client.problem import parse_problem


def test_parse_problem_reads_the_facade_error_body():
    err = UnexpectedStatus(404, b'{"type":"https://x/errors/not-found","title":"Not found","status":404,"detail":"gone","instance":"urn:request:abc"}')
    p = parse_problem(err)
    assert p is not None
    assert p.status == 404 and p.detail == "gone" and p.request_id == "abc"


def test_parse_problem_returns_none_for_other_bodies():
    assert parse_problem(UnexpectedStatus(502, b"<html>")) is None
