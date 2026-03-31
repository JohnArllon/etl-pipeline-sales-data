from sqlalchemy import create_engine

def load_data(df):
    print("💾 Carregando dados...")

    engine = create_engine("sqlite:///data/sales.db")
    df.to_sql("sales", engine, if_exists="replace", index=False)