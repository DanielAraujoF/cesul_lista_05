# 5) Desenvolva um programa que receba três valores inteiros, e determine se o menor valor é par.

numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira um segundo número: "))
numero3 = int(input("Insira um terceiro número: "))

if numero1 < numero2 and numero1 < numero3:
    if int(numero1 / 2):
        print(f"O menor número é {numero1:.0f}, e ele é par")
else:
    print(f"O menor número é {numero1:.0f}, e ele é impar")

if numero2 < numero1 and numero2 < numero3:
    if int(numero2 / 2):
        print(f"O menor número é {numero2:.0f}, e ele é par")
else:
    print(f"O menor número é {numero2:.0f}, e ele é impar")

if numero3 < numero1 and numero3 < numero2:
    if int(numero3 / 2):
        print(f"O menor número é {numero3:.0f}, e ele é par")
else:
    print(f"O menor número é {numero3:.0f}, e ele é impar")