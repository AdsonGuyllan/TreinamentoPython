print('PAGAMENTO')
pro = float(input('Qual o valor do produto? '))
print('FORMAS DE PAGAMENTO')
print('Selecione a forma de pagamento de acordo com seu número correspondente \n'
      '1: À vista no dinheiro \n'
      '2: À vista no cartão \n'
      '3: Parcelado 2x no cartão \n'
      '4: Parcelado 3x ou mais no cartão')
paga = int(input('Qual forma deseja pagar: '))
if paga == 1 or paga == 2:
    print('Pagamento selecionado: À vista')
    if paga == 1:
        desc = pro * 0.1
        total = pro - desc
        print('A forma de pagamento foi: À vista no dinheiro e'
              ' o valor final do produto ficou {} reais com o desconto de 10%'.format(total))
    else:
        desc = pro * 0.05
        total = pro - desc
        print('A forma de pagamento foi: À vista no cartão e'
              ' o valor final do produto ficou {} reais com o desconto de 5%'.format(total))
else:
    print('Pagamento selecionado: Parcelado')
    if paga == 3:
        print('A forma de pagamento foi: Parcelado em 2x no cartão e'
              ' o valor final do produto ficou {} reais '.format(pro))
    else:
        juros = pro * 0.2
        total4 = pro + juros
        print('A forma de pagamento foi: Parcelado em 3x ou mais no cartão e'
              ' o valor final do produto ficou {} reais com os juros de 20%'.format(total4))