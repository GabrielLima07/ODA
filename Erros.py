# Projeto 18
proc = True
while proc:
    try:
        nome = input("Digite seu nome completo: ")
        ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
        
        if (ano > 2021) or (ano < 1922):
            raise Exception("O ano inserido deve estar entre 1922 e 2021\n") 
        else:
            print(f"Nome: {nome}\nIdade em 2022: {2022 - ano}")
            proc = False
        
    except Exception as erro:
        print(erro, "\nAlgum dado foi preenchido incorretamente. Tente novamente:\n")
        