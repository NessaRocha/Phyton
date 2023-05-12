import os
#limpar tela doterminal
os.system("cls")
print("-----------------------------------")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade")
#comentario
print("Nome digitado: ", nome)
print("Idade digitada: ", idade)
idade = int(idade)

dias = idade * 365
print("Vc ja viveu: ", dias)

print(type(nome))
print(type(idade))

print("-----------------------------------")