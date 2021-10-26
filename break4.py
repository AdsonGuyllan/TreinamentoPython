print('### Cadastro ###')
cont_t = cont_m = t_maior = cont_f = f_menor = 0
while True:
    s = str(input('Sexo [M/F] ')).strip().upper()[0]
    while s not in 'MF':
        s = str(input('Sexo [M/F]')).strip().upper()[0]
    i = int(input('Idade: '))
    if s == 'M' and i >= 18:
        cont_m +=1
        t_maior += 1
    elif s == 'M' and i < 18:
        cont_m +=1
    elif s == 'F' and i >= 18:
        cont_f +=1
        t_maior +=1
    elif s =='F' and i < 18:
        cont_f += 1
        f_menor +=1
    cont_t += 1
    cont = str(input('Deseja continuar [S/N] ? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N] ? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Um total de {cont_t} pessoas foram cadastradas')
print(f'{cont_m} homens foram cadastrados')
print(f'{cont_f} mulheres foram cadastradas')
print(f'{t_maior} pessoas maiores de idade foram cadastradas')
print(f'{f_menor} mulheres menores de idade foram cadastradas')