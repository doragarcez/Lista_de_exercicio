"""
2o Escreva um código que receba qual será sua idade no ano atual e retorne o ano do seu
nascimento
"""
from datetime import date

anoAtual = date.today().year
idade = int(input("Escreva a idade que fez/fará esse ano:"))
anoNascimento = anoAtual - idade

print("O ano de seu nascimento foi em", anoNascimento)