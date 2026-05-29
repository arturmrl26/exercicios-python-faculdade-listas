"""
Exercício 02 - Controle de Multas de Veículos
Disciplina: Algoritmos e Estrutura de Dados
Descrição: Cadastra placa e valor de multa de 15 carros em listas paralelas.
           Calcula a média das multas e identifica veículos com multa >= R$300,00.
           Demonstra listas paralelas, indexação sincronizada e acumuladores.
"""

placas = []
multas = []

for i in range(15):
    print(f"\nCarro {i + 1}:")
    placa = input("  Digite a placa: ")
    multa = float(input("  Digite o valor da multa (R$): "))
    placas.append(placa)
    multas.append(multa)

# Cálculo da média usando acumulador
total = 0
for valor in multas:
    total += valor
media = total / 15

# Contagem de multas altas
contador = 0
for valor in multas:
    if valor >= 300:
        contador += 1

print("\n===== RESULTADOS =====")
print(f"Valor médio das multas    : R$ {media:.2f}")
print(f"Carros com multa >= R$300 : {contador}")

print("\nDetalhamento das multas >= R$300,00:")
for i in range(15):
    if multas[i] >= 300:
        print(f"  Placa: {placas[i]} | Multa: R$ {multas[i]:.2f}")
