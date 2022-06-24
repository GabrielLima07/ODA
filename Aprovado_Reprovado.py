# Projeto 13
# Variáveis
aluno = input("Insira o nome do aluno: ")
n1 = float(input("Insira a nota 1 do aluno: "))
n2 = float(input("Insira a nota 2 do aluno: "))
media = (n1 + n2) / 2
faltas = int(input(f"Quantas faltas teve {aluno}? "))
msg_aprovado = f"{aluno} está aprovado!"
msg_reprovado = f"{aluno} está reprovado!"

# Teste condicional
if (media < 7) or (faltas > 3):
    print(msg_reprovado)
else:
    print(msg_aprovado)
