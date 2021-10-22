soma = 0
cont = 0
for c in range(1, 6+1):
    n = int(input('Informe o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares, a soma deles é {}'.format(cont, soma))