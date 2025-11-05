import random

# 1️⃣ Gerar um número aleatório entre 5 e 20
num_elementos = random.randint(5, 20)

# 2️⃣ Gerar 'num_elementos' números aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# 3️⃣ Calcular soma e média
soma = sum(elementos)
media = soma / num_elementos

# 4️⃣ Exibir os resultados
print(f"Quantidade de elementos: {num_elementos}")
print("Lista de elementos:", elementos)
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
