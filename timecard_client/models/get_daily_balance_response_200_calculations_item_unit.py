from enum import StrEnum


class GetDailyBalanceResponse200CalculationsItemUnit(StrEnum):
    DAYS = "DAYS"
    SECONDS = "SECONDS"

    def __str__(self) -> str:
        return str(self.value)
