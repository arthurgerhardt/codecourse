# Condicao verdadeira
True

# Condicao falsa
False

#Condicionais
#se condicao
#else = senão
if True:
    print("Condicao verdadeira. Bloco IF vai ser executado.")
else:
    print("Condicao falsa. Bloco ELSE não vai ser executado.")

# Operadores lógicos: and e or.
# AND
if True and True:
    print("Ambas as condicoes verdadeiras. Bloco IF vai ser executado.")

if True and False:
    print("Condicao 1 verdadeira e condicao 2 falsa. Bloco IF não vai ser executado.")
    
if False and False:
    print("Condicao 1 falsa e condicao 2 falsa. Bloco IF não vai ser executado.")

# OR
if True or True:
    print("Ambas as condicoes verdadeiras. Bloco IF vai ser executado.")

if True or False:
    print("Condicao 1 verdadeira ou condicao 2 falsa. Bloco IF vai ser executado.")

if False or False:
    print("Condicao 1 falsa e condicao 2 falsa. Bloco IF não vai ser executado.")