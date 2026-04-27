import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

class RareDiseaseMLModel:
    def __init__(self):
        self.model = None
        self.gene_encoder = MultiLabelBinarizer()
        self.disease_encoder = LabelEncoder()
        self.disease_names = []
        self.trained = False
    
    def prepare_data(self, diseases_info, diseases_genes):
        """Prepare training data from disease and gene datasets"""
        print("Preparing training data...")
        
        # Group genes by disease
        gene_groups = diseases_genes.groupby('OrphaCode')['GeneSymbol'].apply(list).reset_index()
        
        # Merge with disease info
        data = diseases_info.merge(gene_groups, on='OrphaCode', how='inner')
        
        # Filter diseases with genes
        data = data[data['GeneSymbol'].apply(len) > 0]
        
        print(f"Total diseases with genetic data: {len(data)}")
        
        return data
    
    def train(self, diseases_info, diseases_genes):
        """Train the ML model"""
        print("\n[ML MODEL] Training started...")
        
        # Prepare data
        data = self.prepare_data(diseases_info, diseases_genes)
        
        if len(data) < 10:
            print("[WARNING] Not enough data for training")
            return False
        
        # Limit to top 500 diseases for faster training
        if len(data) > 500:
            data = data.head(500)
            print(f"[ML MODEL] Using top {len(data)} diseases for faster training")
        
        # Encode genes (features)
        X = self.gene_encoder.fit_transform(data['GeneSymbol'])
        
        # Encode diseases (labels)
        y = self.disease_encoder.fit_transform(data['Name'])
        self.disease_names = self.disease_encoder.classes_
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train smaller, faster model
        self.model = RandomForestClassifier(
            n_estimators=50,  # Reduced from 100
            max_depth=10,     # Reduced from 20
            random_state=42,
            n_jobs=-1
        )
        
        print(f"Training on {len(X_train)} samples...")
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"[ML MODEL] Training completed!")
        print(f"[ML MODEL] Accuracy: {accuracy:.2%}")
        print(f"[ML MODEL] Total diseases: {len(self.disease_names)}")
        
        self.trained = True
        return True
    
    def predict_disease(self, genes):
        """Predict disease from gene list"""
        if not self.trained:
            return {"error": "Model not trained"}
        
        if not genes or len(genes) == 0:
            return {"error": "No genes provided"}
        
        # Encode input genes
        X = self.gene_encoder.transform([genes])
        
        # Predict
        prediction = self.model.predict(X)[0]
        probabilities = self.model.predict_proba(X)[0]
        
        # Get top 5 predictions
        top_indices = np.argsort(probabilities)[-5:][::-1]
        top_diseases = []
        
        for idx in top_indices:
            if probabilities[idx] > 0.01:  # Only show if probability > 1%
                top_diseases.append({
                    "disease": self.disease_names[idx],
                    "probability": float(probabilities[idx]),
                    "confidence": f"{probabilities[idx]*100:.2f}%"
                })
        
        return {
            "predicted_disease": self.disease_names[prediction],
            "confidence": f"{probabilities[prediction]*100:.2f}%",
            "top_predictions": top_diseases,
            "genes_analyzed": genes
        }
    
    def predict_from_symptoms(self, symptoms_genes):
        """Predict disease from symptom-related genes"""
        return self.predict_disease(symptoms_genes)
    
    def get_disease_info(self, disease_name):
        """Get information about a predicted disease"""
        return {
            "disease": disease_name,
            "status": "Rare Disease",
            "recommendation": "Consult with a genetic specialist"
        }
    
    def save_model(self, filepath='models/rare_disease_model.pkl'):
        """Save trained model"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump({
                'model': self.model,
                'gene_encoder': self.gene_encoder,
                'disease_encoder': self.disease_encoder,
                'disease_names': self.disease_names,
                'trained': self.trained
            }, f)
        print(f"[ML MODEL] Model saved to {filepath}")
    
    def load_model(self, filepath='models/rare_disease_model.pkl'):
        """Load trained model"""
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                data = pickle.load(f)
                self.model = data['model']
                self.gene_encoder = data['gene_encoder']
                self.disease_encoder = data['disease_encoder']
                self.disease_names = data['disease_names']
                self.trained = data['trained']
            print(f"[ML MODEL] Model loaded from {filepath}")
            return True
        return False
