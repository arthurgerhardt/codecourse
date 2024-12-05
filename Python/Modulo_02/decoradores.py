def meu_decorador(func):
    def wrapper():
        print('Antes da função')
        func()
        print('Depois da função')
    return wrapper

@meu_decorador
def minha_funcao():
    print('Minha função')