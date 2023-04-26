# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:51:39 2023

@author: Wilian
"""

def dados(idade):
    if idade >= 65:
       return ('''                  
Paciente n°: {numero}                                 
Nome: {nome}
e-mail: {e_mail}
CPF: {cpf}
RG: {rg}
Telefone: {telefone}
Data de Nacimento: {data_nascimento}
PACIENTE PERTENCE AO GRUPO DE RISCO
        ''')
    else: 
     return (''' 
Paciente n°: {numero}                                      
Nome: {nome}
e-mail: {e_mail}
CPF: {cpf}
RG: {rg}
Telefone: {telefone}
Data de Nacimento: {data_nascimento}  
''')
