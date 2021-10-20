idade = int(input('Qual é sua idade? '))
if idade < 18:
    print('Você é menor de idade por ter só {} anos!'.format(idade))
elif idade >= 18 and idade < 35:
    print('Você é jovem por ter {} anos!'.format(idade))
elif idade >= 35 and idade < 65:
    print('Você é adulto(a) por ter {} anos!'.format(idade))
else:
    print('Você é velho(a) por já ter {} anos!'.format(idade))