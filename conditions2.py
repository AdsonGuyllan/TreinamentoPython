import random
print('ADIVINHE O NÚMERO QUE SERÁ SORTEADO')
adv = int(input('Escolha e digite um número entre 1 e 5: '))
lista = 1, 2, 3, 4, 5
sorte = random.choice(lista)
if adv == sorte:
    print('PARABÉNS! você acertou, o número sorteado tbm foi {}'.format(sorte))
else:
    print('QUE PENA, você errou, o número sorteado foi {}'.format(sorte))