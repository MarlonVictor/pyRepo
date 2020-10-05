## Faça um programa que dado o valor da temperatura em graus FARENHEIT, calcular e escrever o valor da temperatura em graus CELSIUS.

F = int(input('Digite uma temperatura em graus FARENHEIT: '))
C = 5/9 * (F - 32)

print('{0} graus FARENHEIT é equivalente a {1} graus CELSIUS'.format(F, C))