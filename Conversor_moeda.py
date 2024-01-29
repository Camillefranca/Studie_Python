#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

R = float(input('Quanto dinheiro voce tem na carteira? \nR$ '))
D = R / 5.18
print('Com R${:.2f} você pode comprar US{:.2f} '.format(R, D))
