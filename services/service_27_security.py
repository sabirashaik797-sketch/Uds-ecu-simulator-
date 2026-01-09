"""
UDS Service 0x27 - Security Access
"""

def handle_security(state, data):
    # Minimum length check
    if len(data) < 2:
        return [0x7F, 0x27, 0x13]  # Incorrect message length

    sub_function = data[1]

    # 27 01 - Request Seed
    if sub_function == 0x01:
        state.seed = [0x12, 0x34]          # Demo seed
        return [0x67, 0x01] + state.seed

    # 27 02 - Send Key
    elif sub_function == 0x02:
        if not hasattr(state, "seed"):
            return [0x7F, 0x27, 0x24]      # Request sequence error

        key = data[2:]
        expected_key = [state.seed[0] + 1, state.seed[1] + 1]

        if key == expected_key:
            state.security_unlocked = True
            return [0x67, 0x02]
        else:
            return [0x7F, 0x27, 0x35]      # Invalid key

    return [0x7F, 0x27, 0x12]              # Sub-function not supported
