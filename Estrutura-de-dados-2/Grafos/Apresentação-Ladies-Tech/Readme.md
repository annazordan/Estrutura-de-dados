

# Análise de Rede de Conexões — Grafo

## Descrição
Alunas: Anna Clara, Isabela, Mariana
Este projeto apresenta a análise de uma rede de conexões entre **12 pessoas**, representada por um **grafo não direcionado**.

Cada pessoa corresponde a um **vértice (nó)**, e cada linha entre duas pessoas corresponde a uma **aresta (ligação)**. Como as conexões não têm setas, considera-se que são bidirecionais: se A está conectado a B, B também está conectado a A.

## Participantes

1. fernandagil
2. Saara.lima
3. emily.dev
4. leticiagly
5. ths.llys
6. ysadox
7. eusolz
8. thalyana
9. lauraaz
10. maria_anq
11. annanadroz
12. isa.linhares

## Conexões diretas

| Pessoa | Conectada a | Grau |
|---|---|---:|
| fernandagil | lauraaz, Saara.lima, maria_anq | 3 |
| Saara.lima | fernandagil, emily.dev, isa.linhares | 3 |
| emily.dev | Saara.lima, leticiagly | 2 |
| leticiagly | emily.dev, isa.linhares, ths.llys | 3 |
| ths.llys | leticiagly, annanadroz, ysadox | 3 |
| ysadox | eusolz, ths.llys | 2 |
| eusolz | thalyana, annanadroz, ysadox | 3 |
| thalyana | lauraaz, maria_anq, eusolz | 3 |
| lauraaz | fernandagil, thalyana | 2 |
| maria_anq | fernandagil, thalyana, annanadroz | 3 |
| annanadroz | maria_anq, isa.linhares, eusolz, ths.llys | 4 |
| isa.linhares | Saara.lima, leticiagly, annanadroz | 3 |

O **grau** de um vértice indica quantas conexões diretas ele possui.

## Indicadores do grafo

| Indicador | Valor |
|---|---:|
| Total de vértices | 12 |
| Total de arestas | 17 |
| Tipo de grafo | Não direcionado |
| Densidade | 0,2576 (25,76%) |
| Maior grau | 4 |
| Vértice de maior grau | annanadroz |

## Cálculo da densidade

Para um grafo simples não direcionado, a densidade representa a proporção de arestas existentes em relação ao máximo de arestas possíveis.

**Fórmula:**

D = (2 × E) / [V × (V − 1)]

Em que:

- **D** = densidade do grafo;
- **E** = número de arestas (17);
- **V** = número de vértices (12).

**Aplicando os valores:**

D = (2 × 17) / [12 × (12 − 1)]

D = 34 / 132 ≈ 0,2576

**Densidade final: 25,76%.**

Isso significa que aproximadamente **25,76% das conexões possíveis** entre as 12 pessoas estão presentes na rede.

## Perguntas e análise da rede

### 1. Quem é mais conectado? Isso significa que é o mais influente?

O participante **annanadroz** é o mais conectado, com **4 ligações diretas**. Todos os demais possuem 2 ou 3 conexões.

Entretanto, **ter mais conexões não significa necessariamente ser o mais influente**. O grau mede a quantidade de ligações, mas não a importância ou a intensidade dessas relações. Uma pessoa com menos contatos pode ser importante por conectar grupos diferentes ou facilitar a circulação de informações. Para investigar influência, seria necessário observar outras métricas, como centralidade de intermediação e proximidade, além de dados sobre as interações reais.

### 2. Como sugerir amizade usando amigos em comum?

Uma forma simples é recomendar a conexão entre **duas pessoas que ainda não estão ligadas diretamente**, mas possuem **vizinhos (amigos) em comum**. Quanto maior o número de contatos compartilhados, maior pode ser a prioridade da recomendação. Isso é uma hipótese de afinidade, não uma garantia de amizade.

**Exemplos no grafo:**

- **maria_anq e eusolz** não estão conectados diretamente, mas compartilham **thalyana** e **annanadroz**: são **2 amigos em comum**.
- **ths.llys e isa.linhares** não estão conectados diretamente, mas compartilham **leticiagly** e **annanadroz**: também são **2 amigos em comum**.

Uma recomendação pode considerar ainda interesses em comum, permissão dos usuários e a opção de recusar ou ocultar sugestões.

### 3. Que cuidados de privacidade são necessários?

Uma rede de conexões pode revelar informações sobre relações pessoais. Por isso, é importante:

- **Obter consentimento ou outra base legal adequada** para coletar e usar os dados, conforme o contexto e a legislação aplicável.
- **Coletar apenas os dados necessários** para a finalidade da análise.
- **Limitar o acesso** aos dados e proteger os registros contra divulgação não autorizada.
- **Evitar expor a lista de contatos** ou revelar amigos em comum sem considerar as configurações de privacidade de todos os envolvidos.
- **Usar dados fictícios, agregados ou pseudonimizados** quando possível em trabalhos e apresentações; pseudônimos não garantem anonimato.
- **Permitir o gerenciamento da visibilidade e das recomendações**, quando aplicável, e definir prazos de retenção e descarte.

No Brasil, o tratamento de dados pessoais deve observar a **Lei Geral de Proteção de Dados (LGPD)**, quando aplicável.

### 4. Quais outras métricas podem descrever uma rede?

| Métrica | O que descreve |
|---|---|
| **Grau** | Quantidade de conexões diretas de cada pessoa. |
| **Centralidade de proximidade** | Quão perto um nó está dos demais considerando as distâncias na rede. |
| **Coeficiente de agrupamento** | Quanto os vizinhos de uma pessoa também estão conectados entre si. |
| **Centralidade de intermediação** | 	Frequência com que um nó aparece nos caminhos mínimos entre outros nós; ajuda a identificar pontes na rede. |
| **Diâmetro** | Maior distância mínima entre pares de nós, em um grafo conectado. |
| **Densidade** | Proporção de conexões existentes em relação às possíveis. |

Essas medidas ajudam a entender não apenas **quantas conexões existem**, mas também a **estrutura da rede**, os caminhos de comunicação e a formação de grupos. Não é possível concluir influência social real apenas a partir do desenho das conexões.

## Conclusão

A rede possui **12 participantes** e **17 conexões**. O participante **annanadroz** apresenta o maior número de ligações diretas (**4**). A densidade de **25,76%** indica que cerca de um quarto das conexões possíveis está presente.


