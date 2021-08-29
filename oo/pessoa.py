class Pessoa:
    olhos = 2  # :Atributo de classe ou atributo default

    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    """
    self.nome determina o nome o objeto self, é um atributo. 
    Quando não temos o self, o nome é interpretado como parâmetro.
    """
    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe} Aperto de mão!'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    dexter = Mutante(nome="Dexter")
    rafael = Homem(dexter, nome="Rafael")
    print(Pessoa.cumprimentar(dexter))
    print(id(dexter))
    print(dexter.cumprimentar())
    print(dexter.nome)
    for filho in rafael.filhos:
        print(filho.nome)
    rafael.sobrenome = 'Meireles'
    del rafael.filhos
    dexter.olhos = 1
    del dexter.olhos
    print(rafael.__dict__)
    print(dexter.__dict__)
    print(Pessoa.olhos)
    print(dexter.olhos)
    print(rafael.olhos)
    print(id(rafael.olhos), id(dexter.olhos), id(rafael.olhos))
    print(Pessoa.metodo_estatico(), dexter.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), dexter.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(rafael, Pessoa))
    print(isinstance(rafael, Homem))
    print(dexter.olhos)
    print(dexter.cumprimentar())
    print(rafael.cumprimentar())
