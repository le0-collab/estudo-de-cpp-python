n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))
n3 = int(input('terceiro número: '))
if n1 < n2 > n3:
  print('segundo número é o maior' .format(n2))
if n2 < n1 > n3:
  print('primeiro número é o maior' .format(n1))
if n1 < n3 > n2:
  print('terceiro número é o maior' .format(n3))
if n2 > n1 < n3:
  print('primeiro número é o menor' .format(n1))
if n1 > n2 < n3:
  print('segundo número é o menor' .format(n2))
if n2 > n3 < n1:
  print('terceiro número é o menor' .format(n3))