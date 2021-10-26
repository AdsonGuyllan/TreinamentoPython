c = ''
soma = cont = media = maior = 0
while c in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    c = str(input('Deseja continuar [S/N] ? ')).strip().upper()
    soma += n
    media = soma / cont
    if cont == 1:
        maior = n
    elif n > maior:
        maior = n
    if cont == 1:
        menor = n
    elif n < menor:
        menor = n
print('A média dos números é {:.2f}, o maior número é {} e o menor é {}.'.format(media, maior, menor))