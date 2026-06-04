num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
if num1 > num2:
  print('\033[32mO primeiro número é maior!')
elif num2 > num1:
  print('\033[32mO segundo número é maior!')
else:
  print('\033[31mNão existe valor maior, os dois número são iguais! ')