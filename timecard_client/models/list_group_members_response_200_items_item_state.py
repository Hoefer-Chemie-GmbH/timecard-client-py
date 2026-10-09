from enum import StrEnum


class ListGroupMembersResponse200ItemsItemState(StrEnum):
    ACTIVE = "ACTIVE"
    DEACTIVATED = "DEACTIVATED"
    LEFT = "LEFT"

    def __str__(self) -> str:
        return str(self.value)
