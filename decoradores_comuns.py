'''
O que são, principais métodos e como usá-los:
@classmethod
@staticmethod
'''
class MinhaClasse:
    valor = 10 # Atributo de classe
    def __init__(self, nome) -> None:
        self.nome = nome # Atributo da instância, atributos da classe são usados fora do construtor
    
    # Esse método requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome} e usado para {self.valor}"    
    
    # Difernte do self que recebe a instância, o cls recebe a classe
    @classmethod
    def metodo_classe(cls):
        return f"Método de clase chamado para valor={cls.valor}"
    
    # O método estático é diferente do método da instância e do método da classe pq ele não recebe nenhum argumento
    # Logo ele não recebe atributos nem da classe, nem da instância, mas pode executar funções específicas.
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"

obj = MinhaClasse("Classe de Exemplo")
print(obj.metodo_instancia())

'''
Por "valor" ser um atributo da classe "MinhaClasse" é possível chamar ele através da classe
Pois não é necessário uma instância para acessar um atributo da classe
'''
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

# Método da classe é muito utilizado para criar instâncias a partir de configurações globais

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod    
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
configuracao1 = "Fiat, Marea, 2002"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:
    
    @staticmethod
    def somar(a, b):
        return f"{a} + {b} = {a + b}" 
    
print(Matematica.somar(15, 10))