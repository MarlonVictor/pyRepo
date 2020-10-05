## Faça um programa que leia dois números e mostre qual o maior dos dois. O programa deve informar caso sejam iguais.

valor1 = int(input('Digite um número: '))
valor2 = int(input('Agora digite um segundo número: '))

print()
    
if valor1 > valor2:
    print('{0} é maior que {1}'.format(valor1, valor2))
elif valor2 > valor1:
    print('{0} é maior que {1}'.format(valor2, valor1))
else:
    print(' Os dois números digitados são iguais!')