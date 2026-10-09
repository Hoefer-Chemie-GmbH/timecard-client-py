from enum import StrEnum


class GetDailyBalanceResponse200CarryOversItemKind(StrEnum):
    MANUAL = "MANUAL"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
