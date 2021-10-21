casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
tempo = int(input('Em quantos meses quer pagar essa casa? '))
paga = float(casa // tempo)
salarioteste = salario * 0.3
print('A casa custa {} reais e o comprador deseja pagar em {} meses,'
      ' ou seja, cada prestação custará {} reais'. format(casa, tempo, paga))
print('30% do seu salário é {} reais'.format(salarioteste))
if paga > salarioteste:
    print('COMPRA NÃO AUTORIZADA, as prestações ultrapassaram 30% do seu salário.')
else:
    print('COMPRA AUTORIZADA')