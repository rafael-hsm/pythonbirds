class Pessoa:
    def __init__(self, nome = None, idade=31):
        self.idade = idade
        self.nome = nome
    """
    self.nome determina o nome o objeto self, é um atributo. 
    Quando não temos o self, o nome é interpretado como parâmetro.
    """
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa("Ana")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Rafael'
    print(p.nome)
    print(p.idade)

