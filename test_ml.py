from main_system import RareDiseasePrivacySystem
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("ML MODEL TEST - RARE DISEASE PREDICTION")
print("=" * 60)

# Initialize system
print("\n[1/4] Initializing system...")
system = RareDiseasePrivacySystem("../archive")

# Load data and train model
print("\n[2/4] Loading data and training ML model...")
system.load_data()

# Test prediction
print("\n[3/4] Testing disease prediction...")
print("\nTest 1: Single gene (KIF7)")
result1 = system.predict_disease(['KIF7'])
print(f"Predicted: {result1.get('predicted_disease', 'Error')}")
print(f"Confidence: {result1.get('confidence', 'N/A')}")

print("\nTest 2: Multiple genes (CWC27)")
result2 = system.predict_disease(['CWC27'])
print(f"Predicted: {result2.get('predicted_disease', 'Error')}")
print(f"Confidence: {result2.get('confidence', 'N/A')}")

# Test full diagnosis
print("\n[4/4] Testing full patient diagnosis...")
diagnosis = system.diagnose_patient("TEST_PATIENT_001", ['KIF7'])
if diagnosis.get('status') == 'success':
    print(f"Patient diagnosed successfully!")
    print(f"Disease: {diagnosis['prediction']['predicted_disease']}")
    print(f"Confidence: {diagnosis['prediction']['confidence']}")

# Show blockchain info
print("\n" + "=" * 60)
info = system.get_blockchain_info()
print(f"Blockchain: {info['total_blocks']} blocks, Valid: {info['chain_valid']}")
print("=" * 60)
print("\nML MODEL READY FOR USE!")
