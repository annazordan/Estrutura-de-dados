# Dossiê Técnico: AutorizaGov

> Documento de referência sobre a plataforma **AutorizaGov**, o sistema de controle de acesso do Governo Federal brasileiro, desenvolvido pelo **Serpro**. Este dossiê serve como conteúdo-base para material explicativo destinado a públicos técnicos e não técnicos.
>
> **Fontes:** documentação oficial do Governo Digital, documentação técnica de referência do Serpro (*Conceitos — Autoriza*) e leitura das telas de configuração de features.

---

## 1. Visão Geral

### 1.1 O que é o AutorizaGov

O **AutorizaGov** (também referido tecnicamente como **Autoriza**) é a plataforma de **controle de acesso** (gerenciamento de autorizações) integrada ao **Acesso gov.br**, utilizada por sistemas do Governo Federal. Ele é responsável por definir **o que cada usuário pode fazer** dentro de um sistema público, funcionando como uma camada centralizada de **autorização**.

O modelo identifica o usuário por meio do **CPF** registrado no Acesso gov.br e aplica **perfis** e **permissões** à aplicação de governo integrada (chamada de **aplicação parceira**). Em vez de cada sistema do governo construir sua própria lógica de permissões, ele **delega** essa responsabilidade ao AutorizaGov, que centraliza as regras de quem pode acessar quais funcionalidades, sob quais condições.

Além do controle básico por perfis e permissões, a solução disponibiliza **features** — funcionalidades configuráveis que permitem definir condições adicionais para concessão e utilização de acessos (tempo, vínculo funcional, segurança, organização institucional etc.).

### 1.2 Login gov.br vs. AutorizaGov: Autenticação x Autorização

Esses dois conceitos são frequentemente confundidos, mas respondem a perguntas diferentes:

| Conceito | Pergunta que responde | Plataforma responsável |
|---|---|---|
| **Autenticação** | *"Quem é você?"* | **Login gov.br (Acesso gov.br)** |
| **Autorização** | *"O que você pode fazer?"* | **AutorizaGov** |

- O **Login gov.br** confirma a **identidade** do usuário (CPF, verificação facial, senha, certificado digital etc.). Ele diz "esta pessoa é, de fato, quem afirma ser".
- O **AutorizaGov** entra em ação **depois** da autenticação, definindo, para aquele CPF já identificado, **quais telas, funcionalidades e dados** ele está autorizado a acessar dentro de um sistema específico.

> Em resumo: o gov.br abre a porta da frente do Governo Digital; o AutorizaGov decide quais salas, dentro de cada prédio, aquela pessoa pode entrar.

---

## 2. Dicionário da Plataforma (Modelo RBAC)

O AutorizaGov implementa primariamente um modelo de controle de acesso baseado em papéis/funções, o **RBAC** (*Role-Based Access Control*). Cada aplicação parceira deve estar cadastrada como **Sistema**, possuir ao menos um **Perfil** de acesso e pode possuir **Transações** associadas — cada Transação deve estar vinculada a pelo menos um Perfil.

| Termo | Definição |
|---|---|
| **Sistema** | A aplicação parceira do Governo Federal que **consome** o AutorizaGov para controlar seu acesso (ex: um sistema de gestão de servidores, um portal de benefícios etc.). Cada sistema é cadastrado individualmente na plataforma. |
| **Usuário** | A pessoa física identificada por **CPF** que acessa um sistema. É o "sujeito" a quem as permissões são concedidas. |
| **Perfil (Role)** | Um **conjunto nomeado de permissões** (ex: "Gestor", "Operador", "Analista"). Em vez de conceder permissões uma a uma para cada usuário, o administrador cria perfis e depois vincula usuários a eles. |
| **Transação** | A **menor unidade de permissão** dentro de um sistema — uma permissão funcional associada a um perfil (ex: "Consultar", "Cadastrar", "Aprovar"). As transações são agrupadas dentro de um **Perfil**. |
| **Atribuição** | O **ato de vincular** um Perfil a um Usuário (registro da concessão de um perfil a um usuário). É a "ponte" que efetivamente concede o acesso, podendo carregar regras adicionais (vigência, horário, certificado digital etc.) por meio de campos configuráveis. |
| **Política de Acesso** | A regra que determina **quais perfis e/ou transações** o usuário precisa possuir para acessar um determinado recurso da aplicação. Tecnicamente, é expressa em **PML** (*PERM Modeling Language*) — ver Seção 8. |

