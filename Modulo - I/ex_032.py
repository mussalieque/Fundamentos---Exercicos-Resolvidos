'''
Crie um programa que mostre na tela todos 
os números pares que estão no intervalo entre 1 e 50. 
'''

s = t = 0
for num in range(1, 51):
    if num % 2 == 0:
        print(num)
