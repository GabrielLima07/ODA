# Projeto 17
import sys


def calculadora():
    print('''
    1: Soma
    2: Subtração
    3: Multiplicação
    4: Divisão
    0: Sair
    ''')

    operacao = int(input("Escolha a operação: "))
    if operacao == 0:
        print("Programa encerrado.")
        sys.exit()
    elif (operacao == 1) or (operacao == 2) or (operacao == 3) or (operacao == 4):
        num1 = float(input("Insira um número: "))
        num2 = float(input("Insira mais um número: "))
        if operacao == 1:
            print("Resultado:", num1 + num2)
        elif operacao == 2:
            print("Resultado:",num1 - num2)
        elif operacao == 3:
            print("Resultado:",num1 * num2)
        elif operacao == 4:
            print("Resultado:",num1 / num2)      
    else:
        print("Essa opção não existe")
        
    calculadora()
        

calculadora()