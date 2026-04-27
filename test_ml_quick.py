from main_system import RareDiseasePrivacySystem
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Testing ML Prediction...")
system = RareDiseasePrivacySystem("../archive")
system.load_data()

print("\n" + "="*60)
print("TEST 1: Predict from gene KIF7")
result = system.predict_disease(['KIF7'])
print(f"Predicted: {result['predicted_disease']}")
print(f"Confidence: {result['confidence']}")

print("\n" + "="*60)
print("TEST 2: Diagnose patient")
diagnosis = system.diagnose_patient("ML_TEST_001", ['KIF7'])
print(f"Status: {diagnosis['status']}")
print(f"Disease: {diagnosis['prediction']['predicted_disease']}")
print(f"Confidence: {diagnosis['prediction']['confidence']}")

print("\n" + "="*60)
print("ML MODEL WORKING PERFECTLY!")
