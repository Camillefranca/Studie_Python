#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


d = int(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(d))
p = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(p))




