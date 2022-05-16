num = 1
som = total = 0

while num != -1:
    num = int(input('Digite o numero: '))
    if num != -1:
        som += num
        total += 1

print(f'Soma e {som}, total {total}')
