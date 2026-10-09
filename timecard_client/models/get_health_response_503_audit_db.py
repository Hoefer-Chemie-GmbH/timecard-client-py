from enum import StrEnum


class GetHealthResponse503AuditDb(StrEnum):
    OK = "ok"
    SKIPPED = "skipped"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
