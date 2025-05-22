lista = []
alunos = input(str("Coloque a quantidade de alunos: "))
abaixo_da_média = 0
acima_da_média = 0

for i in range(int(alunos)):
    a = int(input(f"digite a média do aluno {i + 1}: "))
    lista.append(a)

    if a <= 59:
        abaixo_da_média += 1
    else:
        acima_da_média += 1

print("Alunos abaixo da média são: ", abaixo_da_média)
print("Alunos acima da média são: ", acima_da_média)

