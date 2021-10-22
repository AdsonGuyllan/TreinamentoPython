import random
print('########### JOGO DA ADIVINHAÇÃO ###########')
cont = 1
eu = int(input('Adivinhe que número estou pensando entre 1 e 10. '
               'Escolha um número: '))
comp = random.randint(1, 10)
while eu != comp:
    eu = int(input('ERRRRROU. Tente novamente: '))
    cont += 1
print('PARÉNS! Você acertou, o número realmente era \33[7m  {}  \33[m '
      'e você precisou de {} chance(s) para acertar'.format(comp, cont))