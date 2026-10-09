from enum import StrEnum


class CreatePersonBodySex(StrEnum):
    DIVERSE = "DIVERSE"
    FEMALE = "FEMALE"
    MALE = "MALE"
    UNSPECIFIED = "UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
