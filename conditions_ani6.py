import random
print('================= JOKENPÔ =================')
eu = int(input('Escolha 1 para PEDRA, 2 para PAPEL ou 3 para TESOURA: '))
p = 'PEDRA'
pp = 'PAPEL'
t = 'TESOURA'
lista = [p, pp, t]
comp = random.choice(lista)
if eu == 1 and comp == p or eu == 2 and comp == pp or eu == 3 and comp == t:
    print('EMPATE, ambos escolheram {}'.format(comp))
elif eu == 1 and comp == t or eu == 2 and comp == p or eu == 3 and comp == pp:
    if eu == 1 and comp == t:
        print('Você escolheu PEDRA e o computador escolheu {}, ou seja...'.format(comp))
        print('VOCÊ VENCEU')
    elif eu == 2 and comp == p:
        print('Você escolheu PAPEL e o computador escolheu {}, ou seja...'.format(comp))
        print('VOCÊ VENCEU')
    else:
        print('Você escolheu TESOURA e o computador escolheu {}, ou seja...'.format(comp))
        print('VOCÊ VENCEU')
elif eu == 1 and comp == pp or eu == 2 and comp == t or eu == 3 and comp == p:
    if eu == 1 and comp == pp:
        print('Você escolheu PEDRA e o computador escolheu {}, ou seja...'.format(comp))
        print('VOCÊ PERDEU')
    elif eu == 2 and comp == t:
        print('Você escolheu PAPEL e o computador escolheu {}, ou seja...'.format(comp))
        print('VOCÊ PERDEU')
    else:
        print('Você escolheu TESOURA e o computador escolheu {}, ou seja...'.format(comp))
        print('VOCÊ PERDEU')
elif eu != 1 and eu != 2 and eu != 3:
    print('\33[7m Error \33[m ESCOLHA UM NÚMERO ENTRE OS ESPECIFICADOS')