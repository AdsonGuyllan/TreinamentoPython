maior = 0
menor = 0
for c in range(3+1):
    peso = float(input('Informe seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O menor peso é {}Kg e o Maior é {}Kg'.format(menor, maior))