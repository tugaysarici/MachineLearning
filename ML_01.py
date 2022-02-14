"""
Bu kodda:
    -kütüphanelerin nasıl yüklendiğine
    -verilerin nasıl import edildiğine
    -sınıf yapısına
    -liste yapısına 
    değinildi.
@author: "Tugay SARICI"
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# numpy --> büyük sayılar ve hesaplama işlemleri için.
# pandas --> veriler için, verileri düzgün bir şekilde tutabilmek ve veri çerçeveleri oluşturmak ve onların içerisindeki verileri düzgün bir şekilde tutmak için.
# matplotlib.pyplot --> çizim amacıyla

#YA DA veriler = pd.read_csv("veriler.csv")
veriler = pd.read_csv('C:\\Users\\TSRC\\Desktop\\ML\\veriler.csv')

print(veriler)

boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)


class insan:
    boy = 180
    def kosmak(self, b):
        return b + 10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))


l = [1,3,4,8] # liste
