'''
18.Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente. 
'''
nome_full = str(input('Digite o nome completo: ')).strip()
dados = nome_full.split()
print(f'Nome completo: {nome_full}')
print('*'*50)
print(f'O primeiro: {dados[0]},{len(dados[0])} ')
print(f'O último: {dados[-1]}, {len(dados[-1])}')
