from pickle import TRUE
import pandas as pd
import openpyxl

df = pd.read_excel('D:\\base_de_dados.xlsx', sheet_name = 1)
df2 = pd.read_excel('D:\\base_de_dados.xlsx', sheet_name = 3)
print(df,df2)