> O modelo é predominantemente **RBAC**, mas o AutorizaGov também oferece recursos compatíveis com uma abordagem **ABAC** (*Attribute-Based Access Control*), por meio das **Características de Usuário** — ver Seção 7.

---

## 3. Arquitetura e Fluxo

Do ponto de vista do usuário final, o processo é instantâneo. Por trás da tela, porém, ocorre uma sequência de etapas técnicas bem definida:

1. **Autenticação no gov.br** — o usuário informa CPF e credenciais (senha, biometria, certificado digital) e o Acesso gov.br confirma sua identidade.
2. **Geração de Token OAuth** — após a autenticação bem-sucedida, é emitido um **token OAuth** (um "crachá digital" temporário e criptografado) que identifica o usuário de forma segura para as próximas requisições.
3. **Consumo da API REST do AutorizaGov** — o sistema cliente (aplicação parceira) envia CPF e token para a **API REST** do AutorizaGov, perguntando, em essência: *"o que este CPF pode fazer no meu sistema?"*
4. **Recuperação de perfis e transações** — o AutorizaGov recupera os perfis e transações aplicáveis ao usuário. Se o sistema utiliza **Tag**, pode ser considerado apenas o subconjunto de perfis/políticas associado à Tag informada.
5. **Avaliação da Política de Acesso** — as políticas do sistema (ou da combinação sistema + Tag) são avaliadas; as **features** configuradas (vigência, horário, vínculo, estrutura institucional etc.) podem restringir quais atribuições serão consideradas.
6. **Retorno do JSON com as permissões** — o AutorizaGov devolve um **JSON estruturado**, listando as transações e perfis liberados para aquele usuário naquele momento.
7. **Renderização da tela** — a aplicação parceira interpreta esse JSON e **monta a interface dinamicamente**, exibindo apenas os menus, botões e funcionalidades autorizados.

```
Usuário → Login gov.br → Token OAuth → API REST AutorizaGov → Avaliação da Política de Acesso (PML) → JSON de permissões → Tela renderizada
```

> Essa arquitetura desacoplada permite que **qualquer sistema do governo** implemente controle de acesso sofisticado sem precisar reconstruir essa lógica do zero — basta consumir a API do AutorizaGov, adotando um dos **modelos de integração** descritos na Seção 10.

---

## 4. Atores de Gestão

A administração do AutorizaGov é dividida entre dois grandes perfis de gestão, com responsabilidades bem distintas dentro de cada sistema cliente:

### Gestor de Sistema (Administrador de Sistema)
- Perfil **técnico**, normalmente vinculado à equipe responsável pelo sistema.
- **Cria e configura as regras** de acesso: define os Perfis, as Transações que os compõem e as **features** de política de acesso (certificado digital, vigência, horário etc.).
- Mantém perfis, transações e features; também acessa **relatórios de auditoria** do sistema administrado.
- Desenha, em outras palavras, o "molde" das permissões que existirão no sistema.

### Gestor de Acesso / Gestor Setorial
- Perfil **operacional/administrativo**, tipicamente um servidor da própria instituição.
- **Não cria regras** — apenas **aplica** as regras já existentes, vinculando o **CPF de um usuário a um Perfil** já configurado pelo Gestor de Sistema.
- O **Gestor de Acesso** mantém atribuições de perfis dos usuários finais em geral.
- O **Gestor de Acesso Setorial** atua em escopo mais restrito: mantém atribuições **dentro de um órgão específico**, respeitando o escopo e apenas os perfis autorizados a ele — depende da habilitação da feature *Gestor de Acesso Setorial*.

