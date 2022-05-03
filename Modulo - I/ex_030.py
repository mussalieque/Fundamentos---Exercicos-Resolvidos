'''
Escreva um programa em Python que leia um número 
inteiro qualquer e peça para o usuário escolher qual
será a base de conversão:
1 para binário, 
2 para octal e 
3 para hexadecimal. 
'''
informacao = ''
num = int(input('Digite um numero inteiro: '))
print('Selecione um das bases para conversão:\n1=>para binário\n2=>para octal\n3=>para hexadecimal')
opcoes = int(input('Sua opcão:'))
print('-'*40)
if opcoes == 1:
    informacao = f'O número: {num} conversão e: {bin(num)[2:]}'
elif opcoes == 2:
    informacao = f'O número: {num} conversão e: {oct(num)[2:]}'
elif opcoes == 3:
    informacao = f'O número: {num} conversão e: {hex(num)[2:]}'
else:
    informacao = f'Invalido!'
print(informacao)
