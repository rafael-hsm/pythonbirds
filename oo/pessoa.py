class Pessoa:
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    """
    self.nome determina o nome o objeto self, é um atributo. 
    Quando não temos o self, o nome é interpretado como parâmetro.
    """
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    dexter = Pessoa(nome="Dexter")
    rafael = Pessoa(dexter, nome="Rafael")
    print(Pessoa.cumprimentar(dexter))
    print(id(dexter))
    print(dexter.cumprimentar())
    print(dexter.nome)
    for filho in rafael.filhos:
        print(filho.nome)
    rafael.sobrenome = 'Meireles'
    del rafael.filhos
    print(rafael.__dict__)
    print(dexter.__dict__)
