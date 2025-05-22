lista_a = []

for i in range(10):
    lista = input(f"Digite o valor {i + 1}: ")
    lista_a.append(lista)

maior_valor = max(lista_a)
menor_valor = min(lista_a)

print("maior valor da lista é: ", maior_valor)
print("mmenor valor da lista é: ", menor_valor)