"""
UDS Service 0x31 - Routine Control
Example: AC ON / OFF
"""

def handle_routine(state, data):
    # Minimum length check: 31 xx rr rr
    if len(data) < 4:
        return [0x7F, 0x31, 0x13]  # Incorrect length

    sub_function = data[1]
    routine_id = (data[2] << 8) | data[3]  # FF00

    # Allow routine only if security unlocked
    if not state.security_unlocked:
        return [0x7F, 0x31, 0x33]  # Security access denied

    # Routine ID: FF00 (AC Control)
    if routine_id != 0xFF00:
        return [0x7F, 0x31, 0x31]  # Request out of range

    # Start Routine (AC ON)
    if sub_function == 0x01:
        state.ac_status = "ON"
        return [0x71, 0x01, 0xFF, 0x00]

    # Stop Routine (AC OFF)
    elif sub_function == 0x02:
        state.ac_status = "OFF"
        return [0x71, 0x02, 0xFF, 0x00]

    else:
        return [0x7F, 0x31, 0x12]  # Sub-function not supported
