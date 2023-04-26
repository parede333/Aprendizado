# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:43:08 2023

@author: Wilian
"""

idade = int(input("Qual a sua idade? "))
if idade > 4 and idade <= 7:
    print('Você possui idade entre 5 a 7 anos, portanto você pertence a categoria Infantil A.')
elif idade > 7 and idade <= 10:
    print('Você possui idade entre 8 a 10 anos, portanto você pertence a categoria Infantil B')
elif idade > 10 and idade <= 13:
    print('Você possui idade entre 11 a 13 anos, portanto você pertence a categoria Juvenil A')
elif idade > 13 and idade <= 17:
    print('Você possui idade entre 14 a 17 anos, portanto você pertence a categoria Juvenil B') 
else:
    print('Você não possui idade para participar.')