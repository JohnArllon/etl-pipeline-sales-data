import pandas as pd

def extract_data(path):
    print("📥 Extraindo dados...")
    return pd.read_csv(path)