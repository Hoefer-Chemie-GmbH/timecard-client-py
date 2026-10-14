from enum import StrEnum


class ListPresenceStatusResponse200ItemsItemStatus(StrEnum):
    ABSENT = "ABSENT"
    PRESENT = "PRESENT"

    def __str__(self) -> str:
        return str(self.value)
