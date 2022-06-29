from enum import Enum


class eleicao(Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0

def finalizar():
    done = input("Você deseja finalizar a votação?(S/N): ")
    done = done.upper()

    if done == "S":
        return False
    elif done == "N":
        return True
    else:
        print("Responda com S para sim ou N para não.")
        finalizar()
        return True


if __name__ == "__main__":
    # Contadores
    condicao = True
    votos_X = 0
    votos_Y = 0
    votos_Z = 0
    votos_nulos = 0

    # Manter o código funcionando enquanto a votação não é encerrada
    while condicao == True:
        voto = input("Insira o número do candidato que deseja votar: ")
        
        try:
            voto = int(voto)
        except:
            print("Você deve inserir o número do candidato.")
            continue

        # Contabilizando votos
        if voto == eleicao.candidato_X.value:
            votos_X += 1
        elif voto == eleicao.candidato_Y.value:
            votos_Y += 1
        elif voto == eleicao.candidato_Z.value:
            votos_Z += 1
        elif voto == eleicao.branco.value:
            votos_nulos += 1
        else:
            votos_nulos += 1
        
        condicao = finalizar()
        if condicao == False: # Vai parar o loop para ele não rodar uma vez a mais do que deveria
            break

    # Resultado eleições:
    lista_votos = [votos_X, votos_Y, votos_Z, votos_nulos]
    vencedor = max(lista_votos)

    # Tratando o caso da maior quantidade de votos serem nulos
    if votos_nulos == vencedor:
        lista_votos.remove(votos_nulos)
        vencedor = max(lista_votos)

    # Lista auxiliar para caso ocorra um candidato com mais votos e 2 com a mesma quantidade de votos o sistema não interpretar como empate
    lista_aux = lista_votos[:-1]
    lista_aux.remove(max(lista_aux))

    if ((votos_X == votos_Y) or (votos_X == votos_Z) or (votos_Y == votos_Z)) and (max(lista_votos) in lista_aux): # Tratando o caso de empate
        vencedor = "Não houve vencedor, todos os candidatos tiveram a mesma quantidade de votos."
    elif votos_X == vencedor:
        vencedor = eleicao.candidato_X.name
    elif votos_Y == vencedor:
        vencedor = eleicao.candidato_Y.name
    elif votos_Z == vencedor:
        vencedor = eleicao.candidato_Z.name
    
    # Exibição do resultado
    print(f"\n\nVencedor: {vencedor}")
    print(f"\nNúmeros de votos:",
    f"\n{eleicao.candidato_X.name}: {votos_X}",
    f"\n{eleicao.candidato_Y.name}: {votos_Y}",
    f"\n{eleicao.candidato_Z.name}: {votos_Z}",
    f"\n{eleicao.branco.name}: {votos_nulos}")
