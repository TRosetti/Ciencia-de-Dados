# %%
import pandas as pd
import sqlalchemy

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

# %%
clientes = pd.read_sql_table(table_name="clientes", con=engine)

# %%
clientes.shape

# %%

query = "SELECT * FROM clientes LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)
df_100

# %%

