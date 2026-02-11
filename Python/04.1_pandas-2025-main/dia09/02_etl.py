# %%
import pandas as pd
import sqlalchemy
# from sklearn import cluster


# %%

with open('etl.sql') as open_file:
    query = open_file.read() 

print(query) # retorna uma string

# %%
engine = sqlalchemy.create_engine("sqlite:///../data/database.db")
df = pd.read_sql_query(query, con=engine)
df

# %%
## Treina modelo de cluster
# kmean = cluster.KMeans(n_clusters=4)
# kmean.fit(df[['IdCliente','TotalPontos']])

# df["cluster"] =  kmean.labels_
# df

# %%
# df.to_sql(
#     "sellers_cluster",
#     con=engine,
#     index=False,
#     if_exists="replace",
# )

# %%
