km = int(input('Qual velocidade seu carro está? '))
print('Carro a {}km/h'.format(km))
if km <= 80:
    print('Velocidade dentro do permitido, continue assim!')
else:
    kms = km-80
    multa = kms * 7
    print('Velocidade acima do permitido, multa de {} reais aplicada!'.format(multa))