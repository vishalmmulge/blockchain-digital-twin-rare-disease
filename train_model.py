from main_system import RareDiseasePrivacySystem
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("PRE-TRAINING ML MODEL")
print("=" * 60)

system = RareDiseasePrivacySystem("../archive")
print("\nThis will take 1-2 minutes. Please wait...")
system.load_data()

print("\n" + "=" * 60)
print("MODEL TRAINED AND SAVED!")
print("Now you can use the web UI instantly.")
print("=" * 60)
