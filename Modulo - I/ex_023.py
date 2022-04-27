'''
23.Faça um Programa que verifique se uma letra digitada 
é vogal ou consoante. 
'''
letras = str(
    input('Verifique se uma letra digitada é vogal ou consoante:')).strip()
if letras in 'AaEeIeOoUu':
    print(f'Vogais: {letras}')
else:
    print(f'Consoantes {letras}')
