## Faça um programa que dado o valor da temperatura em graus FARENHEIT, calcular e escrever o valor da temperatura em graus CELSIUS.

F = int(input('Insira um valor em graus Farenheit: '))
C = round(5/9 * (F - 32))

print('{:.0f}°'.format(F),'Farenheit é equivalente a', C, 'graus Celsius.')