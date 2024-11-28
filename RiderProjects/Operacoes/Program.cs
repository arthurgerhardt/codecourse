using System;

namespace Operacoes
{
    // Classe Program com o método Main
    class Program
    {
        static void Main(string[] args)
        {
            var numero = 0;
            do
            {
                Console.WriteLine("Teste");
                numero++;
            } while (numero < 10);
            Console.WriteLine("Saiu do while.");
        }
    }
}