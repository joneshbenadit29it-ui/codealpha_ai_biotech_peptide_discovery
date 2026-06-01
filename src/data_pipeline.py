class MockDataLoader:
    def __init__(self):
        # Representative dataset of antimicrobial/therapeutic target-binding peptides
        self.raw_data = ["MGEKITERVRR", "KLFKKILKFLK", "RGGRLCYCRRR", "ACDEFGHIKLMNPQRSTVWY"]

    def get_sequences(self):
        return self.raw_data