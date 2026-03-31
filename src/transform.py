def transform_data(df):
    print("🔄 Transformando dados...")

    df = df.dropna()

    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)

    df["total"] = df["price"] * df["quantity"]
    
    df.to_csv("data/processed/sales_clean.csv", index=False)

    print(f"✅ Linhas finais: {len(df)}")
    
    return df
