# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:20:23 2023

@author: Wilian
"""
numero = int(input('Digite um número para a sequencia de Fibonacci'))

def Fibonacci(x):
    if x < 2:
        return x
    return (Fibonacci(x - 1) + Fibonacci(x - 2))


lista = [Fibonacci(x) for x in range(numero)]
print(lista)
print(numero)
if numero in lista:
    print('O número inserido pertence a sequencia')
else:
    print('O número inserido não pertence a sequencia')

    