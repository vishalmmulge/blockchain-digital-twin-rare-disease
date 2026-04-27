# 🌐 Web UI Instructions

## 🚀 How to Run the Web Interface

### Step 1: Install Dependencies
```bash
pip install flask
```

### Step 2: Start the Server
```bash
python app.py
```

### Step 3: Open Browser
Navigate to: **http://localhost:5000**

## 📱 Features Available in UI

### 1. Dashboard
- View system statistics
- See recent access logs
- Monitor blockchain status

### 2. Register Patient
- Add new patients to the system
- Link patients with rare diseases
- Automatic digital twin creation

### 3. Manage Access
- **Grant Access**: Give users permission to view patient data
- **Revoke Access**: Remove user permissions
- **Check Permission**: Verify if user has access

### 4. Request Data
- Access patient information (if authorized)
- View medical and genetic data
- All requests are logged on blockchain

### 5. Blockchain Info
- View total blocks
- Check blockchain integrity
- Verify security status

### 6. Access Logs
- Complete audit trail
- See all system activities
- Track who accessed what and when

## 🔐 Security Features

✅ Smart contract access control
✅ Blockchain immutable logging
✅ Data encryption
✅ Permission-based access
✅ Complete audit trail

## 💡 Quick Start Guide

1. **Grant Access First**:
   - Go to "Manage Access"
   - Select "Grant Access"
   - User: RESEARCHER_001
   - Patient: PATIENT_001

2. **Request Data**:
   - Go to "Request Data"
   - User: RESEARCHER_001
   - Patient: PATIENT_001
   - You'll see the data!

3. **Check Logs**:
   - Go to "Access Logs"
   - See your activity recorded on blockchain

## 🎯 Demo Patients Available

- PATIENT_001 (OrphaCode: 166024)
- PATIENT_002 (OrphaCode: 166032)
- PATIENT_003 (OrphaCode: 166035)

## 🛑 To Stop Server

Press `Ctrl + C` in the terminal
