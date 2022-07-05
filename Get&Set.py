# Projeto 23
class Cartao:

    # Método construtor
    def __init__(self, nome:str, CPF:str, numero_conta:str, saldo=0): # Por padrão todos métodos e atributos são public
        self.__nome = nome                                            # Para tornar o método ou atributo private em python usa-se __ no inicio
        self.__cpf = CPF
        self.__numero_conta = numero_conta
        self._saldo = saldo                                           # Para tornar o método ou atributo protected em python usa-se _ no inicio
                                                    
                                                    
    # Métodos acessores:
    def get_saldo(self):
        return self._saldo

    def get_numero_conta(self):
        return self.__numero_conta

    def get_CPF(self):
        return self.__cpf

    def get_Nome(self):
        return self.__nome

    # Métodos modificadores:
    def set_saldo(self, tipo_de_movimentacao, valor):
        '''
        Para depositar o tipo_de_movimentacao deve ser True
        Para sacar o tipo_de_movimentacao deve ser False
        '''
        if tipo_de_movimentacao:
            self._saldo += valor
        elif not tipo_de_movimentacao and valor <= self._saldo:
            self._saldo -= valor
        else:
            return "Cheque as informações e tente novamente"

    def set_numero_conta(self, novo_numero_conta):
        self.__numero_conta = novo_numero_conta

    def set_CPF(self, novo_CPF):
        self.__cpf = novo_CPF

    def set_nome(self, novo_nome):
        self.__nome = novo_nome



if __name__ == "__main__":
    # Instaciando o objeto
    cartao_banco = Cartao("Gabriel", "000.111.222-33", "7227227220")

    # Testando seus métodos acessores
    print(cartao_banco.get_Nome())
    print(cartao_banco.get_CPF())
    print(cartao_banco.get_numero_conta())
    print(cartao_banco.get_saldo())

    #Testando seus métodos modificadores
    cartao_banco.set_nome("Vinicius")
    cartao_banco.set_CPF("999.999.999-00")
    cartao_banco.set_numero_conta("5366114400")
    cartao_banco.set_saldo(True, 500)
    cartao_banco.set_saldo(False, 150.50)

    # Verificando se os valores realmente foram modificados
    print()
    print(cartao_banco.get_Nome())
    print(cartao_banco.get_CPF())
    print(cartao_banco.get_numero_conta())
    print(cartao_banco.get_saldo())
