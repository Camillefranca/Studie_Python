#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#pow()

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n**(1 / 2)
print('O dobro de {} vale {}'.format(n, d))
print('O triplo de {} vale {}, A raiz quadrada de {} é igual a {} '.format(
    n, t, n, r))