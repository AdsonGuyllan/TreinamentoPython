from datetime import date
cont = 0
cont2 = 0
for c in range(7+1):
    ano = int(input('Em que ano você nasceu? '))
    if date.today().year - ano < 18:
        cont += 1
    else:
        cont2 += 1
print('Sobre os anos informados: Existem {} menores de idade e {} maiores de idade'.format(cont, cont2))