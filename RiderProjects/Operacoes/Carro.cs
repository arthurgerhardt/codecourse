namespace Operacoes;

public class Carro
{
    public string Modelo { get; set; }
    public DateOnly LancadoEm { get; set; }
    public Cor Cor { get; set; }

    public void NomeDoModelo()
    {
        Console.WriteLine($"Nome do modelo: {Modelo}");
        Console.WriteLine($"Ano de lançamento: {LancadoEm}");
        Console.WriteLine($"Cor: {Cor}");
    }
}

