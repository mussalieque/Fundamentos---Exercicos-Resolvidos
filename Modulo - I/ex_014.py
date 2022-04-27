'''
14.Crie um programa que leia o nome de uma cidade 
diga se ela começa ou não com o nome “SANTO”.
'''

nome = str(input('nome: ')).strip()
print('santo' in nome.lower())
