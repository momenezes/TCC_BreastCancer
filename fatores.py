import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder

df1 = pd.read_excel("C:/Users/marin/Downloads/base_de_dados.xlsx", sheet_name = 1)
df2 = pd.read_excel("C:/Users/marin/Downloads/base_de_dados.xlsx", sheet_name = 3)
df1_df2 = pd.merge(df1,df2[['SUBJECTID','sstat']],on='SUBJECTID', how='left')
df = df1_df2[df1_df2.sstat != 9]
df_clean = df.dropna()

dfx = df_clean.iloc[:,[0,2,3,4,5,6,7,10,11]]
dfy = df_clean.iloc[:,[0,16]]
dfbom = pd.merge(dfx, dfy, on="SUBJECTID")
print(dfbom)

le=LabelEncoder()
dfbom['sstat']=le.fit_transform(dfbom['sstat']) 

x = dfbom.iloc[:,3:7]
y = dfbom.iloc[:,7]

bestfeatures = SelectKBest(score_func=chi2, k='all')
fit = bestfeatures.fit(x,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(x.columns)

featureScores = pd.concat([dfcolumns,dfscores], axis=1)
featureScores.columns = ['Fator','Valor']
print(featureScores.nlargest(4,'Valor'))  #print dos 4 fatores