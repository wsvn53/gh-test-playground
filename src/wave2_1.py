"""Wave2 Burst 1 — heavy payload"""
import json
class Wave2Burst1:
    def __init__(self):
        self.payload = {f"field_{i}": [j*1 for j in range(50)] for i in range(20)}
    def serialize(self):
        return json.dumps(self.payload)
