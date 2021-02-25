from .constants import *


def check_result(value: int, against: int) -> str:
    success_crits = set(DEFAULT_CRITICAL_SUCCESS_RANGE)
    fail_crits = set(DEFAULT_CRITICAL_FAIL_RANGE)

    lower = against + 10
    if lower <= MIN_FAIL_CRITICAL_VALUE:
        lower = max(lower, MIN_FAIL_CRITICAL_VALUE)
        for fail_crit_val in range(lower, min(fail_crits)):
            fail_crits.add(fail_crit_val)

    upper = against - 10
    if upper >= MAX_SUCCESS_CRITICAL_VALUE:
        upper = min(upper, MAX_SUCCESS_CRITICAL_VALUE)
        for success_crit_val in range(upper, max(success_crits), -1):
            success_crits.add(success_crit_val)

    if value in success_crits:
        return RESULT_CRITICAL_SUCCESS

    if value in fail_crits:
        return RESULT_CRITICAL_FAIL

    return RESULT_SUCCESS if value <= against else RESULT_FAIL
