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
if data >= 9 and data < 14:
    Informacao = f'MIRIM'


print(f'{Informacao} {data} Idade')
