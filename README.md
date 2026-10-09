# timecard-client-py

Python client for a REST facade in front of the time recording system REINER SCT timeCard, generated with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). The facade offers persons, bookings, balances, absences and master data as a documented JSON API with OAuth authentication, scopes and an audit log.

This project is not affiliated with, endorsed or sponsored by REINER SCT. REINER SCT and timeCard are trademarks of their respective owner.

- API version `0.2.1`.
- Generated: `timecard_client/api/**` (one module per operation, grouped by tag), `timecard_client/models/**`, `client.py`, `errors.py`, `types.py`.
- Hand-written: `timecard_client/google_auth.py` (Google ID tokens, refreshing client), `timecard_client/problem.py` (Problem Details), `timecard_client/photo.py` (photo upload, which the generator cannot express).

## Installation

From the Git tag of a version:

```
pip install "timecard-client @ git+https://github.com/Hoefer-Chemie-GmbH/timecard-client-py@v0.2.1"
```

or from the wheel attached to the GitHub release:

```
pip install https://github.com/Hoefer-Chemie-GmbH/timecard-client-py/releases/download/v0.2.1/timecard_client-0.2.1-py3-none-any.whl
```

Python 3.11 or newer. Dependencies: `httpx`, `attrs`, `python-dateutil`, `google-auth`, `requests`.

## Authentication

The facade accepts Google ID tokens of service accounts. Each service account is registered by the operator of the facade together with the scopes it may use; ask the operator for the registration and for the base URL of the facade. The base URL is also the audience of the token. Keep the service account's JSON key outside the repository and load it from a secret store or a file outside the checkout.

```python
import os

from timecard_client.api.persons import list_persons
from timecard_client.google_auth import authenticated_client

base_url = os.environ["TIMECARD_API_URL"]  # e.g. https://timecard-api.example.com
client = authenticated_client(base_url, os.environ["GOOGLE_SA_KEY_FILE"])
with client:
    page = list_persons.sync(client=client, page_size=50)
    for person in page.items:
        print(person.id, person.person_no, person.last_name)
```

`authenticated_client` mints an ID token with the base URL as audience and renews it before a request once it is about to expire. Every generated operation offers `sync`, `sync_detailed`, `asyncio` and `asyncio_detailed`.

## Scopes

| Scope | Allows |
|---|---|
| `persons:read` | persons, photos, calculation accounts and carry-overs |
| `persons:write` | create and change persons, photos, carry-overs |
| `persons:delete` | delete carry-overs |
| `bookings:read` | bookings, daily balances, calendar, absence overview |
| `bookings:write` | create and change bookings, absence bookings, working time profile assignments |
| `bookings:delete` | delete bookings and working time profile assignments |
| `masterdata:read` | absence types, projects, work operations, departments, groups, calculation templates, working time profiles, break rules, free fields |
| `masterdata:write` | create and change work operations |
| `masterdata:delete` | delete work operations |
| `presence:read` | presence display |
| `audit:read` | the facade's audit log |

A call outside the scopes of the service account answers `403` with a Problem Details body.

## Errors

The facade answers every error with an RFC 9457 Problem Details body. The generated `sync` functions raise `timecard_client.errors.UnexpectedStatus` for statuses the specification does not list; `timecard_client.problem.parse_problem(err)` reads the body into a `ProblemDetails` with `status`, `title`, `detail`, `errors` and `request_id`. Quote the request id when reporting a problem to the operator; the audit log of the facade is searchable by it.

| Status | Meaning |
|---|---|
| 400, 422 | invalid request; `errors` lists the fields |
| 401 | token missing, expired or for a different audience |
| 403 | scope missing, or the person is outside the set released for writing |
| 404 | the resource does not exist |
| 409 | the time recording system rejected the change (e.g. month closed, duplicate) |
| 429 | rate limit of the facade; wait and retry |
| 502, 503 | the time recording system is unavailable or answered unexpectedly; retry later |

## Acting user

Pass `acting_user="..."` to `authenticated_client` when calls are made on behalf of a human user; it is sent as `X-Acting-User` and stored in the audit log next to the service account.

## Photo upload

`PUT /v1/persons/{personId}/photo` takes a raw JPEG body, which the generator does not support. Use `timecard_client.photo.put_person_photo(client, person_id, jpeg_bytes)`.

## Example and tests

- `python examples/read_person.py` (needs `TIMECARD_API_URL` and `GOOGLE_SA_KEY_FILE`).
- `python -m pytest` runs the unit tests of the hand-written layer; no network.

## About this repository

The client is generated from the facade's OpenAPI specification; only the authentication helper, the Problem Details helper, the example and the tests are written by hand. The content of this repository is replaced by synchronisation pull requests whenever the specification changes, so changes made here directly would be overwritten. Report problems as issues.

The version equals the API version of the facade. Merging a synchronisation pull request releases the version if it has no tag yet. Breaking changes of the API arrive as a new major version with a new `/v2` base path.
