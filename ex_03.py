# 3) Desenvolver um programa que verifique se um determinado ano é bissexto. Considere que, para um ano ser bissexto
# ele deve ser divisível por 4, e ao mesmo tempo, deve ser divisível por 400 ou não ser divisível por 100.

ano = int(input("Quer verificar se um ano é ou não é bissexto? Informe o ano desejado: "))

if (ano % 4 == 0) and ( (ano % 400 == 0) or (ano % 100 != 0) ):
    print(f"{ano:.0f} é um ano bissexto!")
else:
    print(f"{ano:.0f} não é um ano bissexto!")

print("Fim!")