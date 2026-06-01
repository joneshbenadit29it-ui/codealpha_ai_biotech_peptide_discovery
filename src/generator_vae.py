import random

class PeptideVAE:
    def __init__(self, latent_dim=32):
        self.latent_dim = latent_dim
        self.amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

    def generate_sequences(self, num_samples=3, length=12):
        """Simulates sampling from the trained latent continuous distributions."""
        generated = []
        for _ in range(num_samples):
            seq = "".join(random.choice(self.amino_acids) for _ in range(length))
            generated.append(seq)
        return generated