#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alu1 = str(input('Primeiro aluno: '))
alu2 = str(input('Segundo aluno: '))
alu3 = str(input('Terceiro aluno: '))
alu4 = str(input('Quarto aluno: '))

lista = [alu1, alu2, alu3, alu4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
