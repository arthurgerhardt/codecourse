let estoqueProdutoA = 50;

function realizarVenda(quantidade) {
    if (quantidade > estoqueProdutoA) {
        console.log("Quantidade insuficiente em estoque.");
    } else {
        estoqueProdutoA -= quantidade;
        console.log(`Venda realizada com sucesso. Novo estoque: ${estoqueProdutoA}`);
    }
}