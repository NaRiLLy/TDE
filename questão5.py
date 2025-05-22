ímpar = 0
par = 0
for i in range(5):
    b = int(input(f"digite o valor {i + 1}: "))

    if b %2 == 0:
        par += 1
        print("esse valor é par")
    else:
        ímpar += 1
        print("esse valor é ímpar")

print("números pares: ", par)
print("números impares: ", ímpar)