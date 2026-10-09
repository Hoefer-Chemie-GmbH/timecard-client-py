from enum import StrEnum


class ReplaceCarryOverResponse200Unit(StrEnum):
    DAYS = "DAYS"
    SECONDS = "SECONDS"

    def __str__(self) -> str:
        return str(self.value)
