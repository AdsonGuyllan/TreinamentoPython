print('~~~~~~ TABUADA ~~~~~~')
while True:
    n   = int(input('Digite um número: '))
    if n < 0:
        break
    print('~' *15)
    for t in range(1, 11):
        print(f'{n} x {t} = {n*t}')
    print('~' *15)
print('PROCESSO ENCERRADO')