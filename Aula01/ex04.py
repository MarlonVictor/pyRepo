## Faça um programa que obtenha a partir da digitação do usuário os seguintes dados: 
# A quantidade de alunos que fazem o curso de Sistemas de Informação;
# A quantidade de alunos que fazem o curso de Análise de Sistemas;
# Ao final o programa deve informar o total de alunos;
# A procentagem de alunos que fazem Sistemas e a porcentagem de alunosque cursam Análises.

alunosSistemas = int(input('Informe quantos alunos fazem o curso de Sistemas de Informação: '))
alunosAnálises = int(input('Agora informe quantos alunos fazem o curso de Análise de Sistemas: '))

totalAlunos = alunosSistemas + alunosAnálises
percSistemas = (alunosSistemas / totalAlunos) * 100
percAnálises = (alunosAnálises / totalAlunos) * 100

print('Ao todo são', totalAlunos, 'alunos.')
print('{:.2f}%'.format(percSistemas), 'cursam Sistemas e {:.2f}%'.format(percAnálises), 'cursam Análises.')