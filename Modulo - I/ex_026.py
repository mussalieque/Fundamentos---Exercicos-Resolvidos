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

categoria = ''
nascimento = int(input('Por favor digite o ano de nascimento de atleta:'))
data = (date.today().year) - nascimento
if data >= 1 and data <= 9:
    categoria = f'MIRIM'
elif data >= 10 and data <= 14:
    categoria = f'INFANTIL'
elif data >= 15 and data <= 19:
    categoria = f'JÚNIOR'
elif data >= 20 and data <= 25:
    categoria = f'SÊNIOR'
else:
    categoria = f'MASTER'
print(f'{categoria} {data} de Idade')
