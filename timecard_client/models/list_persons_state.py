from enum import StrEnum


class ListPersonsState(StrEnum):
    ACTIVE = "ACTIVE"
    DEACTIVATED = "DEACTIVATED"
    LEFT = "LEFT"

    def __str__(self) -> str:
        return str(self.value)
