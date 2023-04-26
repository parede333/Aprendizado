# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:26:12 2023

@author: Wilian
"""
#x = float(input('Digite o valor do primeiro número X '))
#y = float(input('Digite o valor do segundo número Y '))
#base = int(input('Digite o valor da base '))
#expoente = int(input('Digite o valor do expoente '))
def maior(x,y):
    if x > y : return print('X é maior')
    else: print('Y é maior')

def media(x,y):
    media = (x + y)/2
    print(f'A média aritmética de x e y é {media}')
    
def potenciacao(base,expoente):
    resultado = base**expoente
    print(f'O resultado é {resultado}')

def soma(x,y):
    print(x + y)

def subtracao(x,y):
    print(x - y)

def multiplicacao(x,y):
    print(x * y)

def divisao(x,y):
    print( x / y)
   
def qua(base):
    print(base**2)

def raiz(radicando):
    print(radicando**(1/2))

def DivisãoBaseDifZero(dividendo):
    if dividendo == 0 : print('Não é possivel dividir por zero')
    else: print(1/dividendo)

def porcentagem(numero,requerido):
    print(numero*(requerido/100))
    
def transF(x):
    if x > 0: print(x*(-1))
    elif x < 0: print(x*(-1))
    else: print(x)
    
transF(0)
#potenciacao(base,expoente)
#maior(x,y)
#media(x,y)