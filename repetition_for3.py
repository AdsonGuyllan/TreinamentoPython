ni = int(input('Digite o inicio da contagem: '))
nf = int(input('Digite o final da contagem: '))
for c in range(ni, nf+2):
    if c % 2 == 0:
        print(c, '.', end=' ')