def calcular_imc(peso, altura):
    if altura <= 0:
        return "Altura deve ser maior que zero."
    imc = peso / (altura ** 2)
    return imc

# Exemplo de uso
peso = 70  # em quilogramas
altura = 1.75  # em metros
imc = calcular_imc(peso, altura)
print(f"O IMC é: {imc:.2f}")
