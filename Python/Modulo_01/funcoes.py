#  Exemplo

def saudacao(nome):
    print(f"Olá, {nome}!")

print("Chamando a função saudacao:")
saudacao("Andre")
saudacao("Maria")

# Funcao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando a função quadrado:")
resultado_quadrado = quadrado(4)
print("Resultado da função quadrado: ", resultado_quadrado)

# Função com múltiplos parâmetros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma:")
numero1 = 20
numero2 = 50
soma_result = soma(numero1, numero2)
print("Resultado da função soma do numero %s e numero %s é %s" % (numero1, numero2, soma_result))