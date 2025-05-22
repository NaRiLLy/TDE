# 1° questão
X = int(input("insira um valor:"))

valor = X%2

if valor == 0:
    print("é um número par")

elif valor == 1:
    print("é um número ímpar")

# 2° questão
Y = int(input("insira um valor:"))

if Y < 0:
    print("é um número negátivo")

elif Y > 0:
    print("é um número positivo")

elif y == 0:
    print("é zero")

# 3° questão


# 4° questão

A = int(input("coloque um número para A:"))
B = int(input("coloque um número para B:"))
C = int(input("coloque um número para C:"))

if A != C:
    print("este triângulo é isósceles")

elif A != C != B:
    print("este triângulo é escaleno")

elif A == B == C:
    print("este triângulo é equilátero")