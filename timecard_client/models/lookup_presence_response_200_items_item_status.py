from enum import StrEnum


class LookupPresenceResponse200ItemsItemStatus(StrEnum):
    ABSENT = "ABSENT"
    PRESENT = "PRESENT"

    def __str__(self) -> str:
        return str(self.value)
