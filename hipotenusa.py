# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

catOposto = float(input('Comprimento do cateto oposto: '))
catAdjacente = float(input('Comprimento do cateto adjacente: '))

hit = math.hypot(catOposto, catAdjacente)

print('A hipotenusa vai medir {:.2f}'.format(hit))
