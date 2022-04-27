'''
13.Crie um programa que leia o nome completo de uma pessoa e mostre:
a) O nome com todas as letras maiúsculas e minúsculas.
b) Quantas letras ao todo (sem considerar espaços).
c) Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o nome completo: ')).strip()
print(f'{nome.upper()}\n{nome.lower()}')
print(f'{len(nome)-nome.count(" ")}')
dados = nome.split()
print(f'O primeiro nome tem {len(dados[0])} letras')
