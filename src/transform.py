def transform_data(df):
    print("🔄 Transformando dados...")

    # remover nulos
    df = df.dropna()

    # converter tipos
    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)

    # nova coluna
    df["total"] = df["price"] * df["quantity"]

    # 👉 NOVO: salvar dados tratados
    df.to_csv("data/processed/sales_clean.csv", index=False)

    # 👉 NOVO: mostrar quantidade de linhas
    print(f"✅ Linhas finais: {len(df)}")

    return df