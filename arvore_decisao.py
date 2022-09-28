import pandas as pd
import openpyxl
import numpy as np
import seaborn as sns; sns.set()
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
from tabulate import tabulate

df1 = pd.read_excel('D:\\base_de_dados.xlsx', sheet_name = 1)
df2 = pd.read_excel('D:\\base_de_dados.xlsx', sheet_name = 3)
df1_df2 = pd.merge(df1,df2[['SUBJECTID','sstat']],on='SUBJECTID', how='left')
df = df1_df2[df1_df2.sstat != 9]
df_clean = df.dropna()
print(tabulate(df_clean.iloc[:,[0,2,3,4,5,6,7,10,11,16]], headers = ['SUBJECTID', 'age', 'race_id', 'ERpos', 'PgRpos',
'HR Pos', 'Her2MostPos', 'BilateralCa', 'Laterality', 'sstat']))

dfx = df_clean.iloc[:,[0,2,3,4,5,6,7,10,11]]
dfy = df_clean.iloc[:,[0,16]]
dfbom = pd.merge(dfx, dfy, on="SUBJECTID")
print(dfbom)

x = dfbom.iloc[:,1:9]
y = dfbom.iloc[:,9]
print(x,y)

tree_clf = DecisionTreeClassifier(
    max_leaf_nodes = 10, 
    max_depth= 5
)
tree_clf.fit(x,y)
tree.plot_tree(tree_clf)
plt.show()