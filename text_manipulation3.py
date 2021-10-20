city = input('Qual cidade você mora? ').strip()
print('A cidade que você mora começa com "São"? {}'.format(city[:3].upper() == 'SÃO'))
nome = input('Qual é seu nome? ')
print('Existe "Silva" no seu nome? {}'.format('SILVA' in nome.upper()))