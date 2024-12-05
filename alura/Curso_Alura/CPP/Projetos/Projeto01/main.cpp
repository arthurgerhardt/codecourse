#include<iostream>
using namespace std;

int main (){
    cout << "***************************************" << endl;
    cout << "* Boas vindas ao Jogo da Adivinhação! *" << endl;
    cout << "***************************************" << endl;

    const int numero_secreto = 42;
    int chute = 0;
    bool nao_acertou = true;
    
    while(nao_acertou){
        cout << "Digite o seu chute: ";
        cin >> chute;
        cout << "O valor do seu chute é: " << chute << endl;
        bool acertou = chute == numero_secreto;
        bool maior = chute > numero_secreto;
        if(acertou){
            cout << "Parabéns! Você acertou o número secreto!" << endl;
            nao_acertou = false;
        } else if(maior){
            cout << "Seu chute foi maior que o número secreto." << endl;
        } else {
            cout << "Seu chute foi menor que o número secreto." << endl;
        }
    }
    cout << "Fim de jogo!" << endl;
}
