import os
#limpar tela do terminal
os.system("cls")
print("-----------------------------------")
nome = input("Digite seu nome: ")
salario = input("Digite seu salario: ")
aumento = input("Digite a percentagem do aumento: ")

salario = float(salario)
aumento = float(aumento)

aumento = salario * aumento / 100
print("O aumento é de: ", aumento)
salario = salario + aumento
print("O salario sera de: ", salario)
print("-----------------------------------")
print("Olá {0}, seu aumento é de {1:.2f}, e seu novo salário é de {2:.2f} ".format(nome,aumento,salario))

