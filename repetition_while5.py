print('~'*10)
print('FIBONATI',)
print('~'*10)
n = int(input('Informe a quantidade de termos que deseja ver: '))
c = 0
d = 1
print('{} > {}'.format(c, d), end=' ')
cont = 3
while cont <= n:
    e = c + d
    print(' > {}'.format(e), end=' ')
    c = d
    d = e
    cont += 1