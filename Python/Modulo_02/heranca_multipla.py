# Comecando a aprender sobre classes, polimorfismo e preparando para fazer um jogo, todo em Python. Segue nas próximas aulas!

# Herança Múltipla
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass
    
class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
        
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som()
        return "Morcegos emitem sons ultrassônicos."
morcego = Morcego(nome="Batman")

# Acessando métodos da classe `Animal``
print("Nome do morcego: ", morcego.nome)