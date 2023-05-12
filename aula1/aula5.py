import os
#limpar tela do terminal
os.system("cls")
print("-----------------------------------")
def lerDados():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    print("Oseu nome é {0}, e sua idade é {1} anos ".format(nome,idade))
    print("-----------------------------------")
    resposta = input("Deseja continuar S/N")
    if (resposta == "S"):
        lerDados()
    

                                           
                                                       