import sys
from src.data_pipeline import MockDataLoader
from src.generator_vae import PeptideVAE
from src.predictor_transformer import AffinityPredictor

def main():
    print("====================================================================")
    print("Initializing AI/ML Pipeline for De Novo Peptide Discovery")
    print("====================================================================\n")
    
    # 1. Pipeline Stage: Data Loading
    print("[Phase A] Loading bio-sequence datasets...")
    data_loader = MockDataLoader()
    sequences = data_loader.get_sequences()
    print(f"-> Successfully loaded {len(sequences)} baseline active sequences.\n")
    
    # 2. Pipeline Stage: Latent Generative Loop
    print("[Phase B] Initializing Variational Autoencoder (VAE)...")
    vae = PeptideVAE(latent_dim=32)
    generated_candidates = vae.generate_sequences(num_samples=3)
    print("-> Generated Candidate Sequences:")
    for i, seq in enumerate(generated_candidates, 1):
        print(f"   * Candidate {i}: {seq}")
    print("")

    # 3. Pipeline Stage: Deep Predictor Engine
    print("[Phase C] Running Affinity Predictor Infrastructure...")
    predictor = AffinityPredictor()
    for seq in generated_candidates:
        affinity_score = predictor.predict_affinity(seq)
        print(f"   * Predicted IC50 for {seq}: {affinity_score:.2f} nM")
        
    print("\n====================================================================")
    print("Pipeline executed successfully. Ready for full framework optimization.")
    print("====================================================================")

if __name__ == "__main__":
    main()