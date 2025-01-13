print("***************************************")
print("* Boas vindas ao Jogo da Adivinhação! *")
print("***************************************")

print("Qual o nível de dificuldade?")
print("Fácil(F), Médio(M), Difícil(D)")
dificuldade = input("Escolha o nível: ")

numero_de_tentativas = 0

if dificuldade == "F":
    numero_de_tentativas = 15
elif dificuldade == "M":
    numero_de_tentativas = 10
else:    
    numero_de_tentativas = 5

numero_secreto = 42
chute = 0
nao_acertou = True
tentativas = 0
pontos = 1000.0

for rodada in range(1, numero_de_tentativas + 1):
    print(f"Tentativa {tentativas}")
    chute = int(input("Digite o seu chute: "))
    pontos_perdidos = abs(numero_secreto - chute) /2
    pontos = pontos - pontos_perdidos
    print(f"O valor do seu chute é: {chute}")
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    
    if acertou:
        print("Parabéns! Você acertou o número secreto!")
        nao_acertou = False
    elif maior:
        print("Seu chute foi maior que o número secreto.")
    else:
        print("Seu chute foi menor que o número secreto.")
        
print("Fim de jogo!")
if nao_acertou:
    print(f"Você perdeu. Tente novamente!")
else:
        print(f"Você acertou o número secreto em {tentativas} tentativas")
        print(f"Sua pontuação foi de {pontos:.2f} pontos")
