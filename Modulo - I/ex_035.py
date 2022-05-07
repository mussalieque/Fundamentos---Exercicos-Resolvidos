'''
035. Crie um programa que leia o ano de nascimento de
 quatro pessoas. No final, mostre quantas pessoas ainda
  não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
from http.client import CONTINUE
from tkinter import E

maioridade = 0
menoridade = 0

for cont in range(1, 4+1):
    actual = date.today().year
    nascimento = int(input('Digite nascimento: '))
    idade = actual - nascimento
    cont += 1
    if idade < 18:
        menoridade += 1
    else:
        maioridade += 1


print(f'maioridade : {maioridade}')
print(f'menoridade : {menoridade}')
