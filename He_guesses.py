#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print('-=-' * 20)
print('Sou seu computador... Acaabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
print('-=-' * 20)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Maiss... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou!!! com {} palpites. Parabéns'.format(palpites))
