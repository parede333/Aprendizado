# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:26:53 2023

@author: Wilian
"""
import json
with open('dados.json') as f:
    lista = json.load(f)

lista2 = []
for i in lista:
       lista2.append(i['valor'])


lista3 = [1, 1 , 2 , 2 ,3]
lista4 =[]
for i in lista2:
    if i not in lista4:
        lista4.append(i)

lista4.sort()
lista4.remove(0.0)
print(max(lista4))
print(min(lista4))
x = sum(lista4)/len(lista4)
print(x)
