
valorCompra = 1

historicoCompras = []

while valorCompra > 0:
    
    valorCompra = float(input("Digite o valor da compra: "))
    
    if(valorCompra == 0):
        break

    idadeCliente = int(input("Digite a idade do cliente: "))

    quantidadeCompras = int(input("Digite a quantidade de itens: "))

    cupomDesconto = input("Digite o cupom de desconto: ")


    if(valorCompra < 0 or idadeCliente <= 0 or quantidadeCompras <= 0):
        print("Valor da compra, idade do cliente e quantidade de itens devem ser maiores que zero.")
        print("Digite novamente os valores.")
        valorCompra, idadeCliente, quantidadeCompras = 1, 0, 0
        continue
    
    valorDesconto = 0
        
    if idadeCliente >= 65:
        valorDesconto = valorCompra * 0.20

    if(valorCompra - valorDesconto) > 100:
        valorDesconto += (valorCompra - valorDesconto) * 0.10

    if(quantidadeCompras > 3):
        valorDesconto += (valorCompra - valorDesconto) * 0.05

    if(cupomDesconto == "FIDELIDADE10"):
        valorDesconto += (valorCompra - valorDesconto) * 0.10

    valorFinal = valorCompra - valorDesconto

    historicoCompras.append({
        "valorCompra": valorCompra,
        "idadeCliente": idadeCliente,
        "quantidadeCompras": quantidadeCompras,
        "cupomDesconto": cupomDesconto,
        "valorDesconto": valorDesconto,
        "valorFinal": valorFinal
    })

    print("Valor final esperado: R$ ", f"{valorFinal:.2f}")


print("------------------------------\n")

print("Histórico de compras:")

totalDescontosConcedidos = 0
totalBruto = 0
totalFinal = 0

for compra in historicoCompras:
    print("Valor da compra: R$ ", f"{compra['valorCompra']:.2f}")
    print("Idade do cliente: ", compra["idadeCliente"])
    print("Quantidade de itens: ", compra["quantidadeCompras"])
    print("Cupom de desconto: ", compra["cupomDesconto"])
    print("Valor do desconto: R$ ", f"{compra['valorDesconto']:.2f}")
    print("Valor final: R$ ", f"{compra['valorFinal']:.2f}")
    print("-----------------------------")

    totalDescontosConcedidos += compra["valorDesconto"]
    totalBruto += compra["valorCompra"]
    totalFinal += compra["valorFinal"]

with open("resumo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Resumo das compras:\n")
    arquivo.write("------------------------------\n")
    arquivo.write("Total de compras realizadas: " + str(len(historicoCompras)) + "\n")
    arquivo.write("Total de descontos concedidos: R$ " + f"{totalDescontosConcedidos:.2f}" + "\n")
    arquivo.write("Total bruto: R$ " + f"{totalBruto:.2f}" + "\n")
    arquivo.write("Total final: R$ " + f"{totalFinal:.2f}" + "\n") 

print("Total de compras realizadas: ", len(historicoCompras))
print("Total de descontos concedidos: R$ ", f"{totalDescontosConcedidos:.2f}")
print("Total bruto: R$ ", f"{totalBruto:.2f}")
print("Total final: R$ ", f"{totalFinal:.2f}")
