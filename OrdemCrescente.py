"""
5o Escreva um código que receba 3 números inteiro e os exiba em ordem crescente
"""
lista = []
contador = 0

while contador != 3:
    numero = int(input(""))
    lista.append(numero)
    contador += 1

crescente = sorted(lista)
print(crescente)

