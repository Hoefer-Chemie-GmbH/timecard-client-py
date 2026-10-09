from enum import StrEnum


class ListAbsenceTypesUsage(StrEnum):
    ALL = "ALL"
    BOOKING = "BOOKING"
    MANUAL = "MANUAL"
    REQUEST = "REQUEST"

    def __str__(self) -> str:
        return str(self.value)