> A separação de papéis segue o princípio de **segregação de funções**: quem desenha a regra não é necessariamente quem a aplica no caso concreto, o que aumenta a governança e a rastreabilidade do processo. A estrutura completa de perfis administrativos — incluindo os *cadastradores* responsáveis por cada um desses papéis — está detalhada na Seção 9.1.

---

## 5. Catálogo Completo de Features de Configuração

As **features** são configurações específicas de cada sistema: blocos de construção com os quais o Gestor de Sistema monta a política de acesso de cada Perfil ou Atribuição. Tecnicamente, cada feature adiciona **campos** às atribuições de perfis, e essas informações podem ser usadas pela aplicação parceira como **critérios de filtragem** no controle de acesso. Elas se dividem em quatro categorias.

### A. Segurança do sistema

- **Certificado Digital**
  - **Feature:** exige o uso de certificado digital do usuário na atribuição ou no uso do(s) perfil(is) do sistema. Campo técnico: `exigeCertificadoDigital` (booleano).
  - **Regras de atribuição:** pode ser atribuída de forma independente. Quando marcada como **obrigatória**, todos os usuários precisam atender a essa exigência.
  - **Comportamento na avaliação de acesso:**
    - Se o usuário estiver autenticado no Acesso gov.br **com** Certificado Digital, todos os perfis e transações atribuídos ao usuário no sistema podem ser retornados — inclusive os que exigem certificado.
    - Se o usuário estiver autenticado por **outro meio** (ex: usuário e senha), são retornados **apenas** os perfis e transações que **não exigem** Certificado Digital.

- **Validação de Vínculo no eSocial**
  - **Feature:** valida se o usuário possui **vínculo ativo no eSocial** — verificação compatível com a checagem funcional feita via SIAPE.
  - **Observação:** segundo a documentação oficial, o uso dessa validação é **restrito à Receita Federal do Brasil (RFB)**.

- **Validação Por Vínculo Funcional No SIAPE**
  - **Feature:** valida se o usuário possui vínculo funcional compatível com o **SIAPE**.
  - **Regras de atribuição:** exige que um **Órgão SIAPE** esteja selecionado. **Não combina** com as estruturas **SIORG** ou **SIAFI**.

### B. Controle no tempo

- **Dias Da Semana**
  - **Feature:** restringe o acesso aos dias da semana configurados para o sistema. Campo técnico: `diasDaSemana` (texto de sete dígitos, iniciando no domingo; `1` permite e `0` nega).
  - **Regras de atribuição:** pode ser atribuída de forma independente. Quando selecionada, o(s) dia(s) de acesso deve(m) ser informado(s). Pode ser combinada com Horário e Vigência.

- **Horário**
  - **Feature:** restringe o acesso a uma faixa de horário configurada para o sistema. Campos técnicos: `horaInicio` / `horaFim` (formato `HH:MM`).
  - **Regras de atribuição:** pode ser atribuída de forma independente. Quando selecionada, o **horário de início** e o **horário de fim** devem ser informados.

- **Vigência**
  - **Feature:** define o período de validade da atribuição de um perfil. Campos técnicos: `dataInicioVigencia` / `dataFimVigencia` (formato `AAAA/MM/DD`).
  - **Regras de atribuição:** pode ser atribuída de forma independente e pode ser usada como critério de contexto. A **data de início é obrigatória** quando a feature é selecionada. Adequada para substituições, projetos ou autorizações com prazo definido.

