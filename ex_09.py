# 9) O departamento que controla o índice de poluição do meio ambiente mantém 3 grupos de indústrias que são altamente
# poluentes do meio ambiente. O índice de poluição aceitável varia de 0,05 até 0,25. Se o índice ficar entre 0,25 e 0,3
# as indústrias do 1º grupo são intimadas a suspenderem suas atividades, se ficar entre 0,31 e 0,4 as do 1º e 2º grupo
# são intimadas a suspenderem suas atividades e se o índice for maior que 0,41 os três grupos devem ser notificados a
# paralisarem suas atividades. Escrever um algoritmo que lê o índice de poluição medido e emite a notificação adequada
# aos diferentes grupos de empresas.

indice = float(input("Qual o índice de poluição atual?"))

if 0.25 <= indice <= 3:
    print("intimação e suspensão do 1° grupo")
elif 0.31 <= indice <= 0.4:
    print("intimação e suspensão do 1° e 2° grupo")
elif indice >= 0.41:
    print("todos os 3 devem suspender")
else:
    print("Aceitável.")