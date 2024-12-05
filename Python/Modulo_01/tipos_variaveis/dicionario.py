# Criando um dicionário de exemplo

pessoa = {"nome": "Arthur", "sobrenome": "Gerhardt", "idade": 38, "cidade": "Rio de Janeiro"}

# Exibindo o dicionário
print ("Meu dicionário de exemplos: ", pessoa)

# Adicionando um novo par chave-valor
print("nome: ", pessoa["nome"])
print("sobrenome", pessoa["sobrenome"])
print("idade: ", pessoa["idade"])
print("cidade: ", pessoa["cidade"])
pessoa["Estado_civil"] = "Casado"
print("Estado civíl: ", pessoa["Estado_civil"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplos: ", pessoa)

# Métodos keys(), values(), items()
chaves = list(pessoa.keys())
print("Chave do dicionário: ", chaves)
print("Primeira chave do dicionário: ", chaves[0])
print("Meu dicionário de exemplos: ", pessoa.keys())

# Métodos values()
valores = list(pessoa.values())
print("Valores do dicionário: ", valores)
print("Primeiro valor do dicionário: ", valores[0])

# Método items
itens = list(pessoa.items())
print("Pares do dicionário: ", itens)
print("Primeir chave-valor dodicionário: %s = %s" % (itens[0][0], itens[0][1]))