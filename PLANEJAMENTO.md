# Planejamento de estudos — Python

Este é o roteiro permanente dos blocos 01 a 04. Os exercícios são cumulativos: use o que aprendeu nos blocos anteriores. Os enunciados são pontos de partida, sem soluções prontas.

## Como usar

1. Estude o assunto em uma aula ou livro e faça suas anotações no Obsidian.
2. Tente resolver os exercícios sozinho, na ordem sugerida. Marque `[x]` quando concluir cada um.
3. Salve cada exercício na pasta do bloco, com número e nome descritivo, por exemplo `02-lacos/01_contagem_crescente.py`.
4. Comece o arquivo com o enunciado, a fonte e seu raciocínio em comentários, como no README. Para os enunciados deste roteiro, a fonte pode ser `PLANEJAMENTO.md`.
5. Teste entradas diferentes, faça commits pequenos e volte a resolver alguns exercícios dias depois, sem consultar a primeira solução.

Os itens do bloco 01 abaixo correspondem aos arquivos já presentes no repositório. As pastas seguintes podem ser criadas quando você começar cada bloco. A numeração recomeça em cada pasta.

---

## 01 — Básico (`01-basico/`)

**Estudar:** variáveis, tipos, entrada e saída, conversão de tipos, operadores aritméticos, relacionais e lógicos, `if`, `elif` e `else`.

**Objetivo:** receber dados, fazer cálculos e tomar decisões. Exercícios registrados no repositório:

- [x] **01 — Boas-vindas:** leia o nome e mostre uma mensagem personalizada. `01_Boas_Vindas.py`
- [x] **02 — Apresentação:** crie variáveis para nome, cidade e idade e apresente esses dados. `02_Apresentacao.py`
- [x] **03 — Tipos:** experimente diferentes tipos de dados e sua manipulação. `03_Tipos.py`
- [x] **04 — Soma:** leia dois números e mostre a soma. `04_soma_dois_numeros.py`
- [x] **05 — Antecessor e sucessor:** leia um inteiro e mostre seus vizinhos. `05_antecessor_sucessor.py`
- [x] **06 — Operadores aritméticos:** leia dois números diferentes de zero e mostre as operações aritméticas, incluindo divisão inteira, resto e potência. `06_operadores_aritmeticos.py`
- [x] **07 — Média de notas:** leia três notas e mostre a média com duas casas decimais. `07_media_notas.py`
- [x] **08 — Conversor de temperatura:** converta Celsius para Fahrenheit. `08_conversor_temperatura.py`
- [x] **09 — Desconto:** leia preço e percentual de desconto; mostre o desconto e o preço final. `09_desconto_produto.py`
- [x] **10 — Par ou ímpar:** leia um inteiro e identifique sua paridade. `10_par_ou_impar.py`
- [x] **11 — Comparar números:** informe se o primeiro número é maior, menor ou igual ao segundo. `11_comparar_numeros.py`
- [x] **12 — Situação do aluno:** calcule a média de três notas e classifique como reprovado, em recuperação ou aprovado. `12_situacao_aluno.py`
- [x] **13 — Validação de nota:** informe se uma nota está entre 0 e 10, inclusive. `13_validacao_nota.py`
- [x] **14 — Acesso ao evento:** permita a entrada de maiores de idade ou de pessoas acompanhadas por responsável. `14_acesso_evento.py`
- [x] **15 — Calculadora condicional:** leia dois números e uma operação; trate operação inválida e divisão por zero. `15_calculadora_condicional.py`

**Revisão:** refaça par ou ímpar e a calculadora sem consultar os arquivos. Explique quando usar `and`, `or` e `elif`.

---

## 02 — Laços (`02-lacos/`)

**Estudar:** `while`, `for`, `range`, contadores, acumuladores, laços aninhados, `break` e `continue`.

**Objetivo:** repetir ações com quantidade conhecida ou até uma condição ser atendida. Em cada laço, identifique quando ele começa, como avança e quando termina.

