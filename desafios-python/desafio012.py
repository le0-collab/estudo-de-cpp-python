print('\033[32m<>' * 10)
print('\033[32mAlistamento')
print('\033[32m<>' * 10)
idade = int(input('Qual é a sua idade? '))
data = 2026 - idade
if data >= 2009:
  print('\033[30mvocê ainda irá se alistar no exército')
  cal1 = data - 2008
  print('Falta {} ano(s) para você se alistar!' .format(cal1))
elif data == 2008:
  print('\033[30mestá na hora de se alistar para o exército')
elif data <= 2007:
  print('\033[31mSeu tempo de se alistar já passou')
  cal = data - 2008
  print('O prazo de alistamento da sua idade foi a {} ano(s)!' .format(cal))