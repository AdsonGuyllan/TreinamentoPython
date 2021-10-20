km = int(input('Quantos km terá sua viagem? '))
print('A viagem terá {}km'.format(km))
if km <= 200:
    valor = float(km * 0.5)
    print('O valor da sua viagem será {} reais'.format(valor))
else:
    valor2 = float(km * 0.45)
    print('O valor da sua viagem será {} reais'.format(valor2))