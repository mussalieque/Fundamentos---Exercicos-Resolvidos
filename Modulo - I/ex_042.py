'''
Faça um programa que leia o sexo de uma pessoa, mas só 
aceite os valores ‘M’ ou ‘F’. Caso esteja errado, 
peça a digitação novamente até ter um valor correto.
'''


sexo = input('Por favor informe o seu sexo [M] ou [F]').strip()
while sexo not in 'MmFf':
    sexo = input(
        'Dados invalido, Por favor informe o seu sexo [M] ou [F]').strip()
print(f'Sexo {sexo} registado com sucesso.')
