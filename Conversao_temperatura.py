#14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input('Informe a temperatura em C°: '))

conversão = ((9 * temperatura) / 5) + 32

print('A temperatura de {}°C corresponde a {}°f'.format(temperatura, conversão))
