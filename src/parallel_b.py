"""Parallel test B"""
class ParallelB:
    def run(self): return {f"k{i}": i*i for i in range(500)}
