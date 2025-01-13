import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()
# Carregar o arquivo de som 
pygame.mixer.music.load("/Users/arthurdiasgomesgerhardt/codecourse/codecourse/Python/Modulo_02/Projeto/media/Zelda/Battle.mp3")

# Personagem: Classe mãe
class Personagem:
    def __init__(self, nome, vida, nivel):
        self._nome = nome
        self._vida = vida
        self._nivel = nivel

    def get_nome(self):
        return self._nome

    def get_vida(self):
        return self._vida

    def get_nivel(self):
        return self._nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self._vida -= dano
        if self._vida <= 0:
            self._vida = 0

    def atacar(self, alvo):
        dano = self._nivel * 4
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano.\n")

# Herói: Controlado pelo jogador
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self._habilidade = habilidade

    def get_habilidade(self):
        return self._habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo):
        dano = self._nivel * 15
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade {self.get_habilidade()} e causou {dano} de dano.\n")

    def ataque_one_hit_obliterator(self, alvo):
        alvo.receber_ataque(alvo.get_vida())
        print(f"{self.get_nome()} usou o One-Hit Obliterator e derrotou {alvo.get_nome()} em um único golpe!\n")

# Inimigo: Controlado pelo computador
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

class Jogo:
    """ Classe Orquestradora do jogo """
    def __init__(self):
        # Criar instâncias de herói e inimigo
        self.heroi = Heroi("Link", 1800, 10, "Espada Mestre")
        self.inimigo = Inimigo("Calamity Ganon", 1500, 7, "Chefe Final")
        
        # Tocar o som 
        pygame.mixer.music.play()

    def iniciar_batalha(self):
        """ Inicia a batalha entre o herói e o inimigo """
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("Detalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para continuar...")
            escolha = input("Escolha (1- Ataque normal, 2- Ataque especial, 3- One-Hit Obliterator): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
                if self.inimigo.get_vida() > 0:
                    self.inimigo.atacar(self.heroi)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
                if self.inimigo.get_vida() > 0:
                    self.inimigo.atacar(self.heroi)
            elif escolha == '3':
                self.heroi.ataque_one_hit_obliterator(self.inimigo)
                if self.inimigo.get_vida() > 0:
                    self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("Parabéns! Link venceu a batalha!")
        else:
            print("Game Over! Calamity Ganon venceu a batalha!")

# Manter o programa em execução para ouvir o som
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Criar instância do jogo e iniciar a batalha
if __name__ == "__main__":
    print("********************************************************************************")
    print("******************* The Legend of Zelda: Breath of the Wild ********************")
    print("************************* Bem-vindo ao jogo! Começar! **************************")
    print("********************************************************************************\n")

    print("Esta é a batalha final entre Link e Calamity Ganon\n")
    print("Calamity Ganon diz: Eu vou acabar com você, com a minha força e poder!")
    print("Link diz: Eu vou te derrotar, com a minha coragem e determinação!")
    print("Calamity Ganon diz: Então, vamos ver quem é o mais forte!")
    print("Link diz: Vamos ver, Calamity Ganon!\n")

    jogo = Jogo()
    jogo.iniciar_batalha()
