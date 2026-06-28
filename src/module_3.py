"""Module 3 — stress test with big output."""
import json
class StressTest3:
    def __init__(self):
        self.data = {f"key_{i}": list(range(i*10)) for i in range(30)}
    def dump(self):
        return json.dumps(self.data, indent=2)
