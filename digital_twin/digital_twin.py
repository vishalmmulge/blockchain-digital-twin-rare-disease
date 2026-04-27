import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import hashlib
import json

class DigitalTwin:
    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.medical_data = {}
        self.genetic_data = {}
        self.predictions = {}
        self.model = None
    
    def add_medical_data(self, data: dict):
        self.medical_data.update(data)
    
    def add_genetic_data(self, genes: list):
        self.genetic_data['genes'] = genes
    
    def get_data_hash(self) -> str:
        data_string = json.dumps({
            "patient_id": self.patient_id,
            "medical_data": self.medical_data,
            "genetic_data": self.genetic_data
        }, sort_keys=True)
        return hashlib.sha256(data_string.encode()).hexdigest()
    
    def predict_disease(self, model) -> dict:
        if not self.genetic_data.get('genes'):
            return {"error": "No genetic data available"}
        
        self.predictions = {
            "risk_score": np.random.random(),
            "predicted_diseases": []
        }
        return self.predictions
    
    def simulate_treatment(self, treatment: str) -> dict:
        return {
            "treatment": treatment,
            "predicted_outcome": "positive",
            "confidence": 0.85
        }

class DigitalTwinManager:
    def __init__(self):
        self.twins = {}
        self.model = None
    
    def create_twin(self, patient_id: str, medical_data: dict, genetic_data: list) -> DigitalTwin:
        twin = DigitalTwin(patient_id)
        twin.add_medical_data(medical_data)
        twin.add_genetic_data(genetic_data)
        self.twins[patient_id] = twin
        return twin
    
    def get_twin(self, patient_id: str) -> DigitalTwin:
        return self.twins.get(patient_id)
    
    def train_model(self, df: pd.DataFrame):
        le = LabelEncoder()
        X = df[['OrphaCode']].values
        y = le.fit_transform(df['Name'])
        
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X, y)
        return self.model
