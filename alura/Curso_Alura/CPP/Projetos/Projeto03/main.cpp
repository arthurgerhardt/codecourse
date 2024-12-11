#include <iostream>
#include <string>

// Classe base Personagem
class Personagem {
protected:
    std::string nome;
    int vida;
    int nivel;

public:
    Personagem(const std::string& nome, int vida, int nivel)
        : nome(nome), vida(vida), nivel(nivel) {}

    const std::string& get_nome() const {
        return nome;
    }

    int get_vida() const {
        return vida;
    }

    int get_nivel() const {
        return nivel;
    }

    virtual std::string exibir_detalhes() const {
        return "Nome: " + get_nome() + "\nVida: " + std::to_string(get_vida()) + "\nNível: " + std::to_string(get_nivel());
    }

    void receber_ataque(int dano) {
        vida -= dano;
        if (vida < 0) {
            vida = 0;
        }
    }

    void atacar(Personagem &alvo) {
        int dano = nivel * 4;
        alvo.receber_ataque(dano);
        std::cout << get_nome() << " atacou " << alvo.get_nome() << " e causou " << dano << " de dano.\n";
    }
};

// Classe Heroi derivada de Personagem
class Heroi : public Personagem {
    std::string habilidade;

public:
    Heroi(const std::string& nome, int vida, int nivel, const std::string& habilidade)
        : Personagem(nome, vida, nivel), habilidade(habilidade) {}

    const std::string& get_habilidade() const {
        return habilidade;
    }

    std::string exibir_detalhes() const override {
        return Personagem::exibir_detalhes() + "\nHabilidade: " + get_habilidade();
    }

    void ataque_especial(Personagem &alvo) {
        int dano = nivel * 15;
        alvo.receber_ataque(dano);
        std::cout << get_nome() << " usou a habilidade " << get_habilidade() << " e causou " << dano << " de dano.\n";
    }

    void ataque_one_hit_obliterator(Personagem &alvo) {
        alvo.receber_ataque(alvo.get_vida());
        std::cout << get_nome() << " usou o One-Hit Obliterator e derrotou " << alvo.get_nome() << " em um único golpe!\n";
    }
};

// Classe Inimigo derivada de Personagem
class Inimigo : public Personagem {
    std::string tipo;

public:
    Inimigo(const std::string& nome, int vida, int nivel, const std::string& tipo)
        : Personagem(nome, vida, nivel), tipo(tipo) {}

    const std::string& get_tipo() const {
        return tipo;
    }

    std::string exibir_detalhes() const override {
        return Personagem::exibir_detalhes() + "\nTipo: " + get_tipo();
    }
};

// Classe do jogo
class Jogo {
    Heroi heroi;
    Inimigo inimigo;

public:
    Jogo()
        : heroi("Link", 1800, 10, "Espada Mestre"), inimigo("Calamity Ganon", 1500, 7, "Chefe Final") {}

    void iniciar_batalha() {
        std::cout << "Iniciando batalha!\n";
        while (heroi.get_vida() > 0 && inimigo.get_vida() > 0) {
            std::cout << "Detalhes dos personagens:\n";
            std::cout << heroi.exibir_detalhes() << "\n";
            std::cout << inimigo.exibir_detalhes() << "\n";

            std::string escolha;
            std::cout << "Escolha (1- Ataque normal, 2- Ataque especial, 3- One-Hit Obliterator): ";
            std::cin >> escolha;

            if (escolha == "1") {
                heroi.atacar(inimigo);
                if (inimigo.get_vida() > 0) {
                    inimigo.atacar(heroi);
                }
            } else if (escolha == "2") {
                heroi.ataque_especial(inimigo);
                if (inimigo.get_vida() > 0) {
                    inimigo.atacar(heroi);
                }
            } else if (escolha == "3") {
                heroi.ataque_one_hit_obliterator(inimigo);
                if (inimigo.get_vida() > 0) {
                    inimigo.atacar(heroi);
                }
            }
        }

        if (heroi.get_vida() > 0) {
            std::cout << "Parabéns! Link venceu a batalha!\n";
        } else {
            std::cout << "Game Over! Calamity Ganon venceu a batalha!\n";
        }
    }
};

int main() {
    std::cout << "********************************************************************************\n";
    std::cout << "******************* The Legend of Zelda: Breath of the Wild ********************\n";
    std::cout << "************************* Bem-vindo ao jogo! Começar! **************************\n";
    std::cout << "********************************************************************************\n\n";

    std::cout << "Esta é a batalha final entre Link e Calamity Ganon\n";
    std::cout << "Calamity Ganon diz: Eu vou acabar com você, com a minha força e poder!\n";
    std::cout << "Link diz: Eu vou te derrotar, com a minha coragem e determinação!\n";
    std::cout << "Calamity Ganon diz: Então, vamos ver quem é o mais forte!\n";
    std::cout << "Link diz: Vamos ver, Calamity Ganon!\n\n";

    Jogo jogo;
    jogo.iniciar_batalha();

    return 0;
}
