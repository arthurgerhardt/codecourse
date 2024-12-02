using System;

class Program
{
    class Character
    {
        public string Name { get; set; }
        public int Health { get; set; }

        public Character(string name, int health)
        {
            Name = name;
            Health = health;
        }

        public void Attack(Character target, int damage)
        {
            target.Health -= damage;
            Console.WriteLine($"{Name} ataca {target.Name} e causa {damage} de dano.");
        }

        public void SpecialAttack(Character target)
        {
            int specialDamage = 30;
            target.Health -= specialDamage;
            Console.WriteLine($"{Name} usa um ataque especial em {target.Name} e causa {specialDamage} de dano.");
        }
    }

    static void Main(string[] args)
    {
        Character hero = new Character("Link", 100);
        Character goblin = new Character("Goblin", 80);

        Console.WriteLine($"HP Inicial de {hero.Name}: {hero.Health}");
        Console.WriteLine($"HP Inicial de {goblin.Name}: {goblin.Health}\n");

        while (goblin.Health > 0 && hero.Health > 0)
        {
            Console.WriteLine("\nEscolha seu ataque:");
            Console.WriteLine("1. Espada (10 de dano)");
            Console.WriteLine("2. Arco e Flecha (10 de dano)");
            Console.WriteLine("3. Flechas Explosivas (10 de dano)");
            Console.WriteLine("4. Magia (30 de dano)");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    hero.Attack(goblin, 10);
                    break;
                case "2":
                    hero.Attack(goblin, 10);
                    break;
                case "3":
                    hero.Attack(goblin, 10);
                    break;
                case "4":
                    hero.SpecialAttack(goblin);
                    break;
                default:
                    Console.WriteLine("Opção inválida. Tente novamente.");
                    continue;
            }

            Console.WriteLine($"HP de {hero.Name}: {hero.Health}");
            Console.WriteLine($"HP de {goblin.Name}: {goblin.Health}");

            if (goblin.Health <= 0)
            {
                Console.WriteLine("\nParabéns, você venceu o Goblin!");
            }
        }
    }
}
