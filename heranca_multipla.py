class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
        
    def emitir_som(self):
        pass
    
class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando!"

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando!"
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        # O super é uma função padrão que chama a implementação da classe mãe, é válido para herança de implementações de funções que retornam ou processavam algo
        # Para esse caso o super é desnecessário
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego("Batman")

# Acessando os métodos da classe base "Animal"
print(f"O nome do morcego é: {morcego.nome}")
print(f"Som do morcego: {morcego.emitir_som()}")

# Acessando os métodos das classes "Mamífero" e "Ave"
print(f"Morcego voando: {morcego.voar()}")
print(f"Morcego amamentando: {morcego.amamentar()}")