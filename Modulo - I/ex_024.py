'''
024.Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
    A) A mensagem "Aprovado", se a média alcançada for maior ou igual 
    a sete;
    B) A mensagem "Reprovado", se a média for menor do que sete;
    C) A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''


nota_1 = float(input('A primeira nota: '))
nota_2 = float(input('A segunda nota: '))
média = (nota_1+nota_2)/2

Informacao = ''
if média >= 7 and média <= 9:
    Informacao = f'Aprovado com {média}'
elif média >= 0 and média <= 6:
    Informacao = f'Reprovado com {média}'
elif média == 10:
    Informacao = f'Aprovado com Distinção a sua média é: {média}'
else:
    Informacao = f'Dados Invalidos!'
print(Informacao)
