ano = int(input('qual ano deseja vereficar? '))
resultado = ano % 4
if resultado == 0:
  print('Esse é um ano bissexto')
else:
  print('esse é um ano comum')