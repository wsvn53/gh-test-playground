"""Module 5 — the grand finale!"""
class StressTest5:
    def __init__(self):
        self.data = {f"group_{g}": [i**2 for i in range(100)] for g in range(20)}
    def summary(self):
        return {k: {"count": len(v), "sum": sum(v), "max": max(v)} for k, v in self.data.items()}
