"""Wave2 Burst 3 — heavy payload"""
import json
class Wave2Burst3:
    def __init__(self):
        self.payload = {f"field_{i}": [j*3 for j in range(50)] for i in range(20)}
    def serialize(self):
        return json.dumps(self.payload)
