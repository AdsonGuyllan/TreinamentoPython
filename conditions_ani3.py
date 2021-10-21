print('Forma um triângulo')
a = int(input('Digite o tamanho do primeiro lado: '))
b = int(input('Digite o tamanho do segundo lado: '))
c = int(input('Digite o tamanho do terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('Os tamanhos dos lados informados formam um triângulo')
    if a == b and a == c:
        print('E o triângulo formado é um Equilátero')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('E o triângulo formado é um Isósceles')
    else:
        print('E o triângulo formado é um Escaleno')
else:
    print('Os tamanhos dos lados informados não formam um triângulo')