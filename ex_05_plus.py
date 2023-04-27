# 5) Desenvolva um programa que receba três valores inteiros, e determine se o menor valor é par.

x = int(input("Insira um número: "))
y = int(input("Insira um segundo número: "))
z = int(input("Insira um terceiro número: "))

if x < y and x < z:
    if x % 2 == 0:
        menorNum = x
    else:
        menorNumImpar = x

elif y < x and y < z:
    if y % 2 == 0:
        menorNumPar = y
    else:
        menorNumImpar = y

else:
    if z % 2 == 0:
        menorNum = z
    else:
        menorNumImpar = z

if x < y and x < z:
    menroNumero = x

elif y < x and y < z:
    menorNumero = y

else:
    menorNumero = z

print(f"O menor número é {menorNumPar:.0f}, e ele é par")

print(f"O menor número é {menorNumImpar:.0f}, e ele é impar")