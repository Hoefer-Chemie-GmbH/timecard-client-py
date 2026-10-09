from enum import StrEnum


class CreateBookingBodyType(StrEnum):
    CLOCK_IN = "CLOCK_IN"
    CLOCK_IN_WITH_REASON = "CLOCK_IN_WITH_REASON"
    CLOCK_OUT = "CLOCK_OUT"
    CLOCK_OUT_WITH_REASON = "CLOCK_OUT_WITH_REASON"
    PROJECT_END = "PROJECT_END"
    PROJECT_START = "PROJECT_START"

    def __str__(self) -> str:
        return str(self.value)
