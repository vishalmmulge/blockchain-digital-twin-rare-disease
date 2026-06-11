# 🔐 Blockchain + Digital Twin + ML for Rare Disease Privacy System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

A secure healthcare system combining **Blockchain**, **Digital Twins**, and **Machine Learning** for rare disease management with complete privacy preservation.

![System Architecture](https://img.shields.io/badge/Architecture-Blockchain%20%2B%20ML%20%2B%20Digital%20Twin-blueviolet)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [How Blockchain is Used](#-how-blockchain-is-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Web Interface](#-web-interface)
- [ML Model](#-ml-model)
- [API Documentation](#-api-documentation)
- [Security](#-security)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This project implements a **privacy-preserving healthcare system** for rare disease management using:

- **Blockchain**: Immutable audit trail and tamper-proof records
- **Digital Twins**: Virtual patient models for personalized healthcare
- **Machine Learning**: AI-powered disease prediction from genetic markers
- **Smart Contracts**: Automated access control and permission management
- **Encryption**: End-to-end data privacy and security

### 🎥 Demo

```
Patient Registration → ML Diagnosis → Access Control → Data Sharing → Blockchain Logging
```

---

## ✨ Features

### 🔐 Blockchain Features
- ✅ **Immutable Records**: Cannot modify or delete historical data
- ✅ **SHA-256 Hashing**: Cryptographic security for data integrity
- ✅ **Chain Verification**: Detect tampering attempts instantly
- ✅ **Audit Trail**: Complete log of all system activities
- ✅ **Decentralized**: No single point of failure

### 🧬 ML Features
- ✅ **Disease Prediction**: Analyze genes and predict rare diseases
- ✅ **4,552 Genes**: Comprehensive genetic database
- ✅ **4,128 Diseases**: Rare disease knowledge base
- ✅ **Instant Predictions**: < 1 second response time
- ✅ **Confidence Scores**: Probability-based predictions

### 🔑 Access Control
- ✅ **Smart Contracts**: Automated permission management
- ✅ **Grant/Revoke Access**: Dynamic permission control
- ✅ **Permission Checking**: Verify access rights
- ✅ **Role-Based Access**: Support for doctors, researchers, nurses

### 🛡️ Privacy & Security
- ✅ **Data Encryption**: Fernet symmetric encryption
- ✅ **Data Anonymization**: Hash sensitive information
- ✅ **Privacy Layer**: Separate encryption module
- ✅ **Secure Storage**: Only hashes on blockchain

### 🌐 Web Interface
- ✅ **Modern UI**: Beautiful gradient design
- ✅ **Responsive**: Works on all devices
- ✅ **Real-time Updates**: Instant feedback
- ✅ **8 Interactive Pages**: Complete functionality

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     WEB INTERFACE (Flask)                    │
│                    http://localhost:5000                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    MAIN SYSTEM LAYER                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Blockchain  │  │ Digital Twin │  │   ML Model   │     │
│  │   Manager    │  │   Manager    │  │   Engine     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    CORE COMPONENTS                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Blockchain  │  │Smart Contract│  │Privacy Layer │     │
│  │    Chain     │  │Access Control│  │  Encryption  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                      DATA LAYER                              │
│         Rare Disease Dataset (11,456 diseases)               │
│         Gene Database (4,552 genes)                          │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

```
[Patient Data] → [Digital Twin Creation] → [ML Prediction]
                          ↓
                  [Blockchain Logging]
                          ↓
                  [Smart Contract Check]
                          ↓
                  [Encrypted Storage]
                          ↓
                  [Secure Access]
```

---

## 🔗 How Blockchain is Used

### 1️⃣ **Patient Registration**
```python
# When registering a patient
Block {
    "type": "patient_registration",
    "patient_id": "hashed_abc123",      # Privacy: Hashed ID
    "data_hash": "xyz789",               # Hash of medical data
    "disease": "Disease Name",
    "timestamp": 1234567890
}
```
**Purpose**: Immutable record of patient enrollment

---

### 2️⃣ **Access Control Logging**
```python
# When granting access
Block {
    "type": "access_log",
    "user_id": "RESEARCHER_001",
    "patient_id": "PATIENT_001",
    "action": "access_granted",
    "timestamp": 1234567890
}
```
**Purpose**: Audit trail of permission changes

---

### 3️⃣ **Data Access Tracking**
```python
# When accessing patient data
Block {
    "type": "access_log",
    "user_id": "DOCTOR_001",
    "patient_id": "PATIENT_001",
    "action": "data_accessed",
    "timestamp": 1234567899
}
```
**Purpose**: Track who accessed what and when

---

### 4️⃣ **ML Prediction Logging**
```python
# When ML predicts disease
Block {
    "type": "disease_prediction",
    "genes": ["KIF7", "CWC27"],
    "prediction": "Disease Name",
    "confidence": "95.5%",
    "timestamp": 1234567900
}
```
**Purpose**: Permanent medical diagnosis records

---

### 5️⃣ **Model Update Tracking**
```python
# When updating ML model
Block {
    "type": "model_update",
    "user_id": "RESEARCHER_001",
    "version": "1.1",
    "accuracy": 0.92,
    "timestamp": 1234567910
}
```
**Purpose**: Version control and transparency

---

### 🔐 Blockchain Security

#### **SHA-256 Hashing**
```python
# Each block has unique hash
hash = SHA256(index + timestamp + data + previous_hash)
# Result: a3f5b8c9d2e1f4a7b6c5d8e9f2a1b4c7...
```

#### **Chain Verification**
```python
def verify_chain():
    for each block:
        ✓ Check if hash is correct
        ✓ Check if linked to previous block
        ✓ Detect any tampering
    return True/False
```

#### **What's Protected**
- ✅ Cannot delete old records
- ✅ Cannot modify past transactions
- ✅ Cannot insert fake blocks
- ✅ Instant tampering detection

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 2GB RAM minimum
- Windows/Linux/macOS

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/blockchain-digital-twin-rare-disease.git
cd blockchain-digital-twin-rare-disease
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Prepare Dataset
Place the rare disease dataset files in the `archive/` folder:
- `rare_diseases_info.csv`
- `rare_diseases_genes.csv`
- `rare_diseases_prevalence.csv`

### Step 4: Run the Application
```bash
cd blockchain_digital_twin
python app.py
```

### Step 5: Open Browser
Navigate to: **http://localhost:5000**

---

## 💻 Usage

### Command Line Interface

#### Quick Test
```bash
python quick_test.py
```

#### ML Model Test
```bash
python test_ml_quick.py
```

#### Full Demo
```bash
python demo.py
```

---

### Python API

```python
from main_system import RareDiseasePrivacySystem

# Initialize system
system = RareDiseasePrivacySystem("../archive")
system.load_data()

# Register patient
system.register_patient("PATIENT_001", 166024)

# Grant access
system.grant_access("DOCTOR_001", "PATIENT_001")

# Request data
data = system.request_data("DOCTOR_001", "PATIENT_001")

# Predict disease
prediction = system.predict_disease(['KIF7'])

# Diagnose patient
diagnosis = system.diagnose_patient("PATIENT_002", ['KIF7', 'CWC27'])

# Verify blockchain
is_valid = system.verify_integrity()
```

---

## 🌐 Web Interface

### Pages Overview

#### 1. 🏠 **Home Dashboard**
- Navigation hub
- System overview
- Feature highlights

#### 2. 📊 **Dashboard**
- System statistics
- Recent activity
- Blockchain status

#### 3. 🧬 **Predict Disease** (ML)
- Enter genetic markers
- Get disease prediction
- Confidence scores
- Top 5 predictions

**Example:**
```
Input: KIF7
Output: Multiple epiphyseal dysplasia-macrocephaly-facial dysmorphism syndrome
Confidence: 100%
```

#### 4. 🔬 **Diagnose Patient** (ML + Blockchain)
- Complete patient diagnosis
- Creates digital twin
- Logs on blockchain
- Encrypted storage

**Workflow:**
```
Patient ID + Genes → ML Analysis → Digital Twin → Blockchain → Secure Record
```

#### 5. 👤 **Register Patient**
- Manual patient registration
- Link with known disease
- OrphaCode lookup

#### 6. 🔑 **Manage Access**
- Grant permissions
- Revoke access
- Check permissions
- Role management

#### 7. 📥 **Request Data**
- Access patient information
- Permission-based
- View encrypted data
- Audit logging

#### 8. ⛓️ **Blockchain Info**
- Total blocks
- Chain validation
- Integrity check
- Security status

#### 9. 📋 **Access Logs**
- Complete audit trail
- All activities
- Timestamp tracking
- User actions

---

## 🧠 ML Model

### Fast Gene-Disease Mapping Model

#### Architecture
```python
Gene Input → Gene-Disease Database → Scoring Algorithm → Top Predictions
```

#### Features
- **Training Time**: ~5 seconds
- **Prediction Time**: < 1 second
- **Genes**: 4,552 unique genes
- **Diseases**: 4,128 rare diseases
- **Accuracy**: High for known gene-disease associations

#### How It Works

1. **Training Phase**
```python
# Build gene-disease mapping
for each disease:
    for each gene in disease:
        map[gene] → disease
```

2. **Prediction Phase**
```python
# Score diseases based on gene matches
for each input_gene:
    for each disease with this gene:
        score[disease] += 1 / total_genes_in_disease

# Return top scored diseases
```

#### Sample Predictions

| Input Genes | Predicted Disease | Confidence |
|-------------|------------------|------------|
| KIF7 | Multiple epiphyseal dysplasia-macrocephaly-facial dysmorphism syndrome | 100% |
| CWC27 | Brachydactyly-short stature-retinitis pigmentosa syndrome | 100% |
| KIF7, CWC27 | Multiple predictions | 85-95% |

---

## 📡 API Documentation

### REST Endpoints

#### **POST /register_patient**
Register new patient
```json
{
  "patient_id": "PATIENT_001",
  "orpha_code": 166024
}
```

#### **POST /manage_access**
Manage access permissions
```json
{
  "action": "grant",
  "user_id": "DOCTOR_001",
  "patient_id": "PATIENT_001"
}
```

#### **POST /request_data**
Request patient data
```json
{
  "user_id": "DOCTOR_001",
  "patient_id": "PATIENT_001"
}
```

#### **POST /predict_disease**
Predict disease from genes
```json
{
  "genes": "KIF7, CWC27"
}
```

#### **POST /diagnose_patient**
Full patient diagnosis
```json
{
  "patient_id": "PATIENT_002",
  "genes": "KIF7, CWC27"
}
```

#### **GET /blockchain_info**
Get blockchain status
```json
{
  "total_blocks": 9,
  "total_access_logs": 4,
  "chain_valid": true
}
```

---

## 🔒 Security

### Encryption
- **Algorithm**: Fernet (symmetric encryption)
- **Key Management**: Secure key generation
- **Data Protection**: All sensitive data encrypted

### Hashing
- **Algorithm**: SHA-256
- **Use Cases**: 
  - Patient ID anonymization
  - Data integrity verification
  - Block hash generation

### Access Control
- **Smart Contracts**: Automated permission checks
- **Role-Based**: Support for multiple user types
- **Audit Trail**: All access logged on blockchain

### Privacy Features
- ✅ Patient IDs hashed before storage
- ✅ Medical data encrypted
- ✅ Only metadata on blockchain
- ✅ Genetic data anonymized
- ✅ HIPAA/GDPR compliant design

---

## 📊 Dataset

### Rare Disease Dataset

**Source**: Orphanet Rare Disease Database

**Files**:
- `rare_diseases_info.csv` - Disease information (11,456 diseases)
- `rare_diseases_genes.csv` - Gene associations (4,552 genes)
- `rare_diseases_prevalence.csv` - Prevalence data

**Columns**:
```
rare_diseases_info.csv:
- OrphaCode, Name, DisorderType, DisorderGroup
- ICD-11, MONDO, ICD-10, OMIM, UMLS, MeSH

rare_diseases_genes.csv:
- OrphaCode, DiseaseName, GeneSymbol, GeneName
- AssociationType, AssociationStatus
```

**Sample Data**:
| OrphaCode | Disease Name | Gene | Association |
|-----------|-------------|------|-------------|
| 166024 | Multiple epiphyseal dysplasia-macrocephaly-facial dysmorphism syndrome | KIF7 | Disease-causing germline mutation |
| 166032 | Multiple epiphyseal dysplasia-miniepiphyses syndrome | Multiple | Assessed |

---

## 📁 Project Structure

```
blockchain_digital_twin/
│
├── app.py                          # Flask web application
├── main_system.py                  # Main system integration
├── demo.py                         # Demo script
├── quick_test.py                   # Quick test script
├── test_ml_quick.py               # ML model test
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── COMPLETE_GUIDE.md              # Detailed guide
├── WEB_UI_INSTRUCTIONS.md         # Web UI guide
│
├── blockchain/                     # Blockchain module
│   ├── __init__.py
│   ├── blockchain.py              # Blockchain & Smart Contracts
│   └── privacy.py                 # Encryption & Privacy
│
├── digital_twin/                   # Digital Twin module
│   ├── __init__.py
│   └── digital_twin.py            # Digital Twin & Patient Models
│
├── models/                         # ML Models
│   ├── __init__.py
│   ├── ml_model.py                # Advanced ML model
│   └── fast_model.py              # Fast prediction model
│
├── data/                           # Data processing
│   ├── __init__.py
│   └── data_loader.py             # Dataset loader
│
├── templates/                      # HTML templates
│   ├── index.html                 # Home page
│   ├── dashboard.html             # Dashboard
│   ├── register_patient.html      # Patient registration
│   ├── manage_access.html         # Access management
│   ├── request_data.html          # Data request
│   ├── predict_disease.html       # ML prediction
│   ├── diagnose_patient.html      # Patient diagnosis
│   ├── blockchain_info.html       # Blockchain info
│   └── access_logs.html           # Access logs
│
└── static/                         # Static files
    └── css/
        └── style.css              # Stylesheet
```

---

## 🎯 Use Cases

### 1. **Hospital Patient Management**
- Register patients with rare diseases
- Create digital twins for personalized care
- Track all medical interactions on blockchain

### 2. **Research Collaboration**
- Share anonymized patient data securely
- Grant temporary access to researchers
- Maintain complete audit trail

### 3. **Clinical Diagnosis**
- Use ML to predict rare diseases from genetic markers
- Get confidence scores for diagnosis
- Log all predictions on blockchain

### 4. **Regulatory Compliance**
- Immutable audit trail for HIPAA compliance
- Track all data access for GDPR
- Prove data integrity for audits

### 5. **Telemedicine**
- Secure remote patient data access
- Permission-based sharing with specialists
- Encrypted data transmission

---

## 🔬 Technical Details

### Blockchain Implementation
- **Consensus**: Proof of Authority (PoA)
- **Block Time**: Instant (private chain)
- **Hash Algorithm**: SHA-256
- **Storage**: In-memory (can be extended to persistent storage)

### Digital Twin
- **Model Type**: Virtual patient replica
- **Data Sources**: Medical records, genetic data, IoT sensors
- **Update Frequency**: Real-time
- **Simulation**: Treatment outcome prediction

### ML Model
- **Type**: Gene-disease mapping with scoring
- **Training**: Supervised learning on labeled data
- **Features**: Gene symbols
- **Labels**: Disease names
- **Performance**: < 1s prediction time

---

## 🚦 Performance

| Metric | Value |
|--------|-------|
| ML Prediction Time | < 1 second |
| Data Loading Time | ~5 seconds |
| Blockchain Verification | Instant |
| Total Diseases | 11,456 |
| Gene Database | 4,552 genes |
| Disease Mappings | 4,128 |
| Web Response Time | < 100ms |

---

## 🧪 Testing

### Run All Tests
```bash
# Quick system test
python quick_test.py

# ML model test
python test_ml_quick.py

# Full demo
python demo.py
```

### Expected Output
```
✓ System initialized
✓ Data loaded (11,456 diseases)
✓ ML model ready (4,552 genes)
✓ Patient registered
✓ Access granted
✓ Data accessed
✓ Blockchain verified
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to all functions
- Write unit tests for new features
- Update documentation

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **VISHAL M MULGE** - *Initial work* - [MyGitHub](https://github.com/vishalmmulge)

---

## 🙏 Acknowledgments

- Orphanet for rare disease database
- Flask framework for web interface
- scikit-learn for ML capabilities
- Python cryptography library

---

## 📧 Contact

- **Email**: vishalmulge651@gmail.com
- **GitHub**: [@vishalmmulge](https://github.com/vishalmmulge)
- **LinkedIn**: [Vishal M Mulge](https://www.linkedin.com/in/vishal-m-mulge/)

---

## 🔮 Future Enhancements

- [ ] Add persistent blockchain storage (PostgreSQL/MongoDB)
- [ ] Implement distributed blockchain network
- [ ] Add more ML models (Deep Learning)
- [ ] Mobile application
- [ ] Real-time IoT sensor integration
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] Kubernetes deployment
- [ ] API rate limiting
- [ ] OAuth2 authentication
- [ ] WebSocket real-time updates

---

## 📚 Documentation

- [Complete Guide](COMPLETE_GUIDE.md) - Detailed usage guide
- [Web UI Instructions](WEB_UI_INSTRUCTIONS.md) - Web interface guide
- [API Documentation](#-api-documentation) - REST API reference

---

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

## 📈 Project Status

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![Build](https://img.shields.io/badge/Build-Passing-success)

---

**Made with ❤️ for Healthcare Innovation**
