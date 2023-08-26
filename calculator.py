print("- André Falcão")

from math import factorial
from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

command = ""
while True:
    command = input("> ").lower()

    if command == "vetor2d":
        print("Vetor no plano selecionado.")
        print("Ponto A")
        x1 = float(input("x= "))
        y1 = float(input("y= "))
        print("Ponto B")
        x2 = float(input("x= "))
        y2 = float(input("y= "))
        print((x2 - x1, y2 - y1))
    elif command == "vetor3d":
        print("Vetor no espaço selecionado.")
        print("Ponto A")
        x1 = float(input("x= "))
        y1 = float(input("y= "))
        z1 = float(input("z= "))
        print("Ponto B")
        x2 = float(input("x= "))
        y2 = float(input("y= "))
        z2 = float(input("z= "))
        print((x2 - x1, y2 - y1, z2 - z1))

    elif command == "distancia2d":
        print("Distância entre dois pontos no plano selecionado.")
        print("Ponto A")
        x1 = float(input("x= "))
        y1 = float(input("y= "))
        print("Ponto B")
        x2 = float(input("x= "))
        y2 = float(input("y= "))
        print(((x2 - x1) ** 2 + (y2 - y1) ** 2))
    elif command == "distancia3d":
        print("Distância entre dois pontos no espaço selecionado.")
        print("Ponto A")
        x1 = float(input("x= "))
        y1 = float(input("y= "))
        z1 = float(input("z= "))
        print("Ponto B")
        x2 = float(input("x= "))
        y2 = float(input("y= "))
        z2 = float(input("z= "))
        print(((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2))

    elif command == "pontomedio2d":
        print("Ponto médio de um segmento de reta no plano selecionado.")
        print("Ponto A")
        x1 = float(input("x= "))
        y1 = float(input("y= "))
        print("Ponto B")
        x2 = float(input("x= "))
        y2 = float(input("y= "))
        print(((x1 + x2) / 2, (y1 + y2) / 2))
    elif command == "pontomedio3d":
        print("Ponto médio de um segmento de reta no espaço selecionado.")
        print("Ponto A")
        x1 = float(input("x= "))
        y1 = float(input("y= "))
        z1 = float(input("z= "))
        print("Ponto B")
        x2 = float(input("x= "))
        y2 = float(input("y= "))
        z2 = float(input("z= "))
        print(((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2))

    elif command == "mediatriz2d":
        print("Plano mediador de um segmento de reta no plano selecionado.")
        print("Ponto A")
        x1 = float(input("x= "))
        y1 = float(input("y= "))
        print("Ponto B")
        x2 = float(input("x= "))
        y2 = float(input("y= "))
        print(expand((x - x1) ** 2 + (y - y1) ** 2 - ((x - x2) ** 2 + (y - y2) ** 2)))
    elif command == "mediador3d":
        print("Plano mediador de um segmento de reta no espaço selecionado.")
        print("Ponto A")
        x1 = float(input("x= "))
        y1 = float(input("y= "))
        z1 = float(input("z= "))
        print("Ponto B")
        x2 = float(input("x= "))
        y2 = float(input("y= "))
        z2 = float(input("z= "))
        print(expand((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2 - ((x - x2) ** 2 + (y - y2) ** 2 + (z - z2) ** 2)))

    elif command == "calculadora":
        calc = input("Escreve uma conta:\n")
        print(str(eval(calc)))

    elif command == "tpascal":
        print("Triângulo De Pascal selecionado")
    n = int(input("Número de níveis = "))
    for i in range(n):
        for j in range(n - i + 1):
            print(end="")
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()

    elif command == "ajuda":
    print("""
    vetor2d - Vetor no plano (xy).
    vetor3d - Vetor no espaço (xyz).
    distancia2d - Distância entre dois pontos no plano (xy).
    distancia3d - Distância entre dois pontos no espaço (xyz).
    pontomedio2d - Ponto médio de um segmento de reta no plano (xy).
    pontomedio3d - Ponto médio de um segmento de reta no espaço (xyz).
    mediatriz2d - Mediatriz de um segmento de reta no plano (xy).
    mediador3d - Plano mediador de um segmento de reta no espaço (xyz).
    calculadora - Calculadora de operções básicas.
    sair - Para sair.
        """)

elif command == "sair":
break
else:
print("Comando não reconhecido, para mais ajuda escreva 'ajuda'.")
