class Pessoa:
    # Quando o def está fora de uma classe é uma função e quando está dentro de uma classe é um método
    # O self é uma referência a própria classe para que eu possa utilizar os métodos e atributos dessa classe
    # Como comportamento padrão de um Construtor a seta e o None define que esse método não tem retorno
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Oi, meu nome é {self.nome} e tenho {self.idade} anos"
    
# Objetos são uma instância de uma classe (criados a partir de uma classe respeitando os atributos e os métodos)
# Objetos podem representar entidades do mundo real
pessoa1 = Pessoa("Gustavo", 20)

print(f"Eu sou o {pessoa1.nome} e tenho {pessoa1.idade} anos")

pessoa2 = Pessoa("Gabriel", 17)

print(f"\nEu sou o {pessoa1.nome} e sou irmão do {pessoa2.nome}")

print(pessoa1.saudacao())

print(pessoa2.saudacao())