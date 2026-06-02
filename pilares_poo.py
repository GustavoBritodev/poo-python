# Exemplo de herança

print("Exemplo de Herança: ")

class Animal:
    def __init__(self, nome, genero) -> None:
        self.nome = nome
        self.genero = genero
        
    def andar(self):
        print(f"\nO animal {self.nome} andou pela casa")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau, miau"
    
mironga = Gato("Mironga", "Macho")
print(f"\nO nome do meu gato é {mironga.nome}")

naia = Cachorro("Naiá", "Fêmea")
print(f"\nO nome da minha cachorra é {naia.nome}")

flash = Cachorro("Flash", "Macho")
print(f"\nO nome do meu cachorro é {flash.nome}")

mafalda = Gato("Mafalda", "Fêmea")
print(f"\nO nome da minha gata é {mafalda.nome}")

madonna = Gato("Madonna", "Fêmea")
print(f"\nO nome da minha gata é {madonna.nome}\n")

animais = [mironga, naia, flash, madonna, mafalda]

for animal in animais:
    if(animal.genero == "Fêmea"):
        print(f"A {animal.nome} faz {animal.emitir_som()}")
    else:
        print(f"O {animal.nome} faz {animal.emitir_som()}")
        
print("\nExemplo de Encapsulamento: ")

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Os dois underlines antes do atribudo tornam ele um atributo privado
        # Ao criar um objeto de conta bancária apenas os métodos definidos dentro da classe conseguem acessar o atributo de saldo por ele ser privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente para tentativa de saque")
    
    def consultar_saldo(self):
        return self.__saldo
    
minhaConta = ContaBancaria(2500)

print(f"Meu saldo atual é {minhaConta.consultar_saldo()}")

minhaConta.depositar(500)
print(f"Meu saldo atual é {minhaConta.consultar_saldo()}")

minhaConta.sacar(250)
print(f"Meu saldo atual é {minhaConta.consultar_saldo()}")

minhaConta.sacar(3000)
print(f"Meu saldo atual é {minhaConta.consultar_saldo()}")

print("\nExemplo de Abstração: ")
# Uma classe abstrata não tem a capacidade de criar objetos diretamente dela
# Uma classe abstrata serve como um "molde" para outras classes. Isso ajuda a proteger os atributos e métodos que uma classe tem que respeitar quando ela for criada

from abc import ABC, classmethod

class Veiculo(ABC):
    
    # Decorador para que o interpretador entenda que se trata de um método abstrato
    # Isso significa que ao criar uma classe que utiliza a classe Veículo, obrigatoriamente ela vai ter que implementar esse método
    @classmethod
    def ligar(self):
        pass
    
    @classmethod
    def desligar(self):
        pass
    
class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    
    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"

carro = Carro()
print(carro.ligar())
print(carro.desligar())

class Moto(Veiculo):
    def __init__(self) -> None:
        pass
    
    def ligar(self):
        return "Moto ligada usando o botão"
    
    def desligar(self):
        return "Moto desligada usando o botão"
    
moto = Moto()
print(moto.ligar())
print(moto.desligar())