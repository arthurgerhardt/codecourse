# Algoritmo de Controle de Estoque

# Inicialização das listas para armazenar os produtos
produtos = []
estoque = []

# Função para cadastrar um novo produto
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    codigo = len(produtos) + 1  # Gera um código sequencial
    produtos.append({"codigo": codigo, "nome": nome, "descricao": descricao})
    estoque.append({"codigo": codigo, "quantidade": quantidade})

# Função para consultar o estoque de um produto
def consultar_estoque():
    codigo = int(input("Digite o código do produto: "))
    for item in estoque:
        if item["codigo"] == codigo:
            print(f"Produto: {produtos[codigo-1]['nome']}")
            print(f"Quantidade em estoque: {item['quantidade']}")
            break
    else:
        print("Produto não encontrado.")

# Função para imprimir o relatório de estoque
def imprimir_relatorio():
    print("Relatório de Estoque:")
    for produto in produtos:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Descrição: {produto['descricao']}")
        for item in estoque:
            if item["codigo"] == produto["codigo"]:
                print(f"Quantidade em estoque: {item['quantidade']}")
                break
    print("Fim do relatório.")

# Menu principal
while True:
    print("\nMenu:")
    print("1. Cadastrar produto")
    print("2. Consultar estoque")
    print("3. Imprimir relatório")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        consultar_estoque()
    elif opcao == 3:
        imprimir_relatorio()
    elif opcao == 4:
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
