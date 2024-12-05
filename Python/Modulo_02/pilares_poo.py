"""# Exemplo de heranca
print("\n Exemplo de heranca")
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    def andar(self):
        print(f"O animal {self.__nome} andou.")
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

dog = Cachorro(nome="Rex")
cat = Gato(nome="Garfield")

print("\n Exemplo de polimorfismo")
animals = [dog, cat]
for animal in animals:
    print(animal.emitir_som())
    print(f"{animal.nome} faz: {animal.emitir_som()}") 

print("\n Exemplo de encapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Atributo privado
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária é: {conta.consultar_saldo()}")
conta.depositar(500)
print(f"Saldo da conta bancária é: {conta.consultar_saldo()}")
conta.sacar(200)
print(f"Saldo da conta bancária é: {conta.consultar_saldo()}") """

print("\n Exemplo de abstracao: ")
from abc import ABC, abstractmethod
class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
class Carro(Veiculo):
    def __init__(self) -> None:
        super().__init__()
    def ligar(self):
        return "Carro ligado, usando a chave."
    def desligar(self):
        return "Carro desligado, usando a chave."
        
carroAmarelo = Carro()
print(carroAmarelo.ligar())
print(carroAmarelo.desligar())