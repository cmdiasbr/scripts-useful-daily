import csv
import pandas as pd
import numpy as np

df1 = pd.read_csv("relacoes-completas.csv")
df2 = pd.read_csv("relacoes.csv")

df3 = df1.merge(df2, on=["solicitacao_id"], how='outer')
df3.to_csv("final.csv",index=False)