# timecard-client-py

Python client for a REST facade in front of the time recording system REINER SCT timeCard, generated with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). The facade offers persons, bookings, balances, absences and master data as a documented JSON API with OAuth authentication, scopes and an audit log.

This project is not affiliated with, endorsed or sponsored by REINER SCT. REINER SCT and timeCard are trademarks of their respective owner.

- API version `0.4.0`.
- Generated: `timecard_client/api/**` (one module per operation, grouped by tag), `timecard_client/models/**`, `client.py`, `errors.py`, `types.py`.
- Hand-written: `timecard_client/google_auth.py` (Google ID tokens, refreshing client), `timecard_client/problem.py` (Problem Details), `timecard_client/photo.py` (photo upload, which the generator cannot express).

## Installation

From the Git tag of a version:

```
pip install "timecard-client @ git+https://github.com/Hoefer-Chemie-GmbH/timecard-client-py@v0.4.0"
```

or from the wheel attached to the GitHub release:

```
pip install https://github.com/Hoefer-Chemie-GmbH/timecard-client-py/releases/download/v0.4.0/timecard_client-0.4.0-py3-none-any.whl
```

Python 3.11 or newer. Dependencies: `httpx`, `attrs`, `python-dateutil`, `google-auth`, `requests`.

## Getting access

Access is granted per system by the operator of the facade; there is no self-service registration. Ask the operator for access with:

| Information | Example |
|---|---|
| System name | `hr-sync` (one service account per system and environment) |
| Responsible person | name and e-mail address |
| Scopes | `persons:read`, `bookings:read` (see [Scopes](#scopes)) |
| Write access | which operations, if any |

The operator returns the base URL of the facade and a Google service account registered with the granted scopes, either as a JSON key or as the permission to obtain tokens for it without a key (see [Without a key file](#without-a-key-file)). The first call after the setup is `GET /v1/me`: it needs no scope and returns the registered name and scopes.

| Answer of `GET /v1/me` | Cause |
|---|---|
| `200` | access works; compare the scopes with the request |
| `401` | no token, token expired, or an audience other than the base URL |
| `403` | service account not registered, disabled or expired, or the source address is not allowed |

## Authentication

The facade accepts Google ID tokens of service accounts. Each service account is registered by the operator of the facade together with the scopes it may use; the operator provides the service account and the base URL of the facade (see [Getting access](#getting-access)). The base URL is also the audience of the token. Keep the service account's JSON key outside the repository and load it from a secret store or a file outside the checkout.

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

### Without a key file

A key file is a long-lived secret. Where the system runs on Google Cloud as the registered service account (Compute Engine, GKE with Workload Identity), the metadata server issues the ID token. Elsewhere the operator allows the system's own Google identity to impersonate the service account (role `Service Account Token Creator`), and the system calls the IAM Credentials API `generateIdToken` with `audience` = base URL and `includeEmail: true`; a system outside Google Cloud first obtains such an identity through Workload Identity Federation. The token must carry the claims `email` and `email_verified`: the metadata server includes them only with `format=full`, `generateIdToken` only with `includeEmail: true`. Check the result with `GET /v1/me`.

```python
import httpx

from timecard_client.google_auth import RefreshingClient


class MetadataTokenSource:
    """ID token of the service account the workload runs as, from the Google Cloud metadata server."""

    URL = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"

    def __init__(self, audience: str) -> None:
        self._params = {"audience": audience, "format": "full"}

    def token(self) -> str:
        response = httpx.get(self.URL, params=self._params, headers={"Metadata-Flavor": "Google"})
        response.raise_for_status()
        return response.text


client = RefreshingClient(base_url=base_url, token_source=MetadataTokenSource(base_url), raise_on_unexpected_status=True)
```

`RefreshingClient` accepts any object with a `token()` method (`timecard_client.google_auth.TokenSource`) and asks it before every request; the metadata server caches the token and renews it itself.

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
| `masterdata:write` | create and change projects and work operations |
| `masterdata:delete` | delete projects and work operations |
| `presence:read` | presence display |
| `audit:read` | the facade's audit log |

A call outside the scopes of the service account answers `403` with a Problem Details body.

## Errors

The facade answers every error with an RFC 9457 Problem Details body. A client from `authenticated_client` makes the generated `sync` functions raise `timecard_client.errors.UnexpectedStatus` for every error status (the specification lists success statuses only; with `raise_on_unexpected_status=False` they return `None` instead); `timecard_client.problem.parse_problem(err)` reads the body into a `ProblemDetails` with `status`, `title`, `detail`, `errors` and `request_id`. Quote the request id when reporting a problem to the operator; the audit log of the facade is searchable by it.

| Status | Meaning |
|---|---|
| 400, 422 | invalid request; `errors` lists the fields |
| 401 | token missing, expired or for a different audience |
| 403 | scope missing, or the person is outside the set released for writing |
| 404 | the resource does not exist |
| 409 | the time recording system rejected the change (e.g. month closed, duplicate) |
| 429 | rate limit of the facade; wait and retry |
| 502, 503 | the time recording system is unavailable or answered unexpectedly; retry later |

## Operating rules

- **Data.** The facade reads and changes the data of the connected time recording installation. Ask the operator whether a separate test installation exists; without one, development and tests work on real personal data and fall under the same data protection rules as production.
- **Write access.** The operator can release write access for selected persons only, for example a test person during development; calls for other persons answer `403` without reaching the time recording system.
- **Rate limit.** The facade limits the calls per service account (by default 120 per minute) and answers `429` above it; spread bulk processing over time.
- **Retries.** Retry reads after `502` or `503` with a pause; the facade itself already retries a read once against the time recording system. Send creating calls (`POST`) with an `Idempotency-Key` header, e.g. a UUID per business operation, and repeat a failed call with the same key: the facade executes it once and answers a repeat with the stored response and the header `Idempotent-Replayed: true` (`409` if the first call has no result yet, `422` if the key was used for a different request). Do not repeat changing or deleting calls blindly; read the current state first.
- **Audit.** The facade records every call with the service account, route, parameters and status.
- **Versions.** Install a fixed version (Git tag) and update deliberately; before 1.0.0 a minor version may contain incompatible changes.

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
