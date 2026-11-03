from enum import StrEnum


class GetMeResponse200TimecardSessions(StrEnum):
    ALLOWED = "allowed"
    OFF = "off"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
