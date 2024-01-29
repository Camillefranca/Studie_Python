#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade atual do carro? '))
m = (v - 80) * 7
if v > 80:
  print('MULTADO! Você excedeu o limite que é de 80Km/h')
  print('Você deverá pagar uma multa de R${:.2f}'.format(m))
print('Tenha um bom dia! Dirija com segurança!')


