nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('\033[34mA sua média foi {}' .format(media))
if media <= 5.0:
  print('\033[31mReprovado')
elif 5.1 <= media <= 6.9:
  print('\033[33mRecuperação')
elif media >= 7.0:
  print('\033[32mAprovado')