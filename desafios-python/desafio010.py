print('\033[35m<>' *20)
print('\033[36mCONVERTOR DE NÚMEROS')
print('\033[35m<>\033[34m' *20)
num = int(input('Digite um número: '))
converter = int(input(' 1 para binário \n 2 para octal \n 3 para exadecimal \n digite o número: '))
if converter == 1:
  print(bin(num))
elif converter == 2:
  print(oct(num))
elif converter == 3:
  print(hex(num))
else:
  print('\033[31mErro! Digite um dos três números acima para converter!')