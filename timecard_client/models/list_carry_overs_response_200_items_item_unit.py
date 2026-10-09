from enum import StrEnum


class ListCarryOversResponse200ItemsItemUnit(StrEnum):
    DAYS = "DAYS"
    SECONDS = "SECONDS"

    def __str__(self) -> str:
        return str(self.value)
