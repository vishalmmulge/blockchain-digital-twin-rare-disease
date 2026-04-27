import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from blockchain.blockchain import Blockchain, SmartContract
from blockchain.privacy import PrivacyLayer
from digital_twin.digital_twin import DigitalTwinManager
from data.data_loader import DataLoader
from models.fast_model import FastRareDiseaseModel

class RareDiseasePrivacySystem:
    def __init__(self, data_path: str):
        self.blockchain = Blockchain()
        self.smart_contract = SmartContract()
        self.privacy_layer = PrivacyLayer()
        self.twin_manager = DigitalTwinManager()
        self.data_loader = DataLoader(data_path)
        self.ml_model = FastRareDiseaseModel()
        print("[OK] System initialized")
    
    def load_data(self):
        print("   Loading datasets...")
        self.data_loader.load_all_data()
        print(f"   Loaded {len(self.data_loader.diseases_info)} diseases")
        
        print("   Training fast ML model...")
        self.ml_model.train(
            self.data_loader.diseases_info,
            self.data_loader.diseases_genes
        )
        
        print("[OK] Data loaded and ML model ready")
    
    def register_patient(self, patient_id: str, orpha_code: int):
        profile = self.data_loader.create_patient_profile(orpha_code)
        if not profile:
            return {"error": "Disease not found"}
        
        twin = self.twin_manager.create_twin(
            patient_id,
            {"disease": profile['disease_name'], "orpha_code": orpha_code},
            profile['genes']
        )
        
        data_hash = twin.get_data_hash()
        self.blockchain.add_block({
            "type": "patient_registration",
            "patient_id": self.privacy_layer.hash_sensitive_data(patient_id),
            "data_hash": data_hash,
            "disease": profile['disease_name']
        })
        
        print(f"[OK] Patient {patient_id} registered with disease: {profile['disease_name']}")
        return {"status": "success", "twin": twin, "profile": profile}
    
    def grant_access(self, user_id: str, patient_id: str):
        self.smart_contract.grant_access(user_id, patient_id)
        self.blockchain.log_access(user_id, patient_id, "access_granted")
        print(f"[OK] Access granted to {user_id} for patient {patient_id}")
    
    def revoke_access(self, user_id: str, patient_id: str):
        self.smart_contract.revoke_access(user_id, patient_id)
        self.blockchain.log_access(user_id, patient_id, "access_revoked")
        print(f"[OK] Access revoked from {user_id} for patient {patient_id}")
    
    def request_data(self, user_id: str, patient_id: str):
        if not self.smart_contract.check_permission(user_id, patient_id):
            print(f"[DENIED] Access denied for {user_id}")
            return {"error": "Access denied"}
        
        self.blockchain.log_access(user_id, patient_id, "data_accessed")
        twin = self.twin_manager.get_twin(patient_id)
        
        if not twin:
            return {"error": "Patient not found"}
        
        anonymized = self.privacy_layer.anonymize_patient_data({
            "patient_id": patient_id,
            "medical_data": twin.medical_data,
            "genetic_data": twin.genetic_data
        })
        
        print(f"[OK] Data accessed by {user_id}")
        return {"status": "success", "data": anonymized}
    
    def update_model(self, user_id: str, update_info: dict):
        self.blockchain.add_block({
            "type": "model_update",
            "user_id": user_id,
            "update_info": update_info
        })
        print(f"[OK] Model updated by {user_id}")
    
    def verify_integrity(self):
        is_valid = self.blockchain.verify_chain()
        print(f"[SECURITY] Blockchain integrity: {'Valid' if is_valid else 'Invalid'}")
        return is_valid
    
    def get_access_logs(self):
        return self.blockchain.access_logs
    
    def get_blockchain_info(self):
        return {
            "total_blocks": len(self.blockchain.chain),
            "total_access_logs": len(self.blockchain.access_logs),
            "chain_valid": self.blockchain.verify_chain()
        }
    
    def predict_disease(self, genes):
        """Predict disease from gene list using ML model"""
        prediction = self.ml_model.predict_disease(genes)
        
        # Log prediction on blockchain
        self.blockchain.add_block({
            "type": "disease_prediction",
            "genes": genes,
            "prediction": prediction.get('predicted_disease', 'Unknown')
        })
        
        return prediction
    
    def diagnose_patient(self, patient_id: str, genes: list):
        """Diagnose patient using ML model and create digital twin"""
        # Predict disease
        prediction = self.predict_disease(genes)
        
        if prediction.get('error'):
            return prediction
        
        # Create digital twin with prediction
        twin = self.twin_manager.create_twin(
            patient_id,
            {
                "predicted_disease": prediction['predicted_disease'],
                "confidence": prediction['confidence']
            },
            genes
        )
        
        # Log on blockchain
        data_hash = twin.get_data_hash()
        self.blockchain.add_block({
            "type": "patient_diagnosis",
            "patient_id": self.privacy_layer.hash_sensitive_data(patient_id),
            "data_hash": data_hash,
            "predicted_disease": prediction['predicted_disease']
        })
        
        print(f"[OK] Patient {patient_id} diagnosed: {prediction['predicted_disease']}")
        
        return {
            "status": "success",
            "patient_id": patient_id,
            "prediction": prediction,
            "twin": twin
        }
