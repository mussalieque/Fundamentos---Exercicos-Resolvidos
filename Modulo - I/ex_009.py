'''
10. Faça um algoritmo que leia o preço de um produto 
e mostre seu novo preço, com 5% de desconto.
'''

preço = float(input('Digite o preço: '))
desconto = preço - (preço * 5/100)
print(f'O preço {preço} de um produto {desconto} ')
