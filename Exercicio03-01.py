# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:01:00 2023

@author: Wilian
"""
print('Digite 5 números quaisquer')
primeiro = float(input('Digite o 1° número: '))
maior = primeiro
menor = primeiro
x = 2
while True:
    numero = float(input(f'Digite o {x}° número: '))
    if numero >= maior:
        maior = numero
    elif numero <= menor:
        menor = numero
    x = x + 1
    if x == 6:
        break
print(f'O maior número inserido foi {maior} e o menor número é {menor}')