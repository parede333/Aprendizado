# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:48:15 2023

@author: Wilian
"""
def Rpacientes():
    x = 0
    numero = 0
    f = open('pacientes.txt','w')
    while True:
        x = int(input('Digite 1 para cadastrar um paciente'))
        if x == 1: 
            nome = input('Insira seu nome completo: ')
            e_mail = input('insira seu e-mail: ') 
            cpf = input('Insira seu cpf, formato 000.000.000-00: ')
            rg = input('Insira seu rg,formato 0.000.000: ')
            telefone = input('Insire seu telefone de contato,formato (dd) 0-0000-0000: ')
            data_nascimento = input('Insira sua data de nascimento,(Formato dia/mes/ano): ')
            ano_nascimento = int(data_nascimento[6:10])
            idade = 2023 - ano_nascimento
            numero += 1
            if idade >= 65:
                f.write(f'''                  
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
                f.write(f''' 
Paciente n°: {numero}                                      
Nome: {nome}
e-mail: {e_mail}
CPF: {cpf}
RG: {rg}
Telefone: {telefone}
Data de Nacimento: {data_nascimento}  
            ''')
        else:
            break
    f.close()
    if __name__ == '__main__':
        with open('pacientes.txt') as f:
            read_data = f.read()
            print(read_data)