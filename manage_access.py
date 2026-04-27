from main_system import RareDiseasePrivacySystem
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def display_menu():
    print("\n" + "=" * 60)
    print("ACCESS MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Register New Patient")
    print("2. Grant Access")
    print("3. Revoke Access")
    print("4. Check Access Permission")
    print("5. Request Patient Data")
    print("6. View All Access Logs")
    print("7. View Blockchain Info")
    print("8. Verify Blockchain Integrity")
    print("9. Exit")
    print("=" * 60)

def main():
    # Initialize system
    print("\nInitializing system...")
    system = RareDiseasePrivacySystem("../archive")
    system.load_data()
    
    # Pre-register some patients for demo
    print("\nPre-registering demo patients...")
    system.register_patient("PATIENT_001", 166024)
    system.register_patient("PATIENT_002", 166032)
    system.register_patient("PATIENT_003", 166035)
    print("Demo patients: PATIENT_001, PATIENT_002, PATIENT_003")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == "1":
            patient_id = input("Enter Patient ID: ").strip()
            orpha_code = input("Enter Disease OrphaCode (e.g., 166024): ").strip()
            try:
                result = system.register_patient(patient_id, int(orpha_code))
                if result.get("status") == "success":
                    print(f"\n[SUCCESS] Patient registered!")
                    print(f"Disease: {result['profile']['disease_name']}")
                else:
                    print(f"\n[ERROR] {result.get('error')}")
            except Exception as e:
                print(f"\n[ERROR] {e}")
        
        elif choice == "2":
            user_id = input("Enter User ID (e.g., RESEARCHER_001): ").strip()
            patient_id = input("Enter Patient ID: ").strip()
            system.grant_access(user_id, patient_id)
            print(f"\n[SUCCESS] Access granted to {user_id} for {patient_id}")
        
        elif choice == "3":
            user_id = input("Enter User ID: ").strip()
            patient_id = input("Enter Patient ID: ").strip()
            system.smart_contract.revoke_access(user_id, patient_id)
            system.blockchain.log_access(user_id, patient_id, "access_revoked")
            print(f"\n[SUCCESS] Access revoked for {user_id} from {patient_id}")
        
        elif choice == "4":
            user_id = input("Enter User ID: ").strip()
            patient_id = input("Enter Patient ID: ").strip()
            has_access = system.smart_contract.check_permission(user_id, patient_id)
            if has_access:
                print(f"\n[RESULT] {user_id} HAS access to {patient_id}")
            else:
                print(f"\n[RESULT] {user_id} DOES NOT have access to {patient_id}")
        
        elif choice == "5":
            user_id = input("Enter User ID: ").strip()
            patient_id = input("Enter Patient ID: ").strip()
            result = system.request_data(user_id, patient_id)
            if result.get("status") == "success":
                print(f"\n[SUCCESS] Data retrieved:")
                print(f"Medical Data: {result['data']['medical_data']}")
                print(f"Genetic Data: {result['data']['genetic_data']}")
            else:
                print(f"\n[ERROR] {result.get('error')}")
        
        elif choice == "6":
            logs = system.get_access_logs()
            print(f"\n[ACCESS LOGS] Total: {len(logs)}")
            print("-" * 60)
            for i, log in enumerate(logs, 1):
                print(f"{i}. {log['action']} | User: {log['user_id']} | Patient: {log['patient_id']}")
        
        elif choice == "7":
            info = system.get_blockchain_info()
            print(f"\n[BLOCKCHAIN INFO]")
            print(f"Total Blocks: {info['total_blocks']}")
            print(f"Total Access Logs: {info['total_access_logs']}")
            print(f"Chain Valid: {info['chain_valid']}")
        
        elif choice == "8":
            is_valid = system.verify_integrity()
            if is_valid:
                print("\n[SECURITY] Blockchain is VALID - No tampering detected")
            else:
                print("\n[WARNING] Blockchain is INVALID - Possible tampering!")
        
        elif choice == "9":
            print("\n[EXIT] Goodbye!")
            break
        
        else:
            print("\n[ERROR] Invalid choice. Please enter 1-9.")

if __name__ == "__main__":
    main()
