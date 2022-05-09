'''
037. Desenvolva um programa que leia o nome, idade e sexo de 
4 pessoas. No final do programa, mostre: a média de idade
 do grupo, qual é o nome do homem mais velho e quantas mulheres 
 têm menos de 20 anos.
'''
médiadeidade = 0
NomeHomemMaisVelho = ''
totalMulher = 0
idadeMaior = 0

for cont in range(1, 2+1):
    nome = str(input('Nome completo: '))
    idade = int(input('Sua Idade'))
    sexo = str(input('Sexo:'))

    if idade >= 21:
        NomeHomemMaisVelho = nome
        idade = idadeMaior
    else:
        if nome == NomeHomemMaisVelho or idade == idadeMaior:
            NomeHomemMaisVelho = nome
            idadeMaior = idade

        if sexo in 'Mm' and idade <= 20:
            totalMulher += 1

    médiadeidade += cont/4
print('--'*19)
print(f'Homem Mais Velho e {NomeHomemMaisVelho}, com idade {idadeMaior}')
print(f'total de Mulher com menor de idade sao: {totalMulher}')
print(f'média de idade geral e {médiadeidade}')
