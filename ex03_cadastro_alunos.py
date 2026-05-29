"""
Exercício 03 - Cadastro de Alunos com Análise de Notas
Disciplina: Algoritmos e Estrutura de Dados
Descrição: Cadastra nome, nota e curso de N alunos em três listas paralelas.
           Calcula: total de alunos do curso TADS, média geral das notas
           e quantidade de alunos acima da média.
           Demonstra múltiplas listas paralelas, análise estatística e filtros.
"""

n = int(input("Quantos alunos deseja cadastrar? "))

nomes = []
notas = []
cursos = []

for i in range(n):
    print(f"\nAluno {i + 1}:")
    nome = input("  Nome: ")
    nota = float(input("  Nota: "))
    curso = input("  Curso (ccp ou tads): ").strip().lower()
    nomes.append(nome)
    notas.append(nota)
    cursos.append(curso)

# a) Quantidade de alunos do curso TADS
contador_tads = 0
for curso in cursos:
    if curso == "tads":
        contador_tads += 1

# b) Média das notas
total_notas = 0
for nota in notas:
    total_notas += nota
media = total_notas / n

# c) Alunos com nota acima da média
acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1

print("\n===== RESULTADOS =====")
print(f"a) Alunos do curso TADS        : {contador_tads}")
print(f"b) Média geral das notas       : {media:.2f}")
print(f"c) Alunos acima da média       : {acima_media}")
