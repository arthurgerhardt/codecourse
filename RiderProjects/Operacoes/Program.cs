﻿using System;

namespace Operacoes
{
    // Classe Program com o método Main
    class Program
    {
        static void Main(string[] args)
        {
           var texto = Teste(5);
           Console.WriteLine(texto);
                
        }
        static string Teste(int numero) {
            Console.WriteLine("Teste 1");
            if(numero == 5)
            {
                Console.WriteLine("Teste 2");
                return "wellison";
            }
            Console.WriteLine("Teste 3");
            
            return "Willian";
        }
    }
}