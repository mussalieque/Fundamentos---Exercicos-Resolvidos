'''
Crie um programa que leia dois valores e mostre um menu na tela:
'''


num1 = int(input('Digite o numero: '))
num2 = int(input('Digite o numero: '))
op = 1
linha = '*=' * 20
while op != 5:
    print('''[1]=> Adicao\n[2]=> Subtracao\n[3]=> Novamente\n[4]=> Multiplico\n[5]=> Sair''')
    op = int(input('Selecione:'))
    if op == 1:
        s = num1 + num2
        print(s)
        print(linha)
    elif op == 2:
        s = num1 - num2
        print(s)
        print(linha)
    elif op == 3:
        num1 = int(input('Digite o numero: '))
        num2 = int(input('Digite o numero: '))
        print(linha)
    elif op == 4:
        s = num1 * num2
        print(s)
        print(linha)
    elif op == 5:
        print('Obrigado por usar!')
        print(linha)
