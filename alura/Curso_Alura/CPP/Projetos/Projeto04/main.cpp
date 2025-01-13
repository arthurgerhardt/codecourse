#include <iostream>
#include <string>
#include <map>

using namespace std;

const string palavra_secreta = "MELANCIA";
map<char, bool> chutou;

bool letra_existe(char chute) {
    for(char letra : palavra_secreta) {
        if (chute == letra) {
            return true;
        }
    }
    return false;
}

int main() {

    cout << "*****************************************" << endl;
    cout << "*******Bem-vindo ao jogo da forca!*******" << endl;
    cout << "*****************************************" << endl;

    bool naoacertou = true;
    int tentativas = 0;
    const int max_tentativas = 6;
    
    while(naoacertou && tentativas < max_tentativas) {
        for(char letra : palavra_secreta) {
            if(chutou[letra]) {
                cout << letra << " ";
            } else {
                cout << "_ ";
            }
        }
        cout << endl;
        char chute;
        cout << "Digite uma letra da palavra secreta: " << endl;
        cin >> chute;
        chutou[chute] = true;
        if (letra_existe(chute)) {
            // Update game state if the guess is correct
            bool acertou_todas = true;
            for(char letra : palavra_secreta) {
                if(!chutou[letra]) {
                    acertou_todas = false;
                    break;
                }
            }
            naoacertou = !acertou_todas;
            cout << "Você acertou uma letra da palavra secreta!" << endl;
        } else {
            tentativas++;
        }
    }   

    if (tentativas == max_tentativas) {
        cout << "Você perdeu! O número máximo de tentativas foi atingido." << endl;
    } else {
        cout << "Parabéns! Você adivinhou a palavra secreta." << endl;
    }
}