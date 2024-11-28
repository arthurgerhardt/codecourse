using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace MeuNovoProjeto
{
    class Carro
    {
        public void Ligar()
        {
            Console.WriteLine("Carro ligado");
        }

        public void Desligar()
        {
            Console.WriteLine("Carro desligado");
        }

        private void Teste1()
        {
            Console.WriteLine("Teste 1");
        }

        internal void Teste2()
        {
            Teste1();
            Console.WriteLine("Teste 2");
        }
    }
}