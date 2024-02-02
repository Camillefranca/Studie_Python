#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

campeonato = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense',
              'Internacional', 'Bragantino', 'Fortaleza', 'Athletico-PR',
              'Atlético-MG', 'São Paulo', 'Cruzeiro', 'Santos', 'Bahia',
              'Corinthians', 'Cuiabá', 'Goiás', 'Vasco', 'América-MG',
              'Coritiba')

print('-=' * 15)
print(f'Lista de times do Brasileirão {campeonato}')
print('-=' * 15)
print(f'Os 5 primeiros são {campeonato[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {campeonato[16:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {(sorted(campeonato))}')
print('-=' * 15)
