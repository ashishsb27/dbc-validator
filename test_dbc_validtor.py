import pytest
from dbc_validtor import check_sginal_bounds

def test_check_signal_bounds_within_limits():
    assert check_sginal_bounds(5.0, 0.0, 10.0) == True

def test_check_signal_bounds_below_min_limit():
    assert check_sginal_bounds(-1, 0, 10) == False

def test_check_signal_bounds_above_max_limit():
    assert check_sginal_bounds(15, 0, 10) == False

def test_check_signal_bounds_with_non_numeric_value():
    with pytest.raises(ValueError):
        check_sginal_bounds("not_a_number", 0, 10)

