"""Reads the calling principal and lists three persons.

Environment: TIMECARD_API_URL (base URL of the facade), GOOGLE_SA_KEY_FILE (path to the service account JSON).
"""

import os

from timecard_client.api.persons import list_persons
from timecard_client.api.system import get_me
from timecard_client.google_auth import authenticated_client

base_url = os.environ["TIMECARD_API_URL"]
client = authenticated_client(base_url, os.environ.get("GOOGLE_SA_KEY_FILE", "service-account.json"))

with client:
    me = get_me.sync(client=client)
    print("principal", me.display_name, "scopes", me.scopes)
    page = list_persons.sync(client=client, page_size=3)
    for p in page.items:
        print(p.id, p.person_no, p.last_name, p.first_name)
