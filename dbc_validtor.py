def check_sginal_bounds(value: float, min_limit: float, max_limit: float):
    """
    Returns true f the value is within limit else false
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Signal value must be a number")
    return min_limit <= value <= max_limit
