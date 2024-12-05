# Não há necessidade de definir um pacote em Python
def main():
    for x in range(1, 5):
        print(x)
        if x == 4:
            print("Elemento 4.")

# Chama a função principal
if __name__ == "__main__":
    main()
