# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:40:51 2023

@author: Wilian
"""
def registro(arquivo,idade,nome,email,cpf,rg,telefone,data_nascimento):
    if idade < 65:
        arquivo.write(f'''
            'Nome': {nome}
            'E-mail': {email}
            'CPF': {cpf}
            'RG': {rg}
            'Telefone': {telefone}
            'Data de Nascimento': {data_nascimento}
            ''')
    else:
         arquivo.write(f'''
             'Nome': {nome}
             'E-mail': {email}
             'CPF': {cpf}
             'RG': {rg}
             'Telefone': {telefone}
             'Data de Nascimento': {data_nascimento}
             ''')
def pacientes():
    with open('teste20000.txt','a') as f:
        x = int(input('Digite 1 para Registrar '))
        while x == 1:
            nome = input('Insira seu nome completo: ')
            email = input('insira seu e-mail: ') 
            cpf = input('Insira seu cpf, formato 000.000.000-00: ')
            rg = input('Insira seu rg,formato 0.000.000: ')
            telefone = input('Insire seu telefone de contato,formato (dd) 0-0000-0000: ')
            data_nascimento = input('Insira sua data de nascimento,(Formato dia/mes/ano): ')
            ano_nascimento = int(data_nascimento[6:10])
            idade = 2023 - ano_nascimento
            registro(f,idade,nome,email,cpf,rg,telefone,data_nascimento)
            x = int(input('Digite 1 para realizar mais registros '))
    with open('teste20000.txt', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
        
if __name__ == '__main__':
    pacientes()