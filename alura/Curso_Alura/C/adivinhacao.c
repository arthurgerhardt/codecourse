#include <stdio.h>
#include <stdbool.h>

int main() {
    printf("****************************************** \n");
    printf("****Bem-vindo ao jogo de adivinhação! **** \n");
    printf("****************************************** \n");
    // Declaração de variáveis
    const int numerosecreto = 42;
    int numero;
    bool naoacertou = true;
    // O código em si
    while(naoacertou){
        printf("Qual é o seu chute? \n");
        scanf("%d", &numero);
        printf("Seu chute foi: %d \n", numero);
        int acertou = (numero == numerosecreto);
        if (acertou){
            printf("Parabéns! Você acertou! \n");
            printf("Você é um bom jogador! Jogue de novo! \n");
            naoacertou = false;
            acertou = false;
        }
        else 
        {
            int maior = numero > numerosecreto;
            if (maior)
                printf("Seu chute foi maior que o número secreto. \n");
            else
                printf("Seu número foi menor que o número secreto. \n");
            continue;
        }
        // Add logic to check if the number is correct
    }
    return 0;
}