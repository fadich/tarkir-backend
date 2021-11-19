from tarkir_base.gurps.skill import (
    check_result,
    RESULT_CRITICAL_SUCCESS,
    RESULT_SUCCESS,
    RESULT_FAIL,
    RESULT_CRITICAL_FAIL,
)


if __name__ == '__main__':
    assert check_result(4, 5) == RESULT_CRITICAL_SUCCESS
    assert check_result(5, 5) == RESULT_SUCCESS
    assert check_result(6, 5) == RESULT_FAIL
    assert check_result(14, 5) == RESULT_FAIL
    assert check_result(15, 5) == RESULT_CRITICAL_FAIL

    assert check_result(6, 16) == RESULT_CRITICAL_SUCCESS
    assert check_result(7, 16) == RESULT_SUCCESS
    assert check_result(16, 16) == RESULT_SUCCESS
    assert check_result(17, 16) == RESULT_CRITICAL_FAIL

    assert check_result(4, 3) == RESULT_CRITICAL_SUCCESS
    assert check_result(5, 3) == RESULT_FAIL
    assert check_result(14, 3) == RESULT_FAIL
    assert check_result(15, 3) == RESULT_CRITICAL_FAIL

    assert check_result(6, 20) == RESULT_CRITICAL_SUCCESS
    assert check_result(7, 20) == RESULT_SUCCESS
    assert check_result(16, 20) == RESULT_SUCCESS
    assert check_result(18, 20) == RESULT_CRITICAL_FAIL
