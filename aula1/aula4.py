import os
#limpar tela do terminal
os.system("cls")
print("-----------------------------------")

def novaCompra():
    produto = input("Nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    parcela = int(input("Digite o numero de parcelas: "))
    print("O {0}, custa {1:.2} e o numero de parcelas é de{2}".format(produto,valor,parcela))

    parcelas = valor / parcela
    print("O valor das parcelas é de {2:.2f} ".format(parcelas))
    print("-----------------------------------")

    resposta = input("Deseja continuar S/N ")
    if (resposta == "S"):
        novaCompra()
    
print("Digite a nova compra")
novaCompra()

