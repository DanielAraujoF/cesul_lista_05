# 5) Desenvolva um programa que receba três valores inteiros, e determine se o menor valor é par.

x = int(input("Insira um número: "))
y = int(input("Insira um segundo número: "))
z = int(input("Insira um terceiro número: "))

menorNumero = 0

if x < y and x < z:
    menorNumero = x

elif y < x and y < z:
    menorNumero = y

else:
    menorNumero = z

if menorNumero % 2 == 0:
    print(f"O menor número é {menorNumero} e ele é par.")
else:
    print(f"O menor número é {menorNumero} e ele é impar.")