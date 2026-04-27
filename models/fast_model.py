import pandas as pd
import numpy as np
from collections import defaultdict

class FastRareDiseaseModel:
    """Lightweight model for instant disease prediction"""
    
    def __init__(self):
        self.gene_disease_map = defaultdict(list)
        self.disease_genes_map = defaultdict(set)
        self.trained = False
    
    def train(self, diseases_info, diseases_genes):
        """Build gene-disease mapping"""
        print("\n[FAST ML] Building gene-disease database...")
        
        # Create mappings
        for _, row in diseases_genes.iterrows():
            gene = row['GeneSymbol']
            disease_code = row['OrphaCode']
            
            # Get disease name
            disease_info = diseases_info[diseases_info['OrphaCode'] == disease_code]
            if not disease_info.empty:
                disease_name = disease_info.iloc[0]['Name']
                self.gene_disease_map[gene].append(disease_name)
                self.disease_genes_map[disease_name].add(gene)
        
        print(f"[FAST ML] Loaded {len(self.gene_disease_map)} genes")
        print(f"[FAST ML] Loaded {len(self.disease_genes_map)} diseases")
        self.trained = True
        return True
    
    def predict_disease(self, genes):
        """Predict disease from genes"""
        if not self.trained:
            return {"error": "Model not trained"}
        
        if not genes or len(genes) == 0:
            return {"error": "No genes provided"}
        
        # Score diseases based on gene matches
        disease_scores = defaultdict(float)
        
        for gene in genes:
            if gene in self.gene_disease_map:
                diseases = self.gene_disease_map[gene]
                for disease in diseases:
                    # Score based on gene match ratio
                    total_genes = len(self.disease_genes_map[disease])
                    disease_scores[disease] += 1.0 / total_genes
        
        if not disease_scores:
            return {
                "predicted_disease": "Unknown - No matching genes found",
                "confidence": "0%",
                "top_predictions": [],
                "genes_analyzed": genes
            }
        
        # Sort by score
        sorted_diseases = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Get top predictions
        top_predictions = []
        for disease, score in sorted_diseases[:5]:
            confidence = min(score * 100, 100)
            top_predictions.append({
                "disease": disease,
                "probability": score,
                "confidence": f"{confidence:.2f}%"
            })
        
        best_disease, best_score = sorted_diseases[0]
        confidence = min(best_score * 100, 100)
        
        return {
            "predicted_disease": best_disease,
            "confidence": f"{confidence:.2f}%",
            "top_predictions": top_predictions,
            "genes_analyzed": genes
        }