- [ ] **01 — Contagem crescente:** use `while` para mostrar os números de 1 a 10 e, ao final, a mensagem “Fim!”.
- [ ] **02 — Contagem regressiva:** leia um inteiro positivo e mostre a contagem dele até zero usando `while`.
- [ ] **03 — Repetir até zero:** leia inteiros até o usuário digitar zero; mostre quantos números diferentes de zero foram informados.
- [ ] **04 — Nota válida:** peça uma nota até receber um valor de 0 a 10, inclusive; depois mostre a nota aceita. Considere entradas numéricas.
- [ ] **05 — Contagem com `for`:** mostre os números de 1 a 20 usando `for` e `range`.
- [ ] **06 — Números pares:** mostre os números pares de 0 a 50, inclusive, usando `for` e `range`.
- [ ] **07 — Tabuada:** leia um número e mostre sua tabuada de 1 a 10.
- [ ] **08 — Soma de sequência:** leia um inteiro positivo `n` e calcule a soma dos inteiros de 1 até `n` usando um acumulador.
- [ ] **09 — Média de várias notas:** leia a quantidade de notas, que deve ser positiva; leia as notas e mostre a média.
- [ ] **10 — Maior e menor:** leia cinco números e mostre o maior e o menor. Teste também uma sequência com números negativos.
- [ ] **11 — Contador de paridade:** leia dez inteiros e informe quantos são pares e quantos são ímpares.
- [ ] **12 — Parada com `break`:** leia números até o usuário digitar zero; use `break` para encerrar e mostre a soma dos valores anteriores.
- [ ] **13 — Pulando valores:** percorra os números de 1 a 20 e use `continue` para não mostrar os múltiplos de 3.
- [ ] **14 — Tabuadas aninhadas:** usando dois laços, mostre as tabuadas de 1 a 10, cada uma com multiplicadores de 1 a 10.
- [ ] **15 — Calculadora com menu:** adapte a calculadora do bloco 01 para repetir operações até o usuário escolher sair. Continue tratando operação inválida e divisão por zero.

**Revisão:** refaça a tabuada com `while` e depois com `for`. Confira casos de início, fim e entrada zero.

---

## 03 — Estruturas de dados (`03-estruturas-de-dados/`)

**Estudar:** strings, listas, tuplas, dicionários, índices, fatias, percursos e operações básicas de cada estrutura.

**Objetivo:** guardar e organizar vários valores, escolher a estrutura adequada e percorrer seus dados.

- [ ] **01 — Informações de uma frase:** leia uma frase e mostre a quantidade de caracteres, a versão em maiúsculas e a versão em minúsculas.
- [ ] **02 — Contagem de vogais:** leia uma frase e conte suas vogais, considerando letras maiúsculas e minúsculas. Para este exercício, use as vogais sem acento.
- [ ] **03 — Palíndromo:** leia uma palavra e informe se ela é igual quando lida de trás para frente, ignorando maiúsculas e minúsculas.
- [ ] **04 — Lista de compras:** leia cinco produtos, guarde-os em uma lista e mostre cada item numerado.
- [ ] **05 — Números na lista:** leia cinco números, guarde-os em uma lista e mostre a soma, a média, o maior e o menor.
- [ ] **06 — Busca em lista:** crie uma lista de nomes, peça um nome e informe se ele está presente. Defina como tratar maiúsculas e minúsculas.
- [ ] **07 — Inserir e remover:** monte uma lista de tarefas com opções para adicionar, listar e remover uma tarefa pelo nome; avise se ela não existir. Encerre pelo menu.
- [ ] **08 — Pares e ímpares:** leia dez inteiros, guarde-os em uma lista e mostre separadamente os pares e os ímpares.
- [ ] **09 — Sem repetição:** leia números até o usuário digitar zero; guarde cada valor diferente de zero apenas uma vez e mostre a lista final.
- [ ] **10 — Tupla de produtos:** crie uma tupla com pelo menos cinco nomes de produtos. Mostre todos os itens, o primeiro, o último e quantos existem.
- [ ] **11 — Estatísticas em tupla:** leia cinco números e guarde-os em uma tupla. Mostre quantas vezes um número escolhido aparece e sua primeira posição, se estiver presente.
- [ ] **12 — Cadastro com dicionário:** leia nome, idade e cidade de uma pessoa e armazene os dados em um dicionário; depois apresente-os.
- [ ] **13 — Boletim:** guarde em um dicionário o nome e três notas de um aluno. Calcule a média e informe a situação usando os critérios do exercício 12 do bloco 01.
- [ ] **14 — Contagem de palavras:** leia uma frase e conte quantas vezes cada palavra aparece, ignorando maiúsculas e minúsculas. Para começar, considere palavras separadas por espaços.
- [ ] **15 — Agenda em memória:** crie um menu para cadastrar, buscar, listar e remover contatos em um dicionário de nome e telefone. Avise quando um nome não existir e permita sair.

**Revisão:** explique a diferença entre lista, tupla e dicionário e escolha uma situação adequada para cada um. Teste buscas por itens ausentes e listas vazias quando aplicável.

---

## 04 — Funções e erros (`04-funcoes-e-erros/`)

**Estudar:** definição e chamada de funções, parâmetros, `return`, escopo básico, `try`/`except`, arquivos de texto e `with`.

**Objetivo:** dividir programas em partes reutilizáveis, tratar erros esperados e guardar dados em arquivos.

- [ ] **01 — Saudação:** crie uma função que receba um nome e retorne uma saudação; peça o nome e mostre o resultado.
- [ ] **02 — Soma:** crie uma função que receba dois números e retorne a soma. Chame-a com valores informados pelo usuário.
- [ ] **03 — Paridade:** crie uma função que receba um inteiro e retorne se ele é par. Use o resultado para mostrar uma mensagem.
- [ ] **04 — Média:** crie uma função que receba três notas e retorne a média. Fora da função, apresente o resultado formatado.
- [ ] **05 — Situação do aluno:** crie uma função que receba uma média e retorne a situação conforme os critérios do bloco 01; teste as fronteiras 5 e 7.
- [ ] **06 — Maior de três:** crie uma função que receba três números e retorne o maior. Teste também valores iguais.
- [ ] **07 — Tabuada como função:** crie uma função que receba um número e mostre sua tabuada de 1 a 10; chame-a com um valor lido.
- [ ] **08 — Contagem de vogais:** crie uma função que receba um texto e retorne a quantidade de vogais sem acento, ignorando maiúsculas e minúsculas.
- [ ] **09 — Média de lista:** crie uma função que receba uma lista de números e retorne a média; defina e documente o comportamento para lista vazia.
- [ ] **10 — Conversão segura:** peça um inteiro e use `try`/`except` para informar quando a entrada não puder ser convertida.
- [ ] **11 — Leitura repetida:** crie uma função que peça um inteiro até receber uma entrada válida e o retorne. Trate o erro de conversão.
- [ ] **12 — Divisão segura:** crie uma função que receba dois números e retorne o resultado da divisão. Trate divisão por zero no programa e informe o problema.
- [ ] **13 — Gravar arquivo:** peça uma anotação e grave-a em um arquivo de texto usando `with`. Informe que a gravação foi concluída; escolha um nome de arquivo para o exercício.
- [ ] **14 — Ler arquivo:** leia e mostre o conteúdo do arquivo de anotações. Trate o caso em que o arquivo ainda não existe.
- [ ] **15 — Agenda persistente:** crie um menu com funções para adicionar e listar contatos. Guarde nome e telefone em um arquivo de texto, carregue os dados ao iniciar e trate a ausência inicial do arquivo. Defina um formato de armazenamento e evite apagar contatos já salvos ao adicionar outro.

**Revisão:** explique a diferença entre mostrar um valor com `print` e devolvê-lo com `return`. Teste entradas inválidas, divisão por zero e leitura de um arquivo inexistente.

---

Ao concluir os quatro blocos, revise os pontos em que teve dificuldade e siga para os mini projetos do bloco 05 descritos no README.
