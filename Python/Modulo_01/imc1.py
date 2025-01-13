def calcular_imc(peso, altura):
    """
    Calcula o IMC (Índice de Massa Corporal).
    
    Args:
    peso (float): Peso da pessoa em quilogramas.
    altura (float): Altura da pessoa em metros.
    
    Returns:
    float: Valor do IMC.
    """
    imc = peso / (altura ** 2)
    return imc

def calcular_agua(peso):
    """
    Calcula a quantidade de água (em litros) que a pessoa deve ingerir por dia.
    
    Args:
    peso (float): Peso da pessoa em quilogramas.
    
    Returns:
    float: Quantidade de água em litros.
    """
    # Recomendação comum: 35 ml de água por kg de peso corporal.
    agua = peso * 0.035
    return agua

def main():
    # Solicita o peso e altura da pessoa
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    
    # Calcula o IMC
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    
    # Calcula a quantidade de água recomendada
    agua = calcular_agua(peso)
    print(f"Você deve ingerir aproximadamente {agua:.2f} litros de água por dia.")

if __name__ == "__main__":
    main()
