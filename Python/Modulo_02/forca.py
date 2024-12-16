palavra_secreta = "MELANCIA"

def letra_existe(chute):
    return chute in palavra_secreta

def atualiza_palavra(palavra_atual, chute):
    nova_palavra = ""
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == chute:
            nova_palavra += chute
        else:
            nova_palavra += palavra_atual[i]
    return nova_palavra

def main():
    palavra_atual = "_" * len(palavra_secreta)
    max_tentativas = 5
    tentativas = 0

    print("Bem-vindo ao jogo da forca!")

    while palavra_atual != palavra_secreta and tentativas < max_tentativas:
        chute = input("Digite uma letra da palavra secreta: ").upper()

        if letra_existe(chute):
            palavra_atual = atualiza_palavra(palavra_atual, chute)
            print("Você acertou uma letra da palavra secreta!")
            print("Palavra atual:", palavra_atual)
        else:
            tentativas += 1
            print("Você errou! Tentativas restantes:", max_tentativas - tentativas)

    if tentativas == max_tentativas:
        print("Você perdeu! O número máximo de tentativas foi atingido.")
    else:
        print("Parabéns! Você adivinhou a palavra secreta.")

if __name__ == "__main__":
    main()
