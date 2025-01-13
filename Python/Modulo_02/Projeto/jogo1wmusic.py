import random
import pygame

print("**************************************************************************************")
print("******************* The Legend of Zelda II: Adventure of Link ************************")
print("**************************************************************************************")
print("\n")
print("******************* Bem-vindo ao jogo The Legend of Zelda II *************************")
print("\n")

# Inicializar o mixer do pygame 
pygame.mixer.init()

# Carregar o arquivo MP3 
pygame.mixer.music.load('/Users/arthurdiasgomesgerhardt/codecourse/codecourse/rocketseat/Python/Modulo_02/Projeto/media/ZeldaII/Boss.mp3')

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
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
        return f"Nome do personagem: {self._nome}\nVida: {self._vida}\nNível: {self._nivel}"
    
    def receber_ataque(self, dano):
        self._vida -= dano
        if self._vida <= 0:
            self._vida = 0
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 9)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")
    
    def defender(self):
        defesa = random.randint(self.get_nivel() * 5, self.get_nivel() * 9)
        print(f"{self.get_nome()} defendeu e bloqueou {defesa} de dano")
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self._habilidade = habilidade

    def get_habilidade(self):
        return self._habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nHabilidade: {self._habilidade}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 10, self.get_nivel() * 20)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nTipo: {self.get_tipo()}\n"
    
class Jogo:
    """Classe orquestradora do jogo"""
    def __init__(self) -> None:
        self.heroi = Heroi("Link", 1000, 8, "Jump with Sword")
        self.inimigo = Inimigo("Dark Link", 900, 7, "Final Boss")
    
    def iniciar_batalha(self):
        """ Fazer a gestão da batalha em turnos """
        
        # Função para tocar a música 
        def tocar_musica():
            pygame.mixer.music.play(-1)  # -1 faz a música tocar em loop

        print("Iniciando batalha")

        # Tocar a música no início da batalha
        tocar_musica()

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\n Detalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha o ataque: (1 - Ataque, 2 - Defesa,  3 - Ataque especial, 4 - sair): \n")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
                self.inimigo.atacar(self.heroi)
            elif escolha == '2':
                self.heroi.defender()
                self.inimigo.atacar(self.heroi)
            elif escolha == '3':
                self.heroi.ataque_especial(self.inimigo)
                self.inimigo.atacar(self.heroi)
            elif escolha == '4':
                print("\n Fim do jogo")
                pygame.mixer.music.stop()
                break

        if self.heroi.get_vida() > 0:
            print("\n Parabéns! Você venceu a batalha!")
            print("\n Você salvou o reino de Hyrule!")
            print("\n Fim do jogo")
        else:
            print("\n Você perdeu a batalha!")

# Instanciando o jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()
