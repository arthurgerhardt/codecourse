namespace Operacoes;

public class Operacoes
{
    public (int resultadoAdicao, string autor) Adicionar(int valor1, int valor2)
    {
        var resultado = valor1 + valor2;
        return (resultado, "Arthur");
    }

    public void Teste(int valor1, int valor2 = 7)
    {
        Console.WriteLine(valor1 + valor2);
    } 
}