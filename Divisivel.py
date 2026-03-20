"""
6o Escreva um código que receba um valor inteiro e diga se ele é divisível por cinco.
"""
valor = int(input(""))
resto = valor % 5

if resto == 0:
    print(valor, "é divisível por 5.")
else:
    print(valor, "não é divisível por 5.")