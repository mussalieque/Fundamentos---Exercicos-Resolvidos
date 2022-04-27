'''
Faça um Programa que peça um valor e mostre na tela se 
o valor é positivo ou negativo. 
'''


num = float(input('Valor por favor: '))
if num >= 0:
    print(f'O valor e {num:.0f} positivo')
else:
    print(f'O valor e {num:.0f} negativo')
