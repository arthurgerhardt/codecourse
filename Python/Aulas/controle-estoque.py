import sqlite3

# Conectar ao banco de dados SQLite
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()

# Criar a tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')
conexao.commit()

def cadastrar_produto(nome, quantidade, preco):
    cursor.execute('''
    INSERT INTO produtos (nome, quantidade, preco)
    VALUES (?, ?, ?)
    ''', (nome, quantidade, preco))
    conexao.commit()
    print(f"Produto {nome} cadastrado com sucesso!")

def editar_produto(id, novo_nome=None, nova_quantidade=None, novo_preco=None):
    if novo_nome:
        cursor.execute('''
        UPDATE produtos
        SET nome = ?
        WHERE id = ?
        ''', (novo_nome, id))
    if nova_quantidade is not None:
        cursor.execute('''
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
        ''', (nova_quantidade, id))
    if novo_preco is not None:
        cursor.execute('''
        UPDATE produtos
        SET preco = ?
        WHERE id = ?
        ''', (novo_preco, id))
    conexao.commit()
    print(f"Produto com ID {id} editado com sucesso!")

def remover_produto(id):
    cursor.execute('''
    DELETE FROM produtos
    WHERE id = ?
    ''', (id,))
    conexao.commit()
    print(f"Produto com ID {id} removido com sucesso!")

def listar_produtos():
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar produto")
        print("2. Editar produto")
        print("3. Remover produto")
        print("4. Listar produtos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            cadastrar_produto(nome, quantidade, preco)
        elif opcao == '2':
            id = int(input("ID do produto a editar: "))
            print("Deixe em branco se não quiser alterar.")
            novo_nome = input("Novo nome: ")
            nova_quantidade = input("Nova quantidade: ")
            novo_preco = input("Novo preço: ")
            editar_produto(id, novo_nome or None, int(nova_quantidade) if nova_quantidade else None, float(novo_preco) if novo_preco else None)
        elif opcao == '3':
            id = int(input("ID do produto a remover: "))
            remover_produto(id)
        elif opcao == '4':
            listar_produtos()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()

# Fechar a conexão com o banco de dados
conexao.close()
