import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

df1 = pd.read_excel('D:\\base_de_dados.xlsx', sheet_name = 1)
df2 = pd.read_excel('D:\\base_de_dados.xlsx', sheet_name = 3)
df = pd.merge(df1,df2[['SUBJECTID','sstat']],on='SUBJECTID', how='left')
df_clean = df.dropna()
iloc=df_clean.iloc[:,4:8].values
frequent_itemsets = apriori(iloc, min_support=0.5, use_colnames=True)
print(frequent_itemsets)