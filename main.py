import pandas as pd
import openpyxl
import numpy as np
import seaborn as sns; sns.set()
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz

df1 = pd.read_excel('D:\\base_de_dados.xlsx', sheet_name = 1)
df2 = pd.read_excel('D:\\base_de_dados.xlsx', sheet_name = 3)
df1_df2 = pd.merge(df1,df2[['SUBJECTID','sstat']],on='SUBJECTID', how='left')
df = df1_df2[df1_df2.sstat != 9]
print(df.columns.tolist())
#está dando erro
#x = df.iloc[:,[0,4,5,6,7]]
#y = df.iloc[:,[0,16]]

#tree_clf = DecisionTreeClassifier(max_depth=2, random_state=1000)
#tree_clf.fit(x, y)

#export_graphviz(
        #tree_clf,
        #out_file=df,
        #feature_names=df.feature_names[0:15],
        #class_names=df.target_names
        #)

#ainda não testamos
#def visualize_classifier(model, X, y, ax=None, cmap='rainbow'):
    #ax = ax or plt.gca()
    #ax.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cmap,
               #clim=(y.min(), y.max()), zorder=3)
    #ax.axis('tight')
    #ax.axis('off')
    #xlim = ax.get_xlim()
    #ylim = ax.getylim()

    #model.fit(X, y)
   # xx, yy = np.meshgrid(np.linspace(xlim, num=200),
                         #np.linspace(ylim, num=200))
    #Z = model.predict(np.c[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    #n_classes = len(np.unique(y))
    #contours = ax.contourf(xx, yy, Z, alpha=0.3,
                           #levels=np.arange(n_classes + 1) - 0.5,
                           #cmap=cmap, clim=(y.min(), y.max()),
                           #zorder=1)
    #ax.set(xlim=xlim, ylim=ylim)

#visualize_classifier(tree_clf, X, y)