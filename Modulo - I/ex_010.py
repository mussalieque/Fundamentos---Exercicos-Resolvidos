'''
10.Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário,  com 5% de aumento.
'''

salário = float(input('O salário de um funcionário: '))
aumento = salário + (salário * 5/100)
print(f'Antigo salário {salário}, novo aumento:{aumento} ')
