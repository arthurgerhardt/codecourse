#include <iostream>

class Character {
public:
    std::string name;
    int hp, maxHp;

    Character(std::string name, int hp) : name(name), hp(hp), maxHp(hp) {}

    void takeDamage(int damage) {
        hp -= damage;
        if (hp < 0) hp = 0;
    }

    bool isAlive() {
        return hp > 0;
    }

    void showHpPercentage() {
        float percentage = ((float)hp / maxHp) * 100;
        std::cout << name << " está com " << percentage << "% de vida." << std::endl;
    }
};

class Game {
public:
    Character link;
    Character goblin;

    Game() : link("Link", 100), goblin("Goblin", 150) {}

    void start() {
        std::cout << "Bem-vindo ao jogo de Batalha Espiritual!" << std::endl;
        link.showHpPercentage();
        goblin.showHpPercentage();
        std::cout << "O jogo começou!" << std::endl;

        while (link.isAlive() && goblin.isAlive()) {
            playerTurn();
            if (!goblin.isAlive()) break;
            enemyTurn();
        }
        if (goblin.isAlive()) {
            std::cout << "Link foi derrotado pelo Goblin!" << std::endl;
        } else {
            std::cout << "Você derrotou o Goblin! Parabéns!" << std::endl;
        }
    }

private:
    void playerTurn() {
        std::cout << "Escolha seu ataque: " << std::endl;
        std::cout << "1. Espada (10 de dano)" << std::endl;
        std::cout << "2. Arco e Flecha (15 de dano)" << std::endl;
        std::cout << "3. Arco e Flechas Explosivas (20 de dano)" << std::endl;
        std::cout << "4. Ataque Especial Mágico (35 de dano)" << std::endl;
        int choice;
        std::cin >> choice;

        int damage = 0;
        switch (choice) {
            case 1: damage = 10; break;
            case 2: damage = 15; break;
            case 3: damage = 20; break;
            case 4: damage = 35; break;
            default: std::cout << "Escolha inválida, turno perdido!" << std::endl; return;
        }

        goblin.takeDamage(damage);
        goblin.showHpPercentage();
    }

    void enemyTurn() {
        link.takeDamage(5);
        link.showHpPercentage();
    }
};

int main() {
    Game game;
    game.start();
    return 0;
}
