"""
Exercício 01 - Separação de Pares e Ímpares
Disciplina: Algoritmos e Estrutura de Dados
Descrição: Lê N números inteiros do usuário e os separa em listas de pares e ímpares.
           Demonstra uso de listas, laço while com critério de parada e operador módulo.
"""

resp = "s"

valores = []
par = []
impar = []

while resp == "s":
    numero_inteiro = int(input("Digite um número inteiro: "))
    valores.append(numero_inteiro)
    resp = input("Deseja continuar? (s/n): ").strip().lower()

for num in valores:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"\nValores digitados : {valores}")
print(f"Números pares     : {par}")
print(f"Números ímpares   : {impar}")
