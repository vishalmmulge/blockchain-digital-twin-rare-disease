from main_system import RareDiseasePrivacySystem
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("BLOCKCHAIN + DIGITAL TWIN SYSTEM - QUICK TEST")
print("=" * 60)

# Initialize system
print("\n[1/6] Initializing system...")
system = RareDiseasePrivacySystem("../archive")

# Load data
print("\n[2/6] Loading data...")
system.load_data()

# Register 1 patient
print("\n[3/6] Registering patient...")
result = system.register_patient("PATIENT_001", 166024)
if result.get("status") == "success":
    print(f"      Disease: {result['profile']['disease_name']}")
    print(f"      Genes: {result['profile']['genes'][:3] if result['profile']['genes'] else 'None'}")

# Grant access
print("\n[4/6] Granting access...")
system.grant_access("RESEARCHER_001", "PATIENT_001")

# Request data
print("\n[5/6] Requesting data...")
data = system.request_data("RESEARCHER_001", "PATIENT_001")

# Verify blockchain
print("\n[6/6] Verifying blockchain...")
system.verify_integrity()

print("\n" + "=" * 60)
info = system.get_blockchain_info()
print(f"RESULT: {info['total_blocks']} blocks, {info['total_access_logs']} logs")
print("=" * 60)
