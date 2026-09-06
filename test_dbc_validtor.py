import pytest
from dbc_validtor import check_signal_bounds

def test_check_signal_bounds_within_limits():
    assert check_signal_bounds(5.0, 0.0, 10.0, "ECU") == {"valid": True, "message": "ECU: 5.0 is within range [0.0, 10.0]"}

def test_check_signal_bounds_below_min_limit():
    assert check_signal_bounds(-1, 0, 10, "ECU") == {"valid": False, "message": "ECU: -1 is below minimum (allowed: 0–10)"}

def test_check_signal_bounds_above_max_limit():
    assert check_signal_bounds(15, 0, 10, "ECU") == {"valid": False, "message": "ECU: 15 is above maximum (allowed: 0–10)"} 

def test_check_signal_bounds_with_non_numeric_value():
    with pytest.raises(TypeError):
        check_signal_bounds("not_a_number", 0, 10, "ECU")

def test_check_signal_bounds_with_non_numeric_limits():
    with pytest.raises(TypeError):
        check_signal_bounds(5, "min", 10, "ECU" )
    with pytest.raises(TypeError):
        check_signal_bounds(5, 0, "max", "ECU" )

def test_check_signal_bounds_with_int_signal_value():
    with pytest.raises(TypeError):
        check_signal_bounds(5, 0, 10, 0)