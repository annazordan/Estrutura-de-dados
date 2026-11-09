# Projeto Ladies Tech — Análise de Rede de Conexões com Grafos

**Alunas:** Anna Clara, Isabela e Mariana  
**Disciplina:** Estrutura de Dados 

**Tema:** Análise de redes sociais utilizando grafos

---

## 1. O desafio

O projeto Ladies Tech tem como objetivo analisar uma rede social fictícia utilizando os conceitos da teoria dos grafos.

Nossa missão é representar as amizades entre os usuários, identificar suas conexões, calcular os graus dos vértices, determinar a quantidade de arestas e analisar a densidade da rede.

Para isso, utilizamos um grafo com **12 usuários e 17 amizades**, além da linguagem Python para realizar os cálculos.

O grafo é não direcionado, pois as amizades são recíprocas.

## 2. Conceitos essenciais

Os principais conceitos utilizados no projeto são:

- **Vértice (nó):** representa uma pessoa da rede social.
- **Aresta:** representa uma amizade entre dois usuários.
- **Grau:** quantidade de conexões diretas que um usuário possui.
- **Caminho:** sequência de vértices conectados que permite chegar de um usuário a outro.
- **Densidade:** medida que indica a proporção de conexões existentes em relação ao total de conexões possíveis.
- **Grafo não direcionado:** estrutura em que as conexões não possuem direção, representando amizades recíprocas.

Esses conceitos permitem compreender a organização da rede e identificar padrões de relacionamento entre os usuários.

## 3. Conheça os usuários

O grafo é composto por 12 usuários:

| Código | Usuário |
|---|---|
| A | lauraz |
| B | fernandagil |
| C | thalyana |
| D | maria_anq |
| E | Saara.lima |
| F | isa.linhares |
| G | emily.dev |
| H | leticiagly |
| I | annanadroz |
| J | eusolz |
| K | ths.llys |
| L | ysadox |

### Lista de amizades

As 17 conexões representadas no grafo são:

1. lauraz — fernandagil
2. lauraz — thalyana
3. fernandagil — maria_anq
4. thalyana — maria_anq
5. thalyana — eusolz
6. maria_anq — isa.linhares
7. maria_anq — annanadroz
8. Saara.lima — isa.linhares
9. Saara.lima — emily.dev
10. isa.linhares — annanadroz
11. isa.linhares — leticiagly
12. emily.dev — leticiagly
13. leticiagly — ths.llys
14. annanadroz — eusolz
15. annanadroz — ths.llys
16. eusolz — ysadox
17. ths.llys — ysadox

**Total:** 12 vértices e 17 arestas.

## 4. Representação do grafo

O grafo foi construído utilizando 12 círculos, cada um representando um usuário.

As amizades são representadas por linhas que conectam os vértices.

Como o grafo é não direcionado, não existem setas, pois cada amizade representa uma conexão recíproca.

A representação visual permite identificar os usuários com mais conexões, os diferentes caminhos disponíveis e a estrutura geral da rede.

O desenho utilizado no projeto corresponde ao grafo fornecido na atividade.

## 5. Cálculo do grau de cada usuário

O grau de um vértice corresponde à quantidade de arestas conectadas diretamente a ele.

| Usuário | Amigos diretos | Grau |
|---|---|---:|
| lauraz | fernandagil, thalyana | 2 |
| fernandagil | lauraz, maria_anq | 2 |
| thalyana | lauraz, maria_anq, eusolz | 3 |
| maria_anq | fernandagil, thalyana, isa.linhares, annanadroz | 4 |
| Saara.lima | isa.linhares, emily.dev | 2 |
| isa.linhares | Saara.lima, maria_anq, annanadroz, leticiagly | 4 |
| emily.dev | Saara.lima, leticiagly | 2 |
| leticiagly | emily.dev, isa.linhares, ths.llys | 3 |
| annanadroz | maria_anq, isa.linhares, eusolz, ths.llys | 4 |
| eusolz | thalyana, annanadroz, ysadox | 3 |
| ths.llys | leticiagly, annanadroz, ysadox | 3 |
| ysadox | eusolz, ths.llys | 2 |

### Pergunta 1 — Quem tem mais conexões diretas?

Os usuários **maria_anq, isa.linhares e annanadroz** possuem o maior número de conexões diretas, com 4 amizades cada.

Esses três usuários apresentam o maior grau da rede.

Entretanto, ter mais conexões não significa necessariamente ser o mais influente. A influência também pode depender da posição do usuário no grafo e de sua capacidade de conectar grupos diferentes.

## 6. Cálculo do número de amizades

Para encontrar o número total de arestas do grafo, somamos todos os graus e dividimos por dois.

Isso ocorre porque cada amizade é contabilizada duas vezes: uma para cada usuário conectado.

**Fórmula:**

Número de arestas = Soma dos graus ÷ 2

### Passo 1 — Soma dos graus

2 + 2 + 3 + 4 + 2 + 4 + 2 + 3 + 4 + 3 + 3 + 2 = 34

### Passo 2 — Divisão por dois

E = 34 ÷ 2

**E = 17**

