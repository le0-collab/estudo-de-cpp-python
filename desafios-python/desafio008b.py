salario = float(input('Qual o salário do funcionário: '))
print('\033[36m-='*35)
if salario >= 1251:
  valor = salario * 0.10
  valor1 = salario + valor
  print('Recebeu um aumento de 10% e agora passa receber {}{}$' .format('\033[4;33m', valor1))
print('\033[36m-='*35)
if salario <= 1249:
  v1 = salario * 0.15
  v2 = v1 + salario
  print('{}recebeu um aumento de 15% e agora passa receber {}{}$' .format('\033[35m', '\033[1;32m', v2))
if salario == 1250:
  r1 = salario * 0.15
  r2 = r1 + salario
  print('recebeu um aumento de 15% e agora passa receber {}$' .format('\033[0;31;46m', r2))