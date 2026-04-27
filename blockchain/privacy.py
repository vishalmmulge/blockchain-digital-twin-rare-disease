from cryptography.fernet import Fernet
import hashlib
import json

class PrivacyLayer:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
    
    def encrypt_data(self, data: dict) -> bytes:
        json_data = json.dumps(data)
        return self.cipher.encrypt(json_data.encode())
    
    def decrypt_data(self, encrypted_data: bytes) -> dict:
        decrypted = self.cipher.decrypt(encrypted_data)
        return json.loads(decrypted.decode())
    
    def hash_sensitive_data(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()
    
    def anonymize_patient_data(self, patient_data: dict) -> dict:
        anonymized = patient_data.copy()
        if 'patient_id' in anonymized:
            anonymized['patient_id'] = self.hash_sensitive_data(anonymized['patient_id'])
        return anonymized
