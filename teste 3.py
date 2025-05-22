con = 1
número = int(input("Insira um valor:"))

while con <= 10:
    resultado = número * con

    print(f"{número} * {con} = {resultado}")
    con += 1
# 1)A

t = int(input("insira um valor: "))

for i in range(1,11):
    print(f"{t} * {i} = {t * i}")
# 1)B

numero = int(input("Insira um número inteiro e positivo: "))
if numero <= 0:
    print("esse número não é positivo")
