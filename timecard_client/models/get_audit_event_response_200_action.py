from enum import StrEnum


class GetAuditEventResponse200Action(StrEnum):
    AUTH = "AUTH"
    CREATE = "CREATE"
    DELETE = "DELETE"
    EXECUTE = "EXECUTE"
    READ = "READ"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
