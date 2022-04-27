'''
11.Um professor quer sortear um dos seus quatro alunos para apagar 
o quadro. Faça um programa que ajude ele, lendo o nome 
dos alunos e escrevendo na tela o nome do escolhido.
'''

from random import choice

nome_1 = str(input('Nome 1:'))
nome_2 = str(input('Nome 2:'))
nome_3 = str(input('Nome 3:'))
nome_4 = str(input('Nome 4:'))
dados = [nome_1, nome_2, nome_3, nome_4]
d = choice(dados)
print(d)
