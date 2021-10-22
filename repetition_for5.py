frase = str(input('Digite a frase: ')).strip().upper()
sep = frase.split()
junt = ''.join(sep)
inv = ''
for le in range(len(junt) -1, -1, -1):
    inv += junt[le]
print('O inverso de {} é {}'.format(junt, inv))
if inv == junt:
    print('Essa frase é palindromo!')
else:
    print('Essa frase não é palindromo!')