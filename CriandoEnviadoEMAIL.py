# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:36:31 2023

@author: Wilian
"""

import smtplib
import ssl
import email.message


setor = 'B'
msg = email.message.Message()
msg['Subject'] = f'Planilha Financeiro para o departamento : {setor}'
nome = 'Equipe do Financeiro'
body = f'''
Ola, {nome}
Segue em anexo a planilha com os resultados desse mes
Atenciosamente,
Gerente ADM
'''

msg['From'] = 'willcoura@outlook.com'
msg['To'] = 'willcoura@gmail.com'
password = 'Muitobom111!'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)

context = ssl.create_default_context()
with smtplib.SMTP('smtp-mail.outlook.com', 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(msg['From'],password)
    conexao.sendmail(msg['From'],msg['To'], msg.as_string().encode('utf-8'))
