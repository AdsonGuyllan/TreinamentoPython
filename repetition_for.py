print('==== TABUADA ====')
n = int(input('Digite um número: '))
for c in range(1, 11):
    t = n * c
    print('{} x {} = {}'.format(n, c, t))
