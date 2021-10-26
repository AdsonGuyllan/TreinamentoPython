cont = t = n = 0
n = int(input('Digite um número [99 para parar]: '))
while True:
    t += n
    cont += 1
    n = int(input('Digite um número [99 para parar]: '))
    if n == 99:
        break
print(f'A quantidade de números digitados foi {cont} e a soma de todos ele é {t}')
print('FIM')