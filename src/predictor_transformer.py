import random

class AffinityPredictor:
    def __init__(self):
        pass

    def predict_affinity(self, sequence: str) -> float:
        """Simulates sequence-to-affinity inference outputs."""
        # Lower IC50 implies superior binding affinity performance
        return random.uniform(1.2, 250.5)