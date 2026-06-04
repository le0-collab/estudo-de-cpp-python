print('\033[34m''-='*20)
print('\033[1;36mAnalisador de Triângulos')
print('\033[34m''-='*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
  print('\033[1;32;40mOs segmentos acima PODEM FORMAR triângulo!')
else:
  print('\033[1;31;40mOs segmentos acima NÃO PODEM FORMAR triângulo!')