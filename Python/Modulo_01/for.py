# Loop for()

print("\n For utilizando lista.")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)
    # print("\n")

print("\n For utilizando tupla.")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)
   # print("\n")

pessoa = {"nome": "João", "idade": 30, "cidade": "Rio de Janeiro"}
print("\n For utilizando dicionário - chaves")
for chave in pessoa.keys():
    print(chave)
   # print("\n")

print("\n For utilizando dicionário - valores")
for valor in pessoa.values():
    print(valor)
   # print("\n")


print("\n For utilizando dicionário - chaves e valores")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range(): intervalo numérico
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n For utilizando range()")
for numero in range(0, 10):
    print("Número:", numero)
   # print("\n")

print("\n For utilizando range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
        print(lista)
    else:
        lista[indice] = 0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c", "d", "e", "f"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
     print("Indice 1")