# Projeto 25
class M_String:

    def __init__(self, string):
        self.string = string
        self.dict = {
            "a": "A","b": "B","c": "C","d": "D","e": "E","f": "F","g": "G","h": "H","i": "I","j": "J","k": "K","l": "L","m": "M",
            "n": "N","o": "O","p": "P","q": "Q","r": "R","s": "S","t": "T","u": "U","v": "V","w": "W","x": "X","y": "Y","z": "Z"
            }

    def maiusculo(self):
        x = []

        for i in self.string:
            if i in self.dict.keys():
                x.append(self.dict[i])
            else:
                x.append(i)

        x = ''.join(x)
        return x

    def primeiroMaisculo(self):
        x = list(self.string)  # Transfomando em lista para que aceite item assignment
        
        if self.string[0] in self.dict:
            x[0] = self.dict[self.string[0]]

        x = ''.join(x)
        return x

    def posicao(self, letra:str):
        p = ''

        for i, item in enumerate(self.string):
            if letra == item:
                p = str(i)
                break

        try:
            p = int(p)
        except:
            return f'"{letra}" não está contida em "{self.string}"'
        return p
    

if __name__ == "__main__":

    v = M_String("tudo em todo lugar ao mesmo tempo")
    print("-Testes funções-\n")
    print(v.maiusculo())
    print(v.primeiroMaisculo())
    print(v.posicao('l'))
