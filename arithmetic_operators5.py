alt = float(input('Quantos metros de altura tem sua parede? '))
lar = float(input('E quantos metros de largura? '))
area =alt * lar
tinta = area / 2
print('Sua parede tem {} m², serão necessarios {} litros de tinta para pinta-la'. format(area, tinta))