- **Exercício Anual**
  - **Feature:** organiza as transações do sistema por **exercício anual**, funcionando como um filtro na listagem de perfis de usuário. As habilitações são encerradas ao final do ano e exigem nova ativação — evitando a permanência indefinida de determinadas autorizações.
  - **Regras de atribuição:** não adiciona campo diretamente ao perfil. Habilita a gestão de exercícios e vínculos de transações por exercício.
  - **Regra de remoção:** ao desmarcar essa feature, os **exercícios anuais existentes são removidos após 1 dia** da exclusão da feature.

### C. Controle por níveis de acesso

- **Gestor De Acesso Setorial**
  - **Feature:** permite a gestão de acessos por instituição (administração descentralizada), concedida ao gestor, que atua dentro de um escopo definido e só pode atribuir perfis permitidos.
  - **Regras de atribuição:** exige uma estrutura institucional selecionada — **SIAPE**, **SIORG**, **SIAFI** ou **CNPJ**. Quando **CNPJ** é selecionado, essa feature também deve estar selecionada.
  - **Regra de remoção:** ao desmarcar essa feature, as **concessões de gestor de acesso setorial existentes são removidas após 1 dia** da data de exclusão da feature.

- **Nível de Acesso**
  - **Feature:** restringe perfis de acordo com a hierarquia estabelecida na configuração do sistema. Campo técnico: `nivelAcesso` (texto). Ajuda a limitar o alcance das autorizações (ex: um gestor de unidade não recebe automaticamente o mesmo escopo de um gestor nacional).

- **UORG e UPAG SIAPE**
  - **Feature:** restringe a atribuição de perfis a uma **UORG** (Unidade Organizacional, campo `cdUorgSiape`) ou **UPAG** (Unidade Pagadora, campo `cdUpagSiape`) da estrutura SIAPE.
  - **Regras de atribuição:** exige **Órgão SIAPE** selecionado. Se marcada como obrigatória, o **Órgão SIAPE** também deve ser obrigatório. Pode compor níveis de acesso.
  - **Obrigatoriedade:** quando marcada como obrigatória, a informação deverá ser preenchida na atribuição dos perfis do usuário. Quando não obrigatória, poderá ser usada apenas quando houver valor informado. Em uma alteração de configuração, essa exigência somente pode ser incluída como opcional.

- **Multiórgão**
  - **Feature:** destinada a perfis agregadores multi-órgão dentro da estrutura SIAPE.
  - **Regras de atribuição:** exige **Nível de Acesso** e estrutura SIAPE selecionados. **Não combina** com SIORG ou SIAFI.

- **Filtros institucionais adicionais:** a plataforma também disponibiliza filtros configuráveis por **Órgão SIAPE** (`cdOrgaoSiape`), **Órgão SIORG** (`cdOrgaoSiorg`), **Unidade SIORG** (`cdUnidadeSiorg`), **Órgão SIAFI**, **Unidade Gestora SIAFI** e **CNPJ** (`cnpj`), cada um podendo ser marcado como campo **Obrigatório** na configuração do perfil. Essas estruturas aproximam a autorização da organização real e podem apoiar administração descentralizada e **Controle Hierárquico** — respeitando a estrutura organizacional na concessão de acesso (uma autorização concedida em uma unidade subordinada não implica automaticamente autorização para toda a organização).

### D. Organização dentro do Autoriza

- **Perfil Agregador**
  - **Feature:** perfil especial que agrupa outros perfis como "filhos", sem precisar manipular individualmente cada atribuição. Durante a autorização, os perfis filhos e suas respectivas transações também são considerados como perfis/transações que o usuário possui.
  - **Regras de atribuição:** não adiciona campo institucional ao perfil.
  - **Regra de remoção:** ao desmarcar essa feature, os **perfis agregadores existentes são removidos após 1 dia** da data de exclusão da feature.

