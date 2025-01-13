print("***************************************************")
print("********Bem vindo ao jogo de adivinhação!**********")
print("***************************************************")
# Declaração de variáveis
numero_secreto = 42
naoacertou = True
while(naoacertou):
    # Entrada de dados
    numero = int(input("Digite o seu número: "))
    # Processamento
    acertou = numero == numero_secreto
    if(acertou):
        print("Você acertou!")
        naoacertou = False
    else:
        print("Você errou!")
        maior = numero > numero_secreto
        if(maior):
            print("O número é maior!")
        else:
            print("O número é menor!")
print("Fim do jogo!")