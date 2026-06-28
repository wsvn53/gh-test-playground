"""Module 4 — even more stress."""
class StressTest4:
    def __init__(self):
        self.matrix = [[i*j for j in range(50)] for i in range(50)]
    def trace(self):
        return sum(self.matrix[i][i] for i in range(50))
