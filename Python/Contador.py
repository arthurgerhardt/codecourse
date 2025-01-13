import time

start_time = time.time()

for i in range(1, 1000000001):
    pass  # Contando até um bilhão

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Tempo de execução: {elapsed_time} segundos")
