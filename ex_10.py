# 10) Um banco concede um crédito especial aos seus clientes, variável com o saldo médio no último ano. Faça um
# algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a seguinte tabela.
#                                         | Saldo Médio    |  Percentual                 |
#                                         | 0 a 500        | Nenhum Crédito              |
#                                         | De 501 a 1000  | 20% do valor do saldo médio |
#                                         | De 1001 a 1600 | 30% do valor do saldo médio |
#                                         | Acima de 1601  | 40% do valor do saldo médio |
# Mostre uma mensagem informando o saldo médio e o valor do crédito.

saldoMedio = float(input("Insira seu saldo médio: "))

percentStr = "0%"
if saldoMedio <= 500:
    percent = 0
elif 501 <= saldoMedio <= 1000:
    percent = 0.2
    percentStr = "20%"
elif 1001 <= saldoMedio <= 1600:
    percent = 0.3
    percentStr = "30%"
else:
    percent = 0.4
    percentStr = "40%"

calculo = saldoMedio * percent

print(f"Você terá {percentStr} de cŕedito sobre seu saldo mensal. Significa {calculo:.2f} do saldo médio como crédito!")
