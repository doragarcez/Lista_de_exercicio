"""
1o (RETIRADO DO SLIDE) Escreva um código que receba 3 valores inteiro (a, b e c). Utilize
esses valores para encontrar o valor de delta.

Caso o valor de delta seja menor que zero, informar que a equação não possui raízes reais.
Se for maior ou igual a zero, encontre e informe os valores de x1 e x2.
Para raiz quadrada precisaremos importar a biblioteca “math” e usar o comando math.sqrt().
"""
import math

a = int(input())
b = int(input())
c = int(input())

delta = b**2 - (4*a*c)

if delta >= 0:
    delta = math.sqrt(delta)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print("X1 = ", x1)
    print("X2 = ", x2)
else:
    print("A equação não possui raízes reais")


