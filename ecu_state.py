"""
ECU internal state (memory)
Keeps track of session and security status
"""

class ECUState:
    def __init__(self):
        self.session = 0x01          # Default Session
        self.security_unlocked = False
        self.ac_status = "OFF"
