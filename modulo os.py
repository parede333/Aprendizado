# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:17:01 2023

@author: Wilian
"""

import os

# Verificar se um arquivo existe
print(os.path.exists('Exercicio5.py'))

# Exemplo de caminhos

print(os.path.exists('mir4/mir4.txt'))

# Criando arquivos
#os.mkdir('python')
os.mknod('test.txt')
#f = open('mir4/workfil.py','w')
#f.close()
#os.remove('test.py')