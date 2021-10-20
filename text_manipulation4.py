nome = str(input('Digite seu nome: ')).upper().strip()
print('Seu nome possui {} vezes a letra "A"'.format(nome.count('A')))
print('A primeira letra "A" aparece na posição {}'.format(nome.find('A') + 1 ))
print('A última letra "A" está na posiçõa {}'.format(nome.rfind('A') + 1))