- **Habilitação**
  - **Feature:** controla requisitos de acesso por meio de **contexto**, alterando a regra de atribuição de perfis. **Sem** a feature, um Gestor de Acesso pode atribuir um mesmo perfil a um usuário **apenas uma vez**. **Com** a feature habilitada, o mesmo perfil pode ser atribuído **mais de uma vez**, desde que as atribuições respeitem os critérios de unicidade configurados para o sistema (isso também apoia a *repetição de perfil com critérios distintos* — o mesmo perfil aplicado a escopos ou vigências diferentes).
  - **Regras de atribuição:** torna-se **obrigatória** sempre que houver *features* de contexto configuradas no perfil.

- **Tag**
  - **Feature:** organiza perfis e políticas de acesso para fins de filtro e busca. Quando habilitada, durante a autorização a Tag informada pode fazer com que apenas o subconjunto correspondente de perfis/políticas seja considerado — o que também tem o benefício operacional de **reduzir a quantidade de informação de autorização** trafegada entre a aplicação parceira e o AutorizaGov.
  - **Regra de remoção:** ao desmarcar essa feature, as **tags associadas existentes são removidas após 1 dia** da data de exclusão da feature.

- **Campos Configuráveis**
  - **Feature:** permite criar campos adicionais nas atribuições para compor **regras personalizadas** e específicas da aplicação. Esses campos podem utilizar **validação por expressão regular (regex)**, ampliando a flexibilidade da política de acesso além das features padrão (ex: um campo "Tipo de Unidade" usado como critério adicional de autorização).

---

## 6. Legenda de Ciclo de Vida de Alterações

Ao editar uma configuração de política de acesso, a interface do AutorizaGov sinaliza visualmente o **impacto de cada alteração** antes de sua confirmação, usando cores e ícones padronizados:

| Estado | Indicador visual | Significado |
|---|---|---|
| **Mantida** | 🔵 Azul, com ✔️ | A opção **já estava selecionada** e **permanece ativa** após a alteração. |
| **Adicionada** | 🟢 Verde, com ✔️ | A opção **será incluída** na nova configuração. |
| **Removida** | 🔴 Vermelha, com ❌ | A opção **será retirada** da configuração atual. |
| **Bloqueada** | ⬜ Cinza | A opção **não pode ser alterada**, por regra vigente da configuração atual. |

> As mesmas cores também indicam alterações na coluna **Obrigatório**, sinalizando quando uma exigência está sendo mantida, adicionada, removida ou bloqueada para edição.

---

## 7. Características de Usuário (ABAC)

Além do modelo RBAC principal, o AutorizaGov possui uma modalidade de controle baseada em **atributos (ABAC)**, chamada de **Características de Usuário**. Essas características são mantidas por **outros sistemas** (fontes externas) e consultadas pelo AutorizaGov; a aplicação parceira define quais perfis devem ser atribuídos quando determinada característica estiver presente para o CPF avaliado.

| Característica | Descrição | Sistema de origem indicado |
|---|---|---|
| **Ex-servidor** | Ex-servidor da administração pública da União. | API do Servidor do SIGEPE |
| **Servidor** | Servidor da administração pública da União. | API do Servidor do SIGEPE |
| **Aposentado** | Aposentado da administração pública da União. | API do Servidor do SIGEPE |
| **Pensionista** | Beneficiário de pensão de servidor da administração pública da União. | API do Servidor do SIGEPE |
| **Representante Legal** | Pessoa autorizada a agir em nome de pensionista menor de 18 anos ou incapaz. | API do Servidor do SIGEPE |
| **Representado Legal** | Pensionista menor de 18 anos ou incapaz sob tutela de representante legal. | API do Servidor do SIGEPE |
| **Chefe** | Servidor com cargo de autoridade/chefia em órgão da administração pública da União. | API do Servidor do SIGEPE |
| **Substituto** | Servidor substituto de chefia. | API do Servidor do SIGEPE |
| **Estagiário** | Estagiário em órgão da administração pública da União. | API do Servidor do SIGEPE |

> **Exemplo conceitual:** um sistema pode associar a característica "Ex-servidor" a um perfil como "CLIENTE DADOS FINANCEIROS". Se a fonte externa confirmar que o CPF possui essa característica, o AutorizaGov pode considerar o perfil na decisão de acesso, **mesmo sem uma atribuição direta** daquele perfil.

