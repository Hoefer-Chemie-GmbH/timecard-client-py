from enum import StrEnum


class ListPresenceResponse200ItemsItemStatus(StrEnum):
    ABSENT = "ABSENT"
    AWAY_WITH_REASON = "AWAY_WITH_REASON"
    PRESENT = "PRESENT"

    def __str__(self) -> str:
        return str(self.value)
