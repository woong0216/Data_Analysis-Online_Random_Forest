# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:37:43 2020

Online Random Forest

@author: jaewoong han
"""

from scipy.io import arff
import pandas as pd
import numpy as np
from rfpimp import *
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

data = arff.loadarff("./data/DriftSets/hyperplane6.arff")
df = pd.DataFrame(data[0])

# 결과물 numeric으로 고치기
de=[]
for a in df['output'].values:
    de.append(a.decode())
del df['output']
df['output']=de
X=df.iloc[:,0:10].values
df['output']=df['output'].astype(str).astype(int)
y=df['output'].values

# list
def divide_list(l, n): 
    # 리스트 l의 길이가 n이면 계속 반복
    for i in range(0, len(l), n): 
        yield l[i:i + n] 
        
# 한 리스트에 몇개씩 담을지 결정
n = 1000

result1 = list(divide_list(X, n))
result2 = list(divide_list(y, n))


# RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=3, warm_start=True)
for a,b in zip(result1, result2):
    rfc.fit(a, b)
    rfc.n_estimators += 10
    importances = rfc.feature_importances_
    std = np.std([rfc.feature_importances_ for tree in rfc.estimators_],
             axis=0)
    indices = np.argsort(importances)[::-1]

    # Print the feature ranking
    plt.figure()
    plt.title("Feature importances")
    plt.bar(range(X.shape[1]), importances[indices],color="r", yerr=std[indices], align="center")
    plt.xticks(range(X.shape[1]), indices)
    plt.xlim([-1, X.shape[1]])
    plt.show()
    print("Accuracy: ",rfc.score(X,y))
