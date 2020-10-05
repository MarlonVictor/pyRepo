## Elabore um programa para solicitar o nome de uma equipe de futebol, a quantidade de derrotas, empates e vitórias obtidas por ela no campeonato. No futebol, cada vitória vale três pontos e cada empate vale um ponto. Calcular e informar: a quantidade de pontos ganhos, a quantidade de pontos perdidos e o percentual de aproveitamento da equipe.

time = input('Digite o nome da equipe de futebol: ')
derrotas = int(input('O {} perdeu quantas partidas? '.format(time)))
empates = int(input('Quantos empates? '))
vitórias = int(input('Agora insira o número de vitórias do {} até o momento: '.format(time)))

pontos_ganhos = vitórias * 3 + empates
pontos_perdidos = derrotas * 3 + empates * 2

partidas = derrotas + empates + vitórias
aproveitamento = (pontos_ganhos / (pontos_ganhos + pontos_perdidos)) * 100

print()
print('O {0} disputou {1} jogos'.format(time, partidas))
print('{0} pontos ganhos e {1} pontos perdidos'.format(pontos_ganhos, pontos_perdidos))
print('O aproveitamento do {0} é de {1}%'.format(time, aproveitamento))