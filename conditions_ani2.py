print('===Calcule sua média===')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
total = float (n1 + n2 + n3) // 3
print('Sua média é {}'.format(total))
if total < 5.0:
    print('VOCÊ ESTÁ REPROVADO')
elif total >= 5.0 and total <7.0:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO')
else:
    print('VOCÊ ESTÁ APROVADO, PARABÉNS!')