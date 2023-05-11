# 8) Uma empresa de desenvolvimento de sistemas trabalha com profissionais em regime de
# prestação de serviços, para os quais é aplicada a seguinte tabela de valores por hora trabalhada:
# |         Função           | Valor/Hora |
# | 1 - Testador             | 20,00      |
# | 2 - Analista de Testes   | 35,00      |
# | 3 - Programador          | 45,00      |
# | 4 - Analista de Sistemas | 40,00      |
# | 5 - DBA                  | 50,00      |
# Desenvolva um programa que receba do usuário a função desempenhada e o número de horas
# trabalhadas e exiba como saída o salário do profissional.

funcaoDes = int(input("Qual sua função? \n1 - Testador; \n2 - Analista de Testes; \n3 - Programador; \n4 - Analista de "
                   "Sistemas; \n5 - DBA.\nR: "))
numHoras = float(input("Quantas horas você trabalhou nesta função? "))

valorHora = 0

if funcaoDes == 1:
    valorHora = 20
elif funcaoDes == 2:
    valorHora = 35
elif funcaoDes == 3:
    valorHora = 45
elif funcaoDes == 4:
    valorHora = 40
elif funcaoDes == 1:
    valorHora = 50
else:
    print("Selecione uma função válida.")

valorTotal = valorHora * numHoras

print(f"Você deverá receber um total de R${valorTotal:.2f}.")