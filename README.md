# 🐍 Python — Estudos e Exercícios

Repositório onde eu guardo tudo o que faço enquanto estudo **Python** e **lógica de programação**: exercícios, desafios e mini projetos, organizados por tópico.

---

## 🎯 Objetivo

- Reforçar a base de **lógica de programação** usando Python
- Praticar todos os dias com exercícios, sem copiar solução pronta
- Manter um histórico público e organizado da minha evolução
- Chegar nos mini projetos com a base firme

---

## 🔁 Como eu estudo

Cada tópico segue o mesmo ciclo:

1. **Assistir** à aula (vídeos e cursos externos)
2. **Anotar** no Obsidian, com as minhas palavras
3. **Resolver** os exercícios sem olhar a solução
4. **Subir** aqui no GitHub com commit pequeno e claro
5. **Revisar** dias depois, refazendo alguns exercícios do zero

---

## 📁 Estrutura do repositório

```text
python-estudos/
├── README.md
├── 01-basico/                  # variáveis, tipos, input/print, operadores, condicionais
├── 02-lacos/                   # while, for, range
├── 03-estruturas-de-dados/     # listas, tuplas, dicionários, strings
├── 04-funcoes-e-erros/         # funções, tratamento de erros, arquivos
└── 05-projetos/                # mini projetos
```

Cada pasta tem os exercícios numerados, por exemplo: `01_media_de_notas.py`.

### Padrão de cada exercício

Todo arquivo começa com o enunciado e o raciocínio em comentários, antes do código:

```python
"""
Enunciado: calcular a média de 3 notas e dizer se o aluno foi aprovado.
Fonte: (lista, site ou curso de onde veio)

Raciocínio:
1. Ler as 3 notas
2. Somar e dividir por 3
3. Se a média >= 7, aprovado; senão, reprovado
"""

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f"Aprovado com média {media:.1f}")
else:
    print(f"Reprovado com média {media:.1f}")
```

---

## ✅ Progresso

### Bloco 1 — Básico
- [ ] Variáveis e tipos de dados
- [ ] Entrada e saída (`input` / `print`)
- [ ] Operadores aritméticos, relacionais e lógicos
- [ ] Condicionais (`if` / `elif` / `else`)

### Bloco 2 — Laços
- [ ] `while`
- [ ] `for` e `range`
- [ ] Laços aninhados
- [ ] `break` e `continue`

### Bloco 3 — Estruturas de dados
- [ ] Listas
- [ ] Tuplas
- [ ] Dicionários
- [ ] Strings

### Bloco 4 — Funções e erros
- [ ] Funções (parâmetros e retorno)
- [ ] Tratamento de erros (`try` / `except`)
- [ ] Leitura e escrita de arquivos

### Bloco 5 — Mini projetos
- [ ] Jogo de adivinhação
- [ ] Calculadora no terminal
- [ ] Cadastro em terminal
- [ ] Controle de gastos

---

## ▶️ Como executar

Precisa ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
# clonar o repositório
git clone https://github.com/SEU-USUARIO/python-estudos.git
cd python-estudos

# rodar um exercício
python 01-basico/01_media_de_notas.py
```

---

## 📚 Recursos que eu uso

- **Vídeo-aulas:** Curso em Vídeo (Python),CS50's Introduction to Programming with Python
- **Exercícios:** Lista de exercícios da Python Brasil, Beecrowd, Exercism (trilha de Python), HackerRank
- **Anotações:** Obsidian
- **Livros:** Introdução à Programação com Python (4ª Edição)

---

## 📝 Padrão de commits

Commits pequenos e frequentes, com mensagem direta:

```text
exercicio: média de notas (01-basico)
exercicio: tabuada com for (02-lacos)
revisao: refaz lista de condicionais
projeto: início do jogo de adivinhação
```

---

## 👤 Autor

**Alan** — estudante de Análise e Desenvolvimento de Sistemas, aprendendo Python com foco em back end.
