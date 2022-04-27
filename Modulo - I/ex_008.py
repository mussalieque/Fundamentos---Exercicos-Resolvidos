'''
0.9.Faça um programa que calcule um número Inteiro 
qualquer e mostre na tela a sua tabuada.
'''
num = int(input('Digite o numero Inteiro: '))
for i in range(1, 10+1):
    m = i * num
    print(f'{num} x {i:2} = {m:2}')
