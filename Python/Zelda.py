class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target, damage):
        target.health -= damage
        print(f"{self.name} ataca {target.name} e causa {damage} de dano.")

    def special_attack(self, target):
        special_damage = 30
        target.health -= special_damage
        print(f"{self.name} usa um ataque especial em {target.name} e causa {special_damage} de dano.")

# Criação dos personagens
hero = Character("Link", 100)
goblin = Character("Goblin", 80)

# Exibir HP inicial
print(f"HP Inicial de {hero.name}: {hero.health}")
print(f"HP Inicial de {goblin.name}: {goblin.health}\n")

# Simulação de batalha
while goblin.health > 0 and hero.health > 0:
    print("\nEscolha seu ataque:")
    print("1. Espada (10 de dano)")
    print("2. Arco e Flecha (10 de dano)")
    print("3. Flechas Explosivas (10 de dano)")
    print("4. Magia (30 de dano)")
    choice = input()

    if choice == "1":
        hero.attack(goblin, 10)
    elif choice == "2":
        hero.attack(goblin, 10)
    elif choice == "3":
        hero.attack(goblin, 10)
    elif choice == "4":
        hero.special_attack(goblin)
    else:
        print("Opção inválida. Tente novamente.")
        continue

    print(f"HP de {hero.name}: {hero.health}")
    print(f"HP de {goblin.name}: {goblin.health}")

    if goblin.health <= 0:
        print("\nParabéns, você venceu o Goblin!")
