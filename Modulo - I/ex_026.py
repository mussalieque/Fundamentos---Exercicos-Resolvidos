'''
026. A Confederação Nacional de Natação precisa de um programa que leia o ano 
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
A) Até 9 anos: MIRIM
B) Até 14 anos: INFANTIL
C) Até 19 anos: JÚNIOR
D) Até 25 anos: SÊNIOR
F) Acima de 25 anos: MASTER
'''
from datetime import date

Informacao = ''
nascimento = int(input('Por favor digite o ano de nascimento:'))
data = (date.today().year) - nascimento
if data >= 1 and data <= 9:
    Informacao = f'MIRIM'
elif data >= 10 and data <= 14:
    Informacao = f'INFANTIL'
elif data >= 15 and data <= 19:
    Informacao = f'JÚNIOR'
elif data >= 20 and data <= 25:
    Informacao = f'SÊNIOR'
else:
    Informacao = f'MASTER'
print(f'{Informacao} {data} de Idade')
