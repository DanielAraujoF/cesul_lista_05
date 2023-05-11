# 6) Desenvolva um programa que receba como entrada do usuário as medidas de três lados de um triângulo. O programa
# deverá retornar como saída qual o tipo do triângulo, de acordo com as regras:
# • Triângulo Equilátero possui os três lados com as mesmas medidas.
# • Triângulo Escaleno possui os três lados diferentes
# • Triângulo Isósceles possui dois lados iguais
# Deve-se ainda verificar se as medidas formam um triângulo. Três medidas formam um triângulo quando a soma de dois
# lados for maior do que um terceiro lado.

l1 = float(input("Informe o a medida do primeiro lado: "))
l2 = float(input("Informe o a medida do segundo lado: "))
l3 = float(input("Informe o a medida do terceiro lado: "))

tipo = 1

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    if l1 == l2 and l1 == l3 and l2 == l3:
        tipo = "equilátero"

    elif l1 != l2 and l1 != l3 and l2 != l3:
        tipo = "escaleno"

    else:
        tipo = "isóceles"

else:
    print("Não é um triângulo!")

print(f"As medidas formam um triângulo e é um triângulo {tipo}!")