
historico = []
saldo = 0

while True:

    valor = int(input("Insira um valor: "))

    saldo += valor

    registro = "Você depositou: " + str(saldo)

    historico.append(registro) #APPEND = ANEXAR

    registro2 = "Depositaste: " + str(saldo)

    historico.append(registro2) #APPEND = ANEXAR

    break

# print(historico)

for transacoes in historico:
    print(">> " + registro)