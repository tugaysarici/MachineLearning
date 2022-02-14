"""
Bu kodda:
    -eksikveriler.csv dosyasındaki 2 tane eksik veriyi diğer yaş değerlerine bakarak ortalama bir değer ile düzenledik.
@author: "Tugay SARICI"
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# numpy --> büyük sayılar ve hesaplama işlemleri için.
# pandas --> veriler için, verileri düzgün bir şekilde tutabilmek ve veri çerçeveleri oluşturmak ve onların içerisindeki verileri düzgün bir şekilde tutmak için.
# matplotlib.pyplot --> çizim amacıyla

veriler = pd.read_csv('eksikveriler.csv')

 #sci - kit learn
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)