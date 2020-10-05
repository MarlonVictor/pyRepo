## Faça um programa para solicitar o nome e as duas notas e um aluno. Calcular sua média e informá-la. Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado".

aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Agora informe a nota da primeira avaliação: '))
nota2 = float(input('Agora informe a nota da segunda avaliação: '))
media = (nota1 + nota2) / 2

print()
print('Media: ', media)

if media < 7:
    print('O Aluno foi reprovado!')
else:
    print('Parabéns {}, você foi aprovado(a)'.format(aluno))