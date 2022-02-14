"""
Bu kodda:
    ülke gibi bir kategorik veriyi nasıl ele aldığımıza baktık
@author: "Tugay SARICI"
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# numpy --> büyük sayılar ve hesaplama işlemleri için.
# pandas --> veriler için, verileri düzgün bir şekilde tutabilmek ve veri çerçeveleri oluşturmak ve onların içerisindeki verileri düzgün bir şekilde tutmak için.
# matplotlib.pyplot --> çizim amacıyla

veriler = pd.read_csv('veriler.csv')

ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()

print(ulke)