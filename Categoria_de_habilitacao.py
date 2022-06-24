# Projeto 14
# Variáveis
qntd_rodas = int(input("Insira a quantidade de rodas do veículo: "))
peso = float(input("Informe o peso do veículo em KG: "))
qntd_pessoas = int(input("Quantas pessoas o veículo pode transportar? "))

# Testes condicionais
if qntd_rodas <= 3:
    categoria = "A"
elif (qntd_rodas == 4) and (qntd_pessoas <= 8) and (peso <= 3500):
    categoria = "B"
elif (qntd_rodas > 3) and (peso > 3500) and (peso <= 6000):
    categoria = "C"
elif (qntd_rodas > 3) and (qntd_pessoas > 8):
    categoria = "D"
elif (qntd_rodas > 3) and (peso > 6000):
    categoria = "E"
else:
    categoria = "...\nDe acordo com as entradas a categoria mais adequada foi inconclusiva."

# Resultado final
print(f"A categoria mais adequada para esse veículo é a: {categoria}")
