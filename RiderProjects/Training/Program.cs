using System;

class Program

{
    static void Main(string[] args)
 
       {
            // Solicita o nome do usuário
            Console.WriteLine("Digite o seu nome: ");
            string nome = Console.ReadLine();
            Console.WriteLine("Digite o seu sobrenome: ");
            string sobrenome = Console.ReadLine();
            Console.WriteLine("Digite a sua idade: ");
            int idade = Convert.ToInt32(Console.ReadLine());

            if (idade >= 18)
            {
                Console.WriteLine("Você é maior de 18 anos e tem a idade de: " + idade + " anos.");
            }
            else if (idade <= 17 && idade < 18)
            {
                Console.WriteLine("Você é menor de idade e a sua idade é: " + idade + " anos.");
            }
            // Exibe o nome digitado pelo usuário
            Console.WriteLine("Olá, " + nome + " " +  sobrenome + "! Bem vindo ao programa!");
       }
}