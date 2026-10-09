from enum import StrEnum


class GetHealthResponse503Timecard(StrEnum):
    LOGIN_FAILED = "login_failed"
    OK = "ok"
    SKIPPED = "skipped"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)
