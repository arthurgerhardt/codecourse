import sqlite3

def connect_to_db(db_name=":memory:"):
    return sqlite3.connect(db_name)

def create_table(conn, table_name):
    cursor = conn.cursor()
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """
    cursor.execute(query)
    conn.commit()
    print(f"Tabela {table_name} criada com sucesso.")

def insert_data(conn, table_name, name, age):
    cursor = conn.cursor()
    query = f"INSERT INTO {table_name} (name, age) VALUES (?, ?)"
    cursor.execute(query, (name, age))
    conn.commit()
    print(f"Dados inseridos na tabela {table_name} com sucesso.")

def query_table(conn, table_name):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_table(conn, table_name):
    cursor = conn.cursor()
    query = f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(query)
    conn.commit()
    print(f"Tabela {table_name} excluída com sucesso.")

def main():
    conn = connect_to_db("example.db")
    
    while True:
        print("\nMenu:")
        print("1. Criar tabela")
        print("2. Inserir dados na tabela")
        print("3. Consultar tabela")
        print("4. Excluir tabela")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            table_name = input("Digite o nome da tabela: ")
            create_table(conn, table_name)
        elif choice == '2':
            table_name = input("Digite o nome da tabela: ")
            name = input("Digite o nome: ")
            age = int(input("Digite a idade: "))
            insert_data(conn, table_name, name, age)
        elif choice == '3':
            table_name = input("Digite o nome da tabela: ")
            query_table(conn, table_name)
        elif choice == '4':
            table_name = input("Digite o nome da tabela: ")
            delete_table(conn, table_name)
        elif choice == '5':
            conn.close()
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
