from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def run_pipeline():
    df = extract_data("data/raw/sales.csv")
    df = transform_data(df)
    load_data(df)
    print("✅ Pipeline finalizado!")

if __name__ == "__main__":
    run_pipeline()