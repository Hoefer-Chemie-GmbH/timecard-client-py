from enum import StrEnum


class GetDepartmentResponse200Kind(StrEnum):
    DEPARTMENT = "DEPARTMENT"
    GROUP = "GROUP"

    def __str__(self) -> str:
        return str(self.value)
