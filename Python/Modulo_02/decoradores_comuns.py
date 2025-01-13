# @classmethod
# @staticmethod
class MinhaClasse:
    valor = 10 # Atributo de classe

    def __init__(self, nome):
        self.nome = nome # Atributo de instância

    # Requer uma instância para ser chamado
    def metodo_de_instancia(self):
        return f"Este é um método de instância {self.valor}"
    
    @classmethod
    def metodo_de_classe(cls):
        return f"Este é um método de classe {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Este é um método estático."

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_de_instancia()) # Este é um método de instância.
print(MinhaClasse.valor) # 10
print(MinhaClasse.metodo_de_classe()) # Este é um método de classe.
print(MinhaClasse.metodo_estatico()) # Este é um método estático.

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(" ")
        return cls(marca, modelo, int(ano))
    
configuracao1 = "Toyota Corolla 2021"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}") # Toyota
        
class Matematica: 
    @staticmethod
    def somar(a, b):
            return a + b

print(Matematica.somar(a=10, b=15)) # 25