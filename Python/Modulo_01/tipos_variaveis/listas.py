# Declaracao de listas

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exibindo a lista
print("Minha lista de exemplos:", minha_lista)

# Exibindo os elementos
# minha_lista[0] = "python"
# print("Minha lista de exemplos:", minha_lista)
print("Primeiro elemento da lista:", minha_lista[0])
print("Quinto elemento da lista:", minha_lista[5])
print("Intervalo da lista de 1 a 7:", minha_lista[1:7])
print("Intervalo da lista de 1 a 5:", minha_lista[:6])
print("Intervalo da lista de 3 a 7:", minha_lista[2:])

# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append (6):", minha_lista)

# Método index(): Retorna o índice do elemento informado
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert(): Insere um elemento em uma posição informada
minha_lista.insert(2, 10)
print("Após insert (2,10):", minha_lista)

# Método Pop(): Remove o último elemento da lista
minha_lista.pop()
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove(): Remove o elemento informado
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Método sort(): Ordena a lista
minha_lista.sort()
print("Após sort():", minha_lista)