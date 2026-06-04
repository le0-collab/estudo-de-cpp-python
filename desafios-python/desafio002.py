km = int(input('quantos km o carro esteve? '))
print('o carro esteve a {}km' .format(km))
if km >= 80:
    multa = (km - 80) * 7
    print('você levou uma multa no valor de {}$ pelo excesso de velocidade! '.format(multa))