from enum import StrEnum


class ListAuditEventsFormat(StrEnum):
    CSV = "csv"
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