### Resultado

O grafo possui **17 arestas**, representando 17 amizades únicas entre os usuários.

## 7. Cálculo da densidade do grafo

A densidade indica a proporção de amizades existentes em relação ao total de amizades possíveis.

Para um grafo simples não direcionado, utilizamos:

**Fórmula:**

D = (2 × E) / (V × (V − 1))

Onde:

- D = densidade
- E = número de arestas
- V = número de vértices

### Passo 1 — Identificar os valores

V = 12

E = 17

### Passo 2 — Substituir na fórmula

D = (2 × 17) / (12 × (12 − 1))

D = 34 / (12 × 11)

D = 34 / 132

D ≈ 0,2576

### Passo 3 — Converter em porcentagem

D ≈ 25,76%

### Resultado

**A densidade da rede é aproximadamente 25,76%.**

### Interpretação

A rede possui aproximadamente 25,76% das conexões possíveis.

Isso indica que, apesar de existirem amizades entre os usuários, ainda há muitas possibilidades de novas conexões.

Como cerca de 74,24% das amizades possíveis ainda não existem, consideramos a densidade relativamente baixa.

## 8. Representação do grafo em Python

Para representar a rede em Python, utilizamos um dicionário chamado `rede`.

Cada usuário é uma chave do dicionário, e seus amigos diretos são armazenados em uma lista.

O programa permite calcular automaticamente o grau de cada usuário, a soma dos graus, o número de arestas, a densidade e os usuários com mais conexões.

### Código Python completo

```python
# Projeto Ladies Tech - Analise de Rede de Conexoes
# Alunas: Anna Clara, Isabela e Mariana

rede = {
    "lauraz": ["fernandagil", "thalyana"],

    "fernandagil": ["lauraz", "maria_anq"],

    "thalyana": ["lauraz", "maria_anq", "eusolz"],

    "maria_anq": ["fernandagil", "thalyana",
                  "isa.linhares", "annanadroz"],

    "Saara.lima": ["isa.linhares", "emily.dev"],

    "isa.linhares": ["Saara.lima", "maria_anq",
                     "annanadroz", "leticiagly"],

    "emily.dev": ["Saara.lima", "leticiagly"],

    "leticiagly": ["emily.dev", "isa.linhares",
                   "ths.llys"],

    "annanadroz": ["maria_anq", "isa.linhares",
                    "eusolz", "ths.llys"],

    "eusolz": ["thalyana", "annanadroz", "ysadox"],

    "ths.llys": ["leticiagly", "annanadroz", "ysadox"],

    "ysadox": ["eusolz", "ths.llys"]
}

# Quantidade de usuarios
n = len(rede)

# Calcule o grau de cada usuario
for usuario, amigos in rede.items():
    print(usuario, "tem", len(amigos), "conexoes")

# A soma dos graus conta cada amizade duas vezes
soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2

print("\nTotal de usuarios:", n)
print("Soma dos graus:", soma_graus)
print("Total de amizades:", arestas)

# Densidade do grafo
densidade = (2 * arestas) / (n * (n - 1))
print(f"Densidade: {densidade:.2%}")

# Identificar os usuarios com mais conexoes
maior_grau = max(len(amigos) for amigos in rede.values())

print("\nUsuarios com mais conexoes:")
for usuario, amigos in rede.items():
    if len(amigos) == maior_grau:
        print(usuario, "-", maior_grau, "conexoes")
```

### Explicação do código

1. `rede` armazena os usuários e seus amigos diretos.
2. `len(rede)` conta a quantidade de usuários.
3. `for` percorre cada usuário e sua lista de amigos.
4. `len(amigos)` calcula o grau de cada vértice.
5. `sum(...)` soma os graus de todos os vértices.
6. `// 2` divide a soma dos graus por dois, evitando contar uma amizade duas vezes.
7. A fórmula da densidade calcula a proporção de conexões existentes.
8. `max(...)` identifica o maior grau encontrado.
9. O último `for` apresenta os usuários que possuem o maior número de amizades.

## 9. Encontrando um caminho no grafo

Um caminho é uma sequência de usuários conectados por amizades.

### Exemplo 1 — Caminho de lauraz até leticiagly

lauraz → fernandagil → maria_anq → isa.linhares → leticiagly

**Quantidade de arestas:** 4.

### Exemplo 2 — Outro caminho com a mesma quantidade de arestas

lauraz → thalyana → maria_anq → isa.linhares → leticiagly

**Quantidade de arestas:** 4.

### Interpretação

Os dois caminhos permitem chegar ao mesmo usuário utilizando quatro arestas.

Isso demonstra que uma rede pode apresentar diferentes caminhos entre duas pessoas.

A análise de caminhos é importante para compreender como informações podem circular pela rede e como usuários podem se conectar indiretamente.

## 10. Desafio em grupo — Ampliação da rede

Para realizar o desafio de ampliação, consideramos inicialmente um subgrafo formado por seis usuários:

- lauraz
- fernandagil
- thalyana
- maria_anq
- isa.linhares
- annanadroz

Esse subgrafo possui 6 vértices e 7 arestas.

