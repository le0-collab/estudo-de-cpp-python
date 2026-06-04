km = int(input('quantos km foi a viagem? '))
if km <= 200:
  valor = km * 0.50
  print('\033[36mO valor da viagem é \033[32m{}$' .format(valor))
else:
  valor2 = km * 0.45
  print('\033[34mO valor da viagem é \033[32m{}$' .format(valor2))