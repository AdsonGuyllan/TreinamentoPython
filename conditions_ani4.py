print('========CALCULE AQUI SEU IMC========')
alt = float(input('Qual é sua altura? '))
peso = float(input('Qual é seu peso? '))
imc = peso // (alt **2)
print('Seu IMC é de {} e você está'.format(imc))
if imc < 18.5:
    print('Abaixo do peso. Alimente-se!')
elif imc >= 18.5 and imc < 25:
    print('Com o peso ideal. Parabéns!')
elif imc >= 25 and imc < 30:
    print('Com sobrepreso. Cuidado!')
else:
    print('Com obesidade mórbida. Trate-se!')