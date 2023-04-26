# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:31:07 2023

@author: Wilian
"""

import pydf

pdf = pydf.generate_pdf('<h1>Meu pdf gerado com python</h1>')
with open('meu_pdf.pdf','wb') as f:
    f.write(pdf)