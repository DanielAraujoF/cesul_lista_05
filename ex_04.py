# 4) Desenvolver um programa que receba como entrada três números. Determinar qual entre estes três números é o maior.

x = int(input("Informe três números. Insira apenas o primeiro número pensado: "))
y = int(input("Insira o segundo número: "))
z = int(input("Insira o terceiro número: "))

if (x > y) and (x > z):
    maiorNumero = x
elif (y > x) and (y > z):
    maiorNumero = y
elif (z > x) and (z > y):
    maiorNumero = z

print(f"O número {maiorNumero:.0f} é o maior dentre os três inseridos.")

print("Fim!")