from typing import Any

def meu_decorador(func):
    def wrapper():
        print('Antes da função')
        func()
        print('Depois da função')
    return wrapper

@meu_decorador
def minha_funcao():
    print('Minha função foi chamada.')

minha_funcao()  

class meuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
    def __call__(self) -> Any:
        print("Antes da função ser chamada (decorador de classes).")
        self.func()
        print("Depois da função ser chamada (decorador de classes).")

@meuDecoradorDeClasse
def minha_funcao_decorada():
    print("Minha função decorada foi chamada.")

minha_funcao_decorada()
    
        