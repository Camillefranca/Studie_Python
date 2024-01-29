#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o valor do seu salário atual?R$ '))
novo = salario + (salario * 15 / 100)

print('Seu novo salário de {:.2f} recebeu um aumento de 15% e ficou {:.2f}'.
      format(salario, novo))
