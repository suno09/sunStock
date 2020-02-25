from enum import Enum


class AccountState(Enum):
    FAILED = -2
    NOT_ACTIVE = -1
    DISCONNECTED = 0
    CONNECTED = 1
