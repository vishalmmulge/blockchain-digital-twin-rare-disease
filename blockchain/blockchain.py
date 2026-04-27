import hashlib
import json
from time import time
from typing import List, Dict, Any

class Block:
    def __init__(self, index: int, timestamp: float, data: Dict, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.access_logs: List[Dict] = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, time(), {"type": "genesis"}, "0")
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> Block:
        return self.chain[-1]
    
    def add_block(self, data: Dict) -> Block:
        new_block = Block(
            len(self.chain),
            time(),
            data,
            self.get_latest_block().hash
        )
        self.chain.append(new_block)
        return new_block
    
    def log_access(self, user_id: str, patient_id: str, action: str):
        log_entry = {
            "user_id": user_id,
            "patient_id": patient_id,
            "action": action,
            "timestamp": time()
        }
        self.access_logs.append(log_entry)
        self.add_block({"type": "access_log", "log": log_entry})
    
    def verify_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

class SmartContract:
    def __init__(self):
        self.permissions: Dict[str, List[str]] = {}
    
    def grant_access(self, user_id: str, patient_id: str):
        if user_id not in self.permissions:
            self.permissions[user_id] = []
        if patient_id not in self.permissions[user_id]:
            self.permissions[user_id].append(patient_id)
    
    def revoke_access(self, user_id: str, patient_id: str):
        if user_id in self.permissions and patient_id in self.permissions[user_id]:
            self.permissions[user_id].remove(patient_id)
    
    def check_permission(self, user_id: str, patient_id: str) -> bool:
        return user_id in self.permissions and patient_id in self.permissions[user_id]
