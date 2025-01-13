# Declaracão de variaveis
nome_completo = "Arthur Gerhardt"

nome_completo_aspas = """Arthur 
Gerhardt"""

nome_completo_quebra = "Arthur \
Gerhardt"

nome = "Arthur"
sobrenome = "Gerhardt"

#Formatacão de strings
print("Nome Completo (1a forma): ", nome_completo)
print("Nome Completo (2a forma): " + nome_completo)
print("Nome Completo (3a forma)" + "Arthur" + "Gerhardt")
print("Nome Completo (4a forma)" + "Arthur", "Gerhardt")
print("Nome Completo (5a forma):", nome_completo_aspas)
print("Nome Completo (6a forma):", nome_completo_quebra)
print("Nome Completo (7a forma): %s" % nome_completo)
print("Nome Completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome Completo (9a forma): {nome} {sobrenome}")
print("Nome Completo (10a forma): {} {}".format(nome, sobrenome))