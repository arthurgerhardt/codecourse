import re

print("Aula 01 - Expressões Regulares")

texto = "Bem-vindo ao mundo do Python!"
resultado = re.search(r"Python", texto)

if resultado:
    print("Padrão encontrado:", resultado.group())
else:
    print("Padrão não encontrado.")
# O código acima utiliza a biblioteca re para buscar o padrão "Python" na string "texto".
# Se o padrão for encontrado, ele imprime "Padrão encontrado: Python", caso contrário, imprime "Padrão não encontrado."