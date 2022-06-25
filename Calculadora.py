# Projeto 16
# Função
def calculadora(num1, num2, operacao):
    '''
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    '''
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
    else:
        return 0

# Teste
print("Soma:",calculadora(6, 3, 1),
"\nSubtração:", calculadora(6, 3, 2),
"\nMultiplicação:", calculadora(6, 3, 3),
"\nDivisão:", calculadora(6, 3, 4),
"\nOperação inexistente:", calculadora(6, 3, 7))
