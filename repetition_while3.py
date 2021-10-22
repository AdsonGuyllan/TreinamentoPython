c = 0
n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))
while c != 5:
    menu = print('______________________________\n'
                 '### MENU ### \n'
                 '    [1] Somar \n'
                 '    [2] Multiplicar \n'
                 '    [3] Maior \n'
                 '    [4] Novos números \n'
                 '    [5] Sair do programa \n')
    c = int(input('Escolha o que deseja fazer com os números informados seguindo o MENU: '))
    if c == 1:
        print('Opção "Soma" selecionada')
        soma = n1 + n2
        print('A soma de {} com {} é igual a {}'.format(n1, n2, soma))
    elif c == 2:
        print('Opção "Multiplicação" selecionada')
        mult = n1 * n2
        print('A soma de {} com {} é igual a {}'.format(n1, n2, mult))
    elif c == 3:
        print('Opção "Maior" selecionada')
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        elif n1 < n2:
            print('O maior número é {}'.format(n2))
        else:
            print('Os números informados são iguais')
    elif c == 4:
        n1 = int(input('Informe outro valor: '))
        n2 = int(input('Informe outro valor novamente: '))
print('Programa finalizado')
