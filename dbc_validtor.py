def check_signal_bounds(
    value: float, min_val: float, max_val: float, signal_name: str = ""
) -> dict:
    """
    Check if a CAN signal value is within the allowed [min, max] range.

    Args:
        value:       The decoded signal value to check
        min_val:     Minimum allowed value
        max_val:     Maximum allowed value
        signal_name: Optional name for reporting

    Returns:
        dict with 'valid' (bool) and 'message' (str)
    """
    if not isinstance(signal_name, str):
        raise TypeError(f"signal_name must be a string, got {type(signal_name).__name__}")
    valid = min_val <= value <= max_val

    if valid:
        msg = f"{signal_name}: {value} is within range [{min_val}, {max_val}]"
    else:
        direction = "below minimum" if value < min_val else "above maximum"
        msg = f"{signal_name}: {value} is {direction} (allowed: {min_val}–{max_val})"

    return {"valid": valid, "message": msg}
