print("Exemplo de captura de exceções")
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 10 / numero  # 10 / numero
    except ValueError:
        print(f"Você digitou um valor inválido. Tente novamente. {e}")
        raise ValueError("Tipo de variáveis incompatíveis.")
    except Exception as e:
        print(f"Erro: {e}")
    else:
        print(f"O resultado é {resultado}:")
    finally:
        print("Operação concluída. Aplicação encerrada.")
