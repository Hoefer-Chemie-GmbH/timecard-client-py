from enum import StrEnum


class CreateCarryOverResponse201Unit(StrEnum):
    DAYS = "DAYS"
    SECONDS = "SECONDS"

    def __str__(self) -> str:
        return str(self.value)