---

## 8. Política de Acesso e PML

Uma **Política de Acesso** determina quais **perfis** e/ou **transações** o usuário precisa possuir para acessar um determinado recurso da aplicação. Tecnicamente, essas políticas são expressas na **PML** (*PERM Modeling Language*), no formato:

```
nome dos perfis, nome das transações, identificador do recurso, verbo HTTP
```

Os **verbos HTTP** aceitos são `GET`, `POST`, `PUT`, `PATCH`, `DELETE` ou `*` (asterisco, que representa qualquer verbo).

**Exemplo documentado:**

```
AUDITOR|EQUIPE TECNICA,*,/private/protocolo,GET
*,GESTAO PROTOCOLOS,/private/protocolo,POST
*,ATUALIZAR PROTOCOLO,/private/protocolo,PATCH
```

- Na primeira linha, um usuário com o perfil **AUDITOR** ou **EQUIPE TECNICA** pode realizar `GET` no recurso indicado.
- Na segunda, a transação **GESTAO PROTOCOLOS** autoriza `POST`.
- Na terceira, a transação **ATUALIZAR PROTOCOLO** autoriza `PATCH`.

---

## 9. Gestão de Clientes e Perfis Administrativos

O **Ministério da Gestão e da Inovação (MGI)** realiza a gestão de clientes e o processo de integração de novas aplicações: recebe pedidos de adesão, avalia os pedidos, cadastra novos sistemas quando os requisitos são atendidos, cadastra o órgão/cliente, vincula sistemas e concede acesso a administradores representantes.

### 9.1 Estrutura de perfis administrativos

A estrutura de gestão segue um modelo em **pares**, onde cada perfil possui um **cadastrador** responsável por sua manutenção — evitando que a mesma pessoa eleve seus próprios privilégios.

| Perfil | Função | Observação |
|---|---|---|
| **Cadastrador de Cliente** | Cadastra órgão/entidade por CNPJ; vincula sistemas a clientes; consulta o Relatório de Autorizações Consolidado. | Perfil de nível superior da gestão de clientes. |
| **Administrador de Cliente** | Configura o sistema do cliente para concessão de acesso; ajusta as features disponíveis; inclui cadastradores de gestor e de gestor de acesso setorial. | Deve haver **pelo menos dois** por cliente (ver nota abaixo). |
| **Cadastrador de Administrador de Sistema** | Mantém o usuário/equipe de Administradores de Sistema. | Cadastro realizado na funcionalidade "Cadastradores". |
| **Administrador de Sistema** | Mantém perfis, transações e features; acessa relatórios de auditoria do sistema administrado. | Perfil central da administração da aplicação parceira. |
| **Cadastrador de Gestor de Acesso** | Mantém usuários/equipe de Gestores de Acesso. | Cadastro realizado na funcionalidade "Cadastradores". |
| **Gestor de Acesso** | Mantém atribuições de perfis dos usuários finais. | Concede e mantém acessos. |
| **Cadastrador de Gestor de Acesso Setorial** | Mantém usuários/equipe de Gestores de Acesso Setorial. | Cadastro em funcionalidade específica de cadastradores. |
| **Gestor de Acesso Setorial** | Mantém atribuições dentro de um órgão, apenas com perfis/sistemas autorizados ao seu escopo. | Usado em cenários de hierarquia de órgãos. |

> **Nota:** deve existir **pelo menos dois administradores** cadastrados por cliente, pois **não é permitido escalar privilégios para si próprio** — a concessão precisa ocorrer por pares.

### 9.2 Regras de hierarquia

