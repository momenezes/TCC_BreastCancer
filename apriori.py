import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt

df1 = pd.read_excel("C:/Users/marin/Downloads/base_de_dados.xlsx", sheet_name = 1)
df2 = pd.read_excel("C:/Users/marin/Downloads/base_de_dados.xlsx", sheet_name = 3)
df1_df2 = pd.merge(df1,df2[['SUBJECTID','sstat']],on='SUBJECTID', how='left')
df = df1_df2[df1_df2.sstat != 9]
df_clean = df.dropna()

df_apriori = df_clean.iloc[:,[4,5,6,7,16]]
print(df_apriori.columns)

te = TransactionEncoder()
te_ary = te.fit(df_apriori).transform(df_apriori)
df_te = pd.DataFrame(te_ary, columns=te.columns_)
print(df_te)

frequent_itemsets = apriori(df_te, min_support=0.02, use_colnames=True)
print(frequent_itemsets['support'].describe())

ass_rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print(ass_rules)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=20)
print(rules)

support_arr=np.array(frequent_itemsets['support'])

plt.hist(support_arr)
plt.xlabel('Frequência')
plt.ylabel('Gravidade')
plt.show()