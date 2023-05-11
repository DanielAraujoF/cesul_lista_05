# 7) Uma facultative classifica as notas dos alunos conforme a faixa de média que tenha atingido
# de acordo com a seguinte tabela:
#                                         | Média      | Classificação  |
#                                         | 9,0 a 10   | Superior       |
#                                         | 7,0 a 8,9  | Médio Superior |
#                                         | 5, 0 a 6,9 | Médio          |
#                                         | 3,0 a 4,9  | Médio Inferior |
#                                         | 0,1 a 2,9  | Inferior       |
#                                         | 0          | Sem Rendimento |
# Faça um algoritmo que lê a nota de um aluno e informa a sua classificação.

media = float(input("Insira sua média: "))

if 0 < media > 10:
    print("Nota inválida!")
elif media >= 9:
    print("A sua classificação é superior!")
elif media >= 7:
    print("A sua classificação é médio superior!")
elif media >= 5:
    print("A sua classificação é médio!")
elif media >= 3:
    print("A sua classificação é médio inferior!")
elif media >= 0.1:
    print("A sua classificação é inferior!")
else:
    print("A sua classificação é sem rendimento!")
