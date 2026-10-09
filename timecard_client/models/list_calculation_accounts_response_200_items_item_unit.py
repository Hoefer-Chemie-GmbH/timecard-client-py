from enum import StrEnum


class ListCalculationAccountsResponse200ItemsItemUnit(StrEnum):
    DAYS = "DAYS"
    SECONDS = "SECONDS"

    def __str__(self) -> str:
        return str(self.value)
