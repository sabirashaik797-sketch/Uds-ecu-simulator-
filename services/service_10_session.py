"""
UDS Service 0x10 - Diagnostic Session Control
"""

def handle_session(state, data):
    """
    data[0] -> Service ID (0x10)
    data[1] -> Sub-function (01, 02, 03)
    """

    if len(data) < 2:
        return [0x7F, 0x10, 0x13]  # Incorrect message length

    sub_function = data[1]

    # Default Session
    if sub_function == 0x01:
        state.session = 0x01
        return [0x50, 0x01, 0x00, 0x32, 0x01]

    # Programming Session
    elif sub_function == 0x02:
        state.session = 0x02
        return [0x50, 0x02, 0x00, 0x32, 0x01]

    # Extended Diagnostic Session
    elif sub_function == 0x03:
        state.session = 0x03
        return [0x50, 0x03, 0x00, 0x32, 0x01]

    else:
        return [0x7F, 0x10, 0x12]  # Sub-function not supported
