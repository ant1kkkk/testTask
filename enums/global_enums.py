from enum import Enum


class GlobalErrorMessages(Enum):
    STATUS_CODES_DONT_MATCH = 'Received status code is not equal to expected'

    DATA_DONT_MATCH = "Received data is not equal to expected"
