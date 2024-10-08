from enum import StrEnum


class GrayBoxStatus(StrEnum):
    PASSED = 'PASSED'
    FAILED = 'FAILED'
    EXECUTION_ERROR = 'EXECUTION_ERROR'
    FUNCTION_NOT_FOUND = 'FUNCTION_NOT_FOUND'
    NOT_A_FUNCTION = 'NOT_A_FUNCTION'
