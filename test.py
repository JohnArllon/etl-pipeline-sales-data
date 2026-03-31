import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/sales.db")
df = pd.read_sql("SELECT * FROM sales", engine)

print(df)