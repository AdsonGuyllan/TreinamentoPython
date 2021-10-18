import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terciero aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteio = (random.choice(lista))
print('Quem fará a apresentação do grupo será o {}'.format(sorteio))
random.shuffle(lista)
print('E a ordem da apresentaçõa será ')
print (lista)