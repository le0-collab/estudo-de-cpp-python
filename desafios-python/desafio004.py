km = int(input('quantos km foi a viagem? '))
if km <= 200:
  valor = km * 0.50
  print('O valor da viagem é {}$'.format(valor))
else:
  valor2 = km * 0.45
  print('O valor da viagem é {}$'.format(valor2))