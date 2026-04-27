import pandas as pd
import os

class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.diseases_info = None
        self.diseases_genes = None
        self.diseases_prevalence = None
    
    def load_all_data(self):
        self.diseases_info = pd.read_csv(os.path.join(self.data_path, 'rare_diseases_info.csv'))
        self.diseases_genes = pd.read_csv(os.path.join(self.data_path, 'rare_diseases_genes.csv'))
        self.diseases_prevalence = pd.read_csv(os.path.join(self.data_path, 'rare_diseases_prevalence.csv'))
        return self
    
    def get_disease_by_code(self, orpha_code: int):
        return self.diseases_info[self.diseases_info['OrphaCode'] == orpha_code]
    
    def get_genes_for_disease(self, orpha_code: int):
        disease_data = self.diseases_genes[self.diseases_genes['OrphaCode'] == orpha_code]
        return disease_data
    
    def get_all_diseases(self):
        return self.diseases_info
    
    def create_patient_profile(self, orpha_code: int):
        disease = self.get_disease_by_code(orpha_code)
        genes = self.get_genes_for_disease(orpha_code)
        
        if disease.empty:
            return None
        
        return {
            'disease_name': disease.iloc[0]['Name'],
            'orpha_code': orpha_code,
            'disorder_type': disease.iloc[0]['DisorderType'],
            'genes': genes['GeneSymbol'].tolist() if not genes.empty else []
        }
