emprestimo = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Quantos é o seu salário? R$'))
anos0 = float(input('Em quantos anos você vai pagar? '))
pct = salario * 0.30
prestacao = emprestimo / 24
if prestacao > pct:
  print('\033[31mO empréstimo foi negado!')
elif anos0 == 2:
  prestacao2 = emprestimo / 24
  print('\033[32mO empréstimo foi aceito! o valor que deverá pagar é {:.2f}$' .format(prestacao2))
elif anos0 == 3:
  prestacao3 = emprestimo /36
  print('\033[32mO empréstimo foi aceito! o valor que deverá pagar é {:.2f}$'.format(prestacao3))
elif anos0 == 4:
  prestacao4 = emprestimo / 48
  print('\033[32mO empréstimo foi aceito! o valor que deverá pagar é {:.2f}$'.format(prestacao4))