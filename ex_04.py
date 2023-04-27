# 4) Desenvolver um programa que receba como entrada três números. Determinar qual entre estes três números é o maior.

x = float(input("Informe três números. Insira apenas o primeiro número pensado: "))
y = float(input("Insira o segundo número: "))
z = float(input("Insira o terceiro número: "))

if (x > y) and (x > z):
    maiorNumero = x
elif (y > x) and (y > z):
    maiorNumero = y
else:
    maiorNumero = z

print(f"O número {maiorNumero:.1f} é o maior dentre os três inseridos.")

print("Fim!")