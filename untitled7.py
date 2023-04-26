# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:05:25 2023

@author: Wilian
"""

faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'outros': 19849.53
    }
j = 0
for x in faturamento_mensal.values():
    j += x
percentual = []
for x in faturamento_mensal.values():
    y = (100*x)/j
    percentual.append(y)

print(f'''
      O percentual de SP foi {percentual[0]} %
      O percentual de RJ foi {percentual[1]} %
      O percentual de MG foi {percentual[2]} %
      O percentual de ES foi {percentual[3]} %
      O percentual dos outros estados foram {percentual[4]} %
      ''')
