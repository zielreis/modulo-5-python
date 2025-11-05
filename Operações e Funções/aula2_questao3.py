import random

# 1️⃣ Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# 2️⃣ Criar uma lista interseção sem duplicatas
interseccao = sorted(list(set(lista1) & set(lista2)))

# 3️⃣ Exibir as listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# 4️⃣ Exibir a interseção ordenada
print("\nInterseccao:", interseccao)

# 5️⃣ Exibir a contagem de cada elemento nas duas listas
print("\nContagem:")
for valor in interseccao:
    print(f"{valor}: (lista1={lista1.count(valor)}, lista2={lista2.count(valor)})")
