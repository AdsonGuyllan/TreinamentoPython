s = str(input('Informe seu sexo: (M/F) ')).upper().strip()[0]
while s not in 'MF':
        s = str(input('Digite o valor conforme o pedido: (M/F) ')).strip().upper()[0]
print('Sexo {} informado'.format(s))