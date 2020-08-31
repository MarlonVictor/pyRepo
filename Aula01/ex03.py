## Faça um programa que leia a partir da digitação de um usuário a descrição de um produto, o seu valor unitário e sua quantidade. O programa deve calcular e informar o valor a pagar.

produto = input('Me diz qual é o produto que deseja comprar: ')
valorUni = float(input('Qual o valor unitário desse produto: '))
qtd = int(input('Quantas unidades você comprou? '))

if qtd > 1:
    produto += 's'

total = valorUni * qtd

print('Você comprou', qtd, produto,'. O total a pagar é', total)