- O administrador pode conceder outros acessos informando o CPF.
- Um usuário pode **acumular perfis**, ampliando as funcionalidades às quais possui acesso.
- Um usuário **não pode conceder acesso a si próprio**.
- Um usuário só concede perfil a um nível da hierarquia com acessos **mais restritos** que o seu.
- O modelo utiliza **cadastradores** responsáveis pelo cadastro de outros usuários.
- Sistemas que trabalham com hierarquia de órgãos podem utilizar **Gestores de Acesso Setorial**.

---

## 10. Modelos de Integração

A aplicação parceira pode adotar um (ou combinar mais de um) dos seguintes modelos de integração com o AutorizaGov:

| Modelo | Descrição |
|---|---|
| **Consumo de informações de autorização** | O AutorizaGov funciona como cadastro centralizado e fonte de dados de autorização; a aplicação parceira aplica as políticas de acesso por conta própria. |
| **Integração com Provider** | O AutorizaGov fornece uma biblioteca/**Provider** (ou *Adapter*) que apoia a aplicação das políticas no lado do sistema cliente. |
| **Aplicação remota das políticas de acesso** | O AutorizaGov realiza remotamente a aplicação das políticas, incluindo o contexto de auditoria das autorizações. |

---

## 11. Auditoria e Relatórios

- **Relatórios de auditoria** associados à gestão do sistema, acessíveis pelo Administrador de Sistema.
- **Relatório de Autorizações Consolidado**, utilizado para acompanhar a volumetria de autorizações por cliente e sistema em determinado período — consultável pelo Cadastrador de Cliente.
- Acompanhamento de quantidade de autorizações por cliente e sistema.
- Menu de Auditoria como área de consulta.

---

## 12. Glossário Técnico

| Termo | Significado |
|---|---|
| **Acesso gov.br** | Mecanismo de autenticação utilizado como base de identificação do usuário. |
| **AutorizaGov / Autoriza** | Solução de controle de acesso e autorização para aplicações integradas ao ecossistema gov.br. |
| **RBAC** | *Role Based Access Control* — controle de acesso baseado em papéis/funções. |
| **ABAC** | *Attribute-Based Access Control* — controle de acesso baseado em atributos do usuário e/ou ambiente. |
| **PML** | *PERM Modeling Language* — linguagem usada para expressar políticas de controle de acesso. |
| **JWT** | *JSON Web Tokens* — formato baseado em JSON para troca de informações. |
| **XACML** | Padrão de linguagem, arquitetura e modelo de processamento para controle de acesso. |
| **Provider / Adapter** | Biblioteca do AutorizaGov embarcada na aplicação parceira para realização da autorização. |
| **Aplicação Parceira** | Sistema que utiliza o AutorizaGov para controle de acesso. |
| **Escopo** | Limite organizacional, temporal ou funcional dentro do qual uma autorização é válida. |
| **Cadastrador** | Perfil responsável por criar e manter determinado grupo de administradores/gestores. |
| **Regex** | Expressão regular usada para validar valores de campos configuráveis. |

---

## 13. Fontes Consultadas

- **Governo Digital — Funcionalidades do AutorizaGov:** `gov.br/governodigital` — plataformas-e-servicos-digitais/autorizagov/funcionalidades-do-autorizagov
- **Governo Digital — Gestão de acesso:** subseção de gestão de acesso do AutorizaGov
- **Governo Digital — Gestão do cliente:** subseção de gestão do cliente do AutorizaGov
- **Governo Digital — Autenticação gov.br:** estratégias e governança digital, ferramentas de autenticação
- **Autoriza — Referência técnica (Serpro):** `docs.autorizagov.estaleiro.serpro.gov.br/conceitos/`
- **Autoriza — Modelos de Integração (Serpro):** `docs.autorizagov.estaleiro.serpro.gov.br/modelosintegracao/`
- Leitura das telas de configuração de features fornecidas no levantamento.

> As descrições devem ser revisadas sempre que a interface ou a documentação oficial do AutorizaGov sofrer alterações.

---

*Documento de referência técnica sobre o AutorizaGov (Serpro) — uso como conteúdo-base para material explicativo.*
