'''
12. O mesmo professor do desafio 011 quer sortear a ordem de
apresentação de trabalhos dos alunos.Faça um programa que 
leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle

nome_1 = str(input('Nome 1:'))
nome_2 = str(input('Nome 2:'))
nome_3 = str(input('Nome 3:'))
nome_4 = str(input('Nome 4:'))
dados = [nome_1, nome_2, nome_3, nome_4]
shuffle(dados)
print(dados)
