from enum import StrEnum


class ListAuditEventsOutcome(StrEnum):
    CLIENT_ERROR = "CLIENT_ERROR"
    DENIED = "DENIED"
    SERVER_ERROR = "SERVER_ERROR"
    SUCCESS = "SUCCESS"
    UPSTREAM_ERROR = "UPSTREAM_ERROR"

    def __str__(self) -> str:
        return str(self.value)
