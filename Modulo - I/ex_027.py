'''
027. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida 
'''
faixa = ''
peso = float(input('Peso(kg):'))
altura = float(input('altura(massa): '))
IMC = peso/pow(altura, 2)
if IMC >= 0 and IMC < 18.5:
    faixa = f'Peso normal!'
elif IMC >= 18.5 and IMC < 25:
    faixa = f'Peso Ideal!'
elif IMC >= 25 and IMC < 30:
    faixa = f'Peso Sobrepeso!'
elif IMC >= 30 and IMC < 40:
    faixa = f'Peso Sobrepeso!'
elif IMC >= 40:
    faixa = f'Obesidade Mórbida '
print(f'{faixa}, {IMC:.1f}')
