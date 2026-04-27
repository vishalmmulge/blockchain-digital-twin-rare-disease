from flask import Flask, render_template, request, jsonify, redirect, url_for
from main_system import RareDiseasePrivacySystem
import os

app = Flask(__name__)

# Initialize system
system = RareDiseasePrivacySystem("../archive")
system.load_data()

# Pre-register demo patients
system.register_patient("PATIENT_001", 166024)
system.register_patient("PATIENT_002", 166032)
system.register_patient("PATIENT_003", 166035)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    info = system.get_blockchain_info()
    logs = system.get_access_logs()
    return render_template('dashboard.html', info=info, logs=logs)

@app.route('/register_patient', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        patient_id = request.form.get('patient_id')
        orpha_code = request.form.get('orpha_code')
        try:
            result = system.register_patient(patient_id, int(orpha_code))
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)})
    return render_template('register_patient.html')

@app.route('/manage_access', methods=['GET', 'POST'])
def manage_access():
    if request.method == 'POST':
        action = request.form.get('action')
        user_id = request.form.get('user_id')
        patient_id = request.form.get('patient_id')
        
        if action == 'grant':
            system.grant_access(user_id, patient_id)
            return jsonify({"status": "success", "message": f"Access granted to {user_id}"})
        elif action == 'revoke':
            system.revoke_access(user_id, patient_id)
            return jsonify({"status": "success", "message": f"Access revoked from {user_id}"})
        elif action == 'check':
            has_access = system.smart_contract.check_permission(user_id, patient_id)
            return jsonify({"status": "success", "has_access": has_access})
    
    return render_template('manage_access.html')

@app.route('/request_data', methods=['GET', 'POST'])
def request_data():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        patient_id = request.form.get('patient_id')
        result = system.request_data(user_id, patient_id)
        return jsonify(result)
    return render_template('request_data.html')

@app.route('/blockchain_info')
def blockchain_info():
    info = system.get_blockchain_info()
    is_valid = system.verify_integrity()
    return render_template('blockchain_info.html', info=info, is_valid=is_valid)

@app.route('/access_logs')
def access_logs():
    logs = system.get_access_logs()
    return render_template('access_logs.html', logs=logs)

@app.route('/predict_disease', methods=['GET', 'POST'])
def predict_disease():
    if request.method == 'POST':
        genes_input = request.form.get('genes')
        genes = [g.strip() for g in genes_input.split(',') if g.strip()]
        
        result = system.predict_disease(genes)
        return jsonify(result)
    
    return render_template('predict_disease.html')

@app.route('/diagnose_patient', methods=['GET', 'POST'])
def diagnose_patient():
    if request.method == 'POST':
        patient_id = request.form.get('patient_id')
        genes_input = request.form.get('genes')
        genes = [g.strip() for g in genes_input.split(',') if g.strip()]
        
        result = system.diagnose_patient(patient_id, genes)
        return jsonify(result)
    
    return render_template('diagnose_patient.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
