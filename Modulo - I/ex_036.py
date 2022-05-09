'''
036. Faça um programa que leia o peso de quatro pessoas. No final, 
mostre qual foi o maior e o menor peso lidos.
'''
Maior = 0
Menor = 0

for cont in range(1, 4+1):
    Peso = float(input('Please Peso: '))

    if cont == 1:
        Maior = Peso
        Menor = Peso
    else:
        if Peso > Maior:
            Maior = Peso
        if Peso < Menor:
            Menor = Peso

print('-' * 50)
print(f'Maior {Maior} e Menor {Menor}')
