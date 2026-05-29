# 📋 Exercícios Python — Listas e Estruturas de Repetição

> Módulo de estudos focado em **listas**, **laços de repetição** e **análise de dados simples**.
> Cada exercício aplica esses fundamentos a cenários do mundo real.

---

## 📚 Sobre o Módulo

Exercícios da disciplina de **Algoritmos e Estrutura de Dados** cobrindo manipulação de listas em Python: criação dinâmica, listas paralelas, filtros, acumuladores e cálculos estatísticos básicos.

---

## 📂 Estrutura

```
listas-faculdade/
│
├── exercicios/
│   ├── ex01_pares_impares.py       # Separação de números em listas de pares e ímpares
│   ├── ex02_multas_veiculos.py     # Controle de multas com listas paralelas
│   └── ex03_cadastro_alunos.py    # Cadastro de alunos com análise estatística
│
└── README.md
```

---

## 🧩 Exercícios

### Exercício 01 — Separação de Pares e Ímpares
**Arquivo:** `exercicios/ex01_pares_impares.py`

O usuário insere quantos números quiser (critério de parada por decisão) e o programa os distribui automaticamente entre uma lista de pares e outra de ímpares.

**Conceitos praticados:**
- `while` com critério de parada controlado pelo usuário
- Método `.append()` para construção dinâmica de listas
- Operador módulo `%` para verificar paridade
- Percorrer listas com `for`

---

### Exercício 02 — Controle de Multas de Veículos
**Arquivo:** `exercicios/ex02_multas_veiculos.py`

Cadastra placa e valor de multa de 15 veículos em **listas paralelas** (índice `i` corresponde ao mesmo carro nas duas listas). Calcula média das multas e lista os veículos com multa acima de R$300,00.

**Conceitos praticados:**
- **Listas paralelas** — vínculo de dados entre listas por índice
- Acumulador para cálculo de média
- Filtro com `if` dentro de `for`
- Acesso simultâneo a múltiplas listas via `range()`

---

### Exercício 03 — Cadastro de Alunos com Análise de Notas
**Arquivo:** `exercicios/ex03_cadastro_alunos.py`

Cadastra N alunos com nome, nota e curso em três listas sincronizadas. Realiza três análises independentes: total por curso, média geral e contagem de alunos acima da média.

**Conceitos praticados:**
- **Três listas paralelas** gerenciadas simultaneamente
- Múltiplos percursos independentes (uma análise por laço)
- Filtro por string (nome do curso)
- Análise estatística básica: média e comparação relativa

---

## 🎯 Por que esses exercícios importam para o aprendizado?

### Listas são a porta de entrada para estruturas de dados
Antes de aprender dicionários, classes, bancos de dados ou APIs, você aprende a armazenar e processar coleções de dados. Esses exercícios constroem essa base de forma progressiva: do simples (separar números) ao mais elaborado (múltiplas listas sincronizadas com análise).

### Listas paralelas ensinam o conceito de relacionamento entre dados
O exercício de multas e o de alunos usam listas paralelas — uma técnica que aparece diretamente em bancos de dados relacionais (onde o índice é a chave primária), em arquivos CSV e em tabelas. Entender essa lógica facilita muito a transição para `dicionários`, `dataframes` do Pandas e tabelas SQL.

### Acumuladores e contadores são padrões universais
A lógica de `total += valor` e `contador += 1` aparece em toda linguagem de programação. É a base de qualquer relatório, dashboard ou sistema de métricas. Praticar esses padrões manualmente — sem `sum()` ou `len()` prontos — constrói o raciocínio algorítmico correto.

### Filtros em listas treinam o pensamento de consulta (query)
O `if valor >= 300` dentro de um `for` é, conceitualmente, um `WHERE valor >= 300` em SQL ou um `.filter()` em Pandas. Entender esse padrão manualmente facilita imensamente o aprendizado de frameworks de dados.

---

## 🌍 Casos Reais de Aplicação

| Exercício | Aplicação no Mundo Real |
|-----------|------------------------|
| **Pares e Ímpares** | Sistemas de roteamento de tarefas (dividir itens entre servidores pares/ímpares), algoritmos de ordenação e hashing, validação de números de documentos (CPF, código de barras usam dígito verificador com módulo). |
| **Multas de Veículos** | Sistemas de DETRAN e estacionamentos usam exatamente listas paralelas (ou tabelas equivalentes) para vincular placa → dados do veículo. Relatórios de frotas corporativas filtram veículos por faixa de custo. Fintechs geram alertas automáticos para transações acima de um limite. |
| **Cadastro de Alunos** | Plataformas como Moodle, Google Classroom e sistemas acadêmicos armazenam e analisam dados de alunos dessa forma. Sistemas de RH calculam médias salariais e identificam outliers. Qualquer dashboard de métricas (vendas, suporte, marketing) usa esses padrões de média e comparação relativa. |

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/python-faculdade.git

# Acesse a pasta deste módulo
cd python-faculdade/listas-faculdade

# Execute qualquer exercício
python exercicios/ex01_pares_impares.py
```

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)

---

## 👨‍🎓 Contexto

Este módulo faz parte de um repositório maior de exercícios de graduação. Cada pasta cobre um tema específico da disciplina de Algoritmos — juntos, formam um portfólio de aprendizado progressivo.

---

> *"Dominar listas é o primeiro passo para dominar qualquer estrutura de dados."*
