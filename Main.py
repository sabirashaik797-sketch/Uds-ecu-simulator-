import can
from ecu_state import ECUState
from services.service_10_session import handle_session
from services.service_27_security import handle_security

# Initialize CAN (virtual CAN example)
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

# Create ECU state
state = ECUState()

print("UDS ECU Simulator Started")

while True:
    msg = bus.recv()
    if msg is None:
        continue

    data = list(msg.data)
    sid = data[0]

    if sid == 0x10:
        response = handle_session(state, data)

    elif sid == 0x27:
        if state.session != 0x03:
            response = [0x7F, 0x27, 0x7E]
        else:
            response = handle_security(state, data)

    else:
        response = [0x7F, sid, 0x11]

    bus.send(
        can.Message(
            arbitration_id=0x7E8,
            data=response,
            is_extended_id=False
        )
        )
