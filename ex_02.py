# 2) Desenvolva um programa que leia um número inteiro. Se o número informado for positivo, imprimir sua raiz quadrada;
# se for negativo, o quadrado do número.

x = int(input("Informe qualquer número: "))

if x > 0:
    # x elevado a 1/2 ou 0.5 = raiz quadrada
    calculo = x ** 0.5
    print(f"A raiz do número é {calculo:.2f}")
else:
    calculo = x ** 2
    print(f"O quadrado do número é {calculo:.0f}")

print("Fim.")