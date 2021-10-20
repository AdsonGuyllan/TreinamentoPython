nome = str(input('Digite seu nome: ')).strip()
nomediv = nome.split()
print('Seu primeiro nome é: {}, e o último é {}'.format(nomediv[0], nomediv[len(nomediv) - 1]))