Posteriormente, incluímos outros seis usuários:

- Saara.lima
- emily.dev
- leticiagly
- eusolz
- ths.llys
- ysadox

A rede ampliada passa a apresentar os 12 usuários e as 17 amizades do grafo final.

### Comparação antes e depois

| Indicador | Rede inicial | Rede ampliada |
|---|---:|---:|
| Usuários | 6 | 12 |
| Arestas | 7 | 17 |
| Soma dos graus | 14 | 34 |
| Densidade | 46,67% | 25,76% |

### Análise da ampliação

A ampliação adicionou seis usuários e dez amizades.

Embora o número de conexões tenha aumentado, a densidade diminuiu de 46,67% para 25,76%.

Isso acontece porque, quanto maior a quantidade de usuários, maior será o número de amizades possíveis.

Portanto, aumentar o número de arestas não significa necessariamente aumentar a densidade.

### Quem possui mais conexões?

Os usuários com maior grau na rede ampliada são:

- maria_anq: 4 conexões.
- isa.linhares: 4 conexões.
- annanadroz: 4 conexões.

### Como sugerir uma amizade utilizando amigos em comum?

Uma rede social pode comparar as listas de amizades de dois usuários.

Por exemplo:

- thalyana é amiga de maria_anq e eusolz.
- annanadroz também é amiga de maria_anq e eusolz.

Como thalyana e annanadroz ainda não possuem uma amizade direta, a rede poderia recomendar uma conexão entre elas.

Essa estratégia é conhecida como recomendação baseada em vizinhos comuns.

## 11. Entrega do projeto

O projeto apresenta a representação do grafo, a identificação dos graus, os cálculos de arestas e densidade, a implementação em Python e as análises das conexões.

### Resumo dos resultados

| Indicador | Resultado |
|---|---|
| Tipo de grafo | Não direcionado |
| Número de usuários | 12 |
| Número de amizades | 17 |
| Soma dos graus | 34 |
| Densidade | 25,76% |
| Maior grau encontrado | 4 |
| Usuários com maior grau | maria_anq, isa.linhares e annanadroz |

### Conclusão do projeto

O desenvolvimento do projeto Ladies Tech permitiu compreender como a teoria dos grafos pode ser aplicada na representação de redes sociais.

Por meio da análise, identificamos 12 usuários conectados por 17 amizades, com densidade aproximada de 25,76%.

Os usuários maria_anq, isa.linhares e annanadroz possuem o maior grau da rede, com quatro conexões diretas cada.

Também observamos que uma rede pode crescer em quantidade de usuários e amizades sem necessariamente apresentar um aumento de densidade.

A utilização do Python facilitou a realização dos cálculos e demonstrou como a programação pode ser utilizada para analisar estruturas de dados e relações entre pessoas.

Assim, concluímos que os grafos são importantes ferramentas para compreender conexões, encontrar caminhos, identificar usuários com maior número de relacionamentos e desenvolver sistemas de recomendação.

## 12. Pergunta de reflexão

### Duas pessoas ainda não são amigas, mas possuem três amigos em comum. Como essa informação poderia ser utilizada para sugerir uma nova conexão?

Uma rede social pode utilizar os amigos em comum como critério para recomendar novas conexões.

Quando duas pessoas possuem três amigos em comum, existe a possibilidade de que participem de grupos sociais semelhantes.

Por isso, o sistema pode sugerir uma amizade entre elas.

Entretanto, a sugestão não significa que a amizade será criada automaticamente. A decisão deve permanecer com os usuários.

### Quais cuidados de privacidade devem ser considerados?

Ao analisar redes sociais, é necessário respeitar a privacidade e a segurança dos usuários.

Os principais cuidados são:

1. Proteger as informações pessoais dos participantes.
2. Respeitar as configurações de privacidade dos perfis.
3. Evitar o compartilhamento de dados sem autorização ou outra base legal adequada.
4. Utilizar apenas as informações necessárias para a análise.
5. Adotar medidas de segurança para impedir acessos indevidos.
6. Respeitar os princípios da Lei Geral de Proteção de Dados (LGPD).

### Outras métricas que podem descrever uma rede

Além do grau e da densidade, existem outras métricas importantes:

- **Centralidade:** ajuda a identificar usuários que ocupam posições importantes na rede.
- **Distância:** indica o menor número de arestas necessário para conectar dois usuários.
- **Centralidade de intermediação:** mede a participação de um usuário nos caminhos mais curtos entre outros usuários.
- **Coeficiente de agrupamento:** avalia o quanto os amigos de um usuário também estão conectados entre si.
- **Componentes conexas:** identificam grupos de usuários que possuem caminhos entre si.

### Conclusão da reflexão

A análise de redes sociais por meio de grafos permite compreender como os usuários se relacionam e como novas amizades podem ser recomendadas.

Entretanto, a utilização dessas informações deve respeitar a privacidade, a segurança e a liberdade de escolha de cada usuário.

---

**Projeto Ladies Tech — Redes Sociais com Grafos**

**Alunas:** Anna Clara, Isabela e Mariana

Estrutura de Dados 
