print("Exemplo de importacao de um módulo padrão: ")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")
print("Exemplo de criação e utilizacão de um módulo personalizado: ")
import meu_modulo

mensagem = meu_modulo.saudacao("Arthur")
resultado_dobro = meu_modulo.dobro(5)
print(mensagem)
print(f"O dobro de 5 é: {resultado_dobro}")