cont = t = n = 0
n = int(input('Digite um número [9 para parar]: '))
while n != 9:
    t += n
    cont += 1
    n = int(input('Digite um número [9 para parar]: '))
print('A quantidade de números digitados foi {} e a soma de todos ele é {}'.format(cont, t))
print('FIM')