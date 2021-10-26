import random
v = 0
eu = ''
while True:
    eu = str(input('Escolha Par ou Impar [P/I]: ').strip().upper()[0])
    n_eu = int(input('Escolha um número [0-10]: '))
    comp = random.randint(1, 10)
    print(f'Computador: {comp}')
    jogo = n_eu + comp
    print(f'{n_eu} + {comp} = {n_eu + comp}')
    if eu == 'P' and jogo % 2 == 0 or eu == 'I' and jogo % 2 != 0:
        print('PARABÉNS, Você venceu!!!')
        v += 1
    else:
        print('QUE PENA, Você perdeu!!!')
        break
print(f'Você venceu um total de {v} vezes!')