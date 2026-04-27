from main_system import RareDiseasePrivacySystem
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    print("=" * 60)
    print("BLOCKCHAIN + DIGITAL TWIN + RARE DISEASE PRIVACY SYSTEM")
    print("=" * 60)
    
    # Initialize system
    system = RareDiseasePrivacySystem("../archive")
    
    # Load data
    print("\nLoading rare disease data...")
    system.load_data()
    
    # Register patients
    print("\nRegistering patients...")
    system.register_patient("PATIENT_001", 166024)
    system.register_patient("PATIENT_002", 166032)
    system.register_patient("PATIENT_003", 166035)
    
    # Grant access to researcher
    print("\nManaging access permissions...")
    system.grant_access("RESEARCHER_001", "PATIENT_001")
    system.grant_access("RESEARCHER_001", "PATIENT_002")
    system.grant_access("DOCTOR_001", "PATIENT_003")
    
    # Request data (authorized)
    print("\nRequesting patient data (authorized)...")
    result = system.request_data("RESEARCHER_001", "PATIENT_001")
    if result.get("status") == "success":
        print(f"   Data retrieved: {result['data']['medical_data']}")
    
    # Request data (unauthorized)
    print("\nRequesting patient data (unauthorized)...")
    system.request_data("RESEARCHER_002", "PATIENT_001")
    
    # Update model
    print("\nUpdating ML model...")
    system.update_model("RESEARCHER_001", {"version": "1.1", "accuracy": 0.92})
    
    # Verify blockchain integrity
    print("\nVerifying blockchain integrity...")
    system.verify_integrity()
    
    # Display blockchain info
    print("\nBlockchain Information:")
    info = system.get_blockchain_info()
    print(f"   Total Blocks: {info['total_blocks']}")
    print(f"   Total Access Logs: {info['total_access_logs']}")
    print(f"   Chain Valid: {info['chain_valid']}")
    
    # Display access logs
    print("\nAccess Logs:")
    logs = system.get_access_logs()
    for log in logs:
        print(f"   {log['action']} - User: {log['user_id']} - Patient: {log['patient_id']}")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    main()
