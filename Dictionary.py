#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['media'] > 7:
    ficha['situação']='Aprovado'
elif ficha['media'] < 5:
    ficha['situação']='Reprovado'
elif 7 > ficha['media'] >= 5:
    ficha['situação']='Recuperação'
print('-=' * 30)
print(f' - nome é igual a {ficha["nome"]}')
print(f' - média é igual a {ficha["media"]}')
print(f' - situação é igual a {ficha["situação"]}')


##################################################################

for k, v in ficha.items():
  print(f'{k} é igual a {v}')
