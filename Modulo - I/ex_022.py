'''
22.Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
'''


digitada = str(input('Verifique se uma letra digitada é "F" ou "M":'))
if digitada in 'Ff' or digitada in 'Mm' or digitada == 'Masculino' or digitada == 'Feminino':
    print(f'O Seu Sexo e : {digitada}.')
else:
    print('Sexo Inválido')
