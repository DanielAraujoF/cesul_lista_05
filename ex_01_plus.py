# 1) Construa um programa que receba dois números do usuário, e retorne como saída a diferença entre o maior e o menor.

x = (int(input("Informe um número: ")))
y = (int(input("Informe mais um número: ")))

if x >= y:
    diferenca = x - y
else:
    diferenca = y - x

print(f"A diferença entre x e y é {diferenca:.0f}. :D")

print("Fim. :D")