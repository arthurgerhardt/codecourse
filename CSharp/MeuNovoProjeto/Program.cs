using System;

using MeuNovoProjeto.Teste;

namespace MeuNovoProjeto
{
    class Program
    {
        static void Main(string[] args)
        {
            Carro meuCarro = new Carro();
            meuCarro.Ligar();
            meuCarro.Desligar();
            Biscoito meuBiscoito = new Biscoito();
            meuBiscoito.Temperatura();
            meuCarro.Teste2();
        }
    }
}
