print('+++++ ANÁLISE +++++')
soma = 0
media = 0
maisvelho = 0
nomemaisvelho = ''
cont = 0
for a in range(1, 5+1):
    print('=== {}ª PESSOA ==='.format(a))
    nome = str(input('Nome: ').strip().title())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ').strip().upper())
    soma += idade
    if a == 1 and sexo =='M':
        maisvelho = idade
        nomemaisvelho = nome
    elif idade > maisvelho and sexo =='M':
        maisvelho = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        cont += 1
media = soma // a
print('A média de idade do grupo é {} anos'.format(media))
print('O homem mais velho é o {} com {} anos'.format(nomemaisvelho, maisvelho))
print('No grupo existem {} mulheres com menos de 20 anos'.format(cont))