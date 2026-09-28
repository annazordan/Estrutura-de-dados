# Atividade de Revisão: Estrutura de Árvores

**Disciplina:** Estrutura de Dados II

**Professora:** Profa. Kadidja Valéria\
**Nome:** Anna Clara Nasciemento Zordan

**Modalidade:** Individual, remota e assíncrona

## Etapa 1 — Revisão Bibliográfica

* **Conceitos Básicos:** Uma árvore é uma estrutura de dados não linear hierárquica. O ponto de entrada é a **raiz**. Cada elemento é um **nó**, que possui ponteiros/referências para seus **filhos** e é apontado por um nó **pai**. Nós sem filhos são chamados de **folhas**. A **altura** corresponde ao caminho mais longo da raiz até uma folha, e os **percursos** (em-ordem, pré-ordem, pós-ordem e em largura) determinam a sequência de visitação dos nós.

* **Árvore Geral:** Organiza nós sem limite fixo de filhos por pai. Não impõe restrições estritas de ordenação. Utilizada em estruturas hierárquicas arbitrárias como sistemas de arquivos e documentos XML/HTML.

* **Árvore Binária:** Cada nó possui no máximo dois filhos (esquerdo e direito). Não garante ordenação lógica dos elementos, servindo de base para estruturas mais complexas.

* **Árvore Binária de Busca (ABB):** Mantém a propriedade de ordenação: para qualquer nó, valores menores ficam na subárvore esquerda e maiores na subárvore direita. Permite busca rápida, porém pode degenerar para complexidade linear se inserida de forma desbalanceada.

* **Árvore AVL:** Árvore binária de busca auto-balanceada rigorosa. Mantém o fator de balanceamento (diferença entre as alturas das subárvores)  Realiza **rotações** (simples ou duplas) após inserções ou remoções para garantir busca em tempo logarítmico 

* **Árvore Rubro-Negra (Red-Black):** Árvore binária de busca auto-balanceada que utiliza cores (vermelho ou preto) nos nós. Garante que nenhum caminho seja mais do que o dobro do comprimento de qualquer outro caminho, realizando **recolorações e rotações** mais leves que a AVL.

* **Árvore B:** Árvore de busca balanceada multidirecional em que cada nó pode conter múltiplos elementos/chaves e múltiplos filhos. Otimizada para leitura e escrita em sistemas de armazenamento secundário (discos e bancos de dados).

* **Árvore B+:** Variação da Árvore B onde todos os dados/registros ficam exclusivamente nas **folhas**, e as folhas são conectadas por uma **lista encadeada**. Os nós internos armazenam apenas chaves para direcionamento de busca, facilitando varreduras sequenciais e consultas por intervalo.

## Etapa 2 — Quadro Comparativo

| Estrutura | Organização dos dados | Regra ou propriedade | Operação ou ajuste | Aplicação | Referência | 
 | ----- | ----- | ----- | ----- | ----- | ----- | 
| **ABB** | Hierárquica binária | Esquerda < Nó < Direita | Inserção/Busca direcionada por comparação | Dicionários simples, tabelas de símbolos | CORMEN et al. (2012) | 
| **AVL** | Hierárquica binária auto-balanceada | Fator de balanceamento $\in \{-1, 0, 1\}$ | Rotações simples e duplas após alterações | Sistemas com foco alto em leitura/busca rápida | CORMEN et al. (2012) | 
| **Rubro-Negra** | Hierárquica binária balanceada com cores | Raiz preta; filhos de nó vermelho são pretos; mesmo número de nós pretos até folha | Recoloração e rotações | `std::map` (C++), `TreeMap` (Java), escalonador do Linux | SEDGEWICK & WAYNE (2011) | 
|  | 
| **B** | Multidirecional balanceada em blocos | Nós possuem entre $\lceil m/2 \rceil$ e $m$ filhos; todas as folhas no mesmo nível | Divisão (*split*) e fusão (*merge*) de nós | Sistemas de arquivos (ex: NTFS, EXT4), bancos de dados | ELMASRI & NAVATHE (2011) | 
| **B+** | Multidirecional; dados nas folhas e chaves nos nós internos | Dados apenas nas folhas; folhas interligadas sequencialmente | Divisão de nó com duplicação da chave para o nível superior | Índices primários/secundários em SGDBs (MySQL/InnoDB, PostgreSQL) | ELMASRI & NAVATHE (2011) | 

## Etapa 3 — Identificação por Analogias

1. **Uma estante de números é reorganizada por rotações quando um lado fica alto demais em relação ao outro.**

   * **Estrutura:** Árvore AVL.

   * **Limite da Analogia:** Uma estante real reposiciona livros fisicamente no mesmo plano, enquanto na AVL o ajuste reorganiza a hierarquia de nós via ponteiros sem mover dados na memória física.

2. **Um catálogo guarda várias chaves por página; quando uma página fica cheia, ela é dividida.**

   * **Estrutura:** Árvore B.

   * **Limite da Analogia:** Páginas de papel são estáticas e exigem reescrita manual ou inserção física de folhas, ao passo que a Árvore B ajusta dinamicamente ponteiros de memória/disco mantendo todas as folhas no mesmo nível.

3. **Uma fila mantém a tarefa de maior prioridade no topo para retirá-la primeiro.**

   * **Estrutura:** Heap (especificamente Max-Heap).

   * **Limite da Analogia:** Em uma fila do mundo real, as pessoas andam fisicamente um passo à frente; no Heap, o topo é removido e o último elemento é promovido para a raiz, sendo reajustado via *sift-down*.

4. **Um índice percorre letras sucessivas e compartilha o início das palavras de mesmo prefixo.**

   * **Estrutura:** Trie (Árvore de Prefixos).

   * **Limite da Analogia:** Um índice impresso repete palavras completas, enquanto a Trie economiza memória ao compartilhar fisicamente os prefixos idênticos na mesma subárvore.

5. **Uma estrutura usa cores, recolorações e rotações para manter controlada a altura dos caminhos de busca.**

   * **Estrutura:** Árvore Rubro-Negra (Red-Black Tree).

   * **Limite da Analogia:** Cores no mundo real costumam ter fins apenas estéticos ou de marcação externa, enquanto na árvore a cor é um bit de controle que determina a lógica e a necessidade de rebalanceamento.

6. **Um índice conduz às folhas que contêm os registros, ligadas entre si para facilitar consultas por intervalo.**

   * **Estrutura:** Árvore B+.

   * **Limite da Analogia:** Livros físicos possuem índices remissivos genéricos que exigem ir e voltar nas páginas, enquanto a Árvore B+ permite navegar direto pelas folhas em sequência sem retornar aos nós superiores.

7. **Numa coleção de números, cada nó direciona valores menores para a esquerda e maiores para a direita.**

   * **Estrutura:** Árvore Binária de Busca (ABB).

   * **Limite da Analogia:** Uma coleção física (como caixas numeradas) exige busca exaustiva ou espaço fixo, enquanto na ABB a organização é dinâmica e baseada unicamente nas relações dos nós.

## Referências Bibliográficas

* CORMEN, Thomas H. et al. **Algoritmos: teoria e prática**. 3. ed. Rio de Janeiro: Elsevier, 2012.

* ELMASRI, Ramez; NAVATHE, Shamkant B. **Sistemas de Banco de Dados**. 6. ed. São Paulo: Pearson, 2011.

* SEDGEWICK, Robert; WAYNE, Kevin. **Algorithms**. 4th ed. Upper Saddle River: Addison-Wesley, 2011.