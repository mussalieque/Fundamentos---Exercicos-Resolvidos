'''
025.Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso.
'''

print('Turno:\n[M]-matutino]\n[V]-Vespertino\n[N]-Noturno')
turno = str(input('Escolhe turno que você estuda: ')).strip()
Informacao = ''
if turno.upper() == 'M' or turno.lower() == 'matutino':
    Informacao = f'Bom Dia!'
elif turno in 'Vv' or turno.upper() == 'VESPERTINO':
    Informacao = f'Boa Tarde!'
elif turno in 'Nn' or turno.upper() == 'NOTURNO':
    Informacao = f'Boa Noite!'
else:
    Informacao = f'Valor Inválido!'
print(Informacao)
