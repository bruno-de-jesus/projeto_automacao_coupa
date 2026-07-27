# Documentação do Projeto: Automação Coupa ERP

> **Status do Projeto:** Fase de Inception / Planejamento Arquitetural (Sprint 0)  
> **Próxima Milestone:** Execução da Sprint 1 (Infraestrutura Base e Camadas)  
> **Última Atualização:** Julho de 2026  

---

## 1. Visão Geral do Produto e Objetivos de Negócio

### 1.1 O Problema
A criação manual de Requisições de Compra (*Purchase Requests* - PR) no ERP Coupa consome tempo excessivo da equipe operacional e possui alta suscetibilidade a erros humanos de digitação e classificação fiscal. Isso atrasa o fluxo subsequente de geração de Pedidos de Compra (*Purchase Orders* - PO) e afeta a precisão dos dados do ERP.

### 1.2 Público-Alvo
Planejadores de manutenção, analistas de suprimentos e demais colaboradores com perfil operacional de compras que utilizam o ERP Coupa.

### 1.3 Objetivos Estratégicos
- **Eficiência Operacional:** Eliminar o trabalho repetitivo e braçal de navegação manual e preenchimento de formulários extensos no Coupa.
- **Foco Analítico:** Liberar a equipe para atividades de planejamento estratégico e análise de suprimentos.
- **Conformidade e Integridade:** Garantir que todas as PRs geradas respeitem regras fiscais (NCM) e de governança (alçadas de aprovação e validação de logins).

---

## 2. Visão Técnica e Decisões Arquiteturais

### 2.1 Stack Tecnológica Definitiva
- **Linguagem Principal:** Python 3.x
- **Frontend / Interface Gráfica:** PySide6 (Qt para Python) — escolhido pela escalabilidade, componentes corporativos e excelente suporte ao empacotamento.
- **Automação Web:** Selenium WebDriver
- **Modelagem de Dados:** Dataclasses nativas do Python
- **Distribuição / Empacotamento:** PyInstaller (`.exe` standalone para Windows)

### 2.2 Padrão Arquitetural Alvo
A aplicação adotará a **Layered Architecture (Arquitetura em Camadas)** combinada ao **Page Object Model (POM)** para o módulo de automação.

#### Fluxo de Execução entre Camadas:
```text
[ Frontend (PySide6) ]
          │ (Captura inputs e dispara comandos)
          ▼
[ Automations / Workflows ]
          │ (Coordena casos de uso completos)
          ▼
[ Services ]
          │ (Aplica regras de negócio, validações e converte Models)
          ▼
[ Pages (POM) ]
          │ (Centraliza seletores e interações de tela)
          ▼
[ BasePage ]
          │ (Abstrai chamadas genéricas do Selenium)
          ▼
[ Selenium / Driver ] -> ERP Coupa
```

### 2.3 Estrutura de Diretórios Proposta

```text
projeto_automacao_coupa/
│
├── frontend/                   # Interface do Usuário (PySide6)
│   ├── views/                  # Telas e Janelas (Main, Formulários)
│   ├── components/             # Componentes reutilizáveis (Botões, Inputs, Modal)
│   └── main_window.py          # Janela principal
│
├── backend/                    # Core da Aplicação
│   ├── models/                 # Representação de dados puras (Dataclasses)
│   ├── pages/                  # Mapeamento do Coupa (POM)
│   ├── services/               # Validações e Regras de Negócio
│   ├── automations/            # Orquestração dos fluxos e casos de uso
│   └── base/                   # WebDriver Manager e BasePage
│
├── resources/                  # Ícones, estilos QSS, assets estáticos
│
├── .env                        # Configurações de ambiente
├── main.py                     # Entry point da aplicação
└── app.spec                    # Configuração de empacotamento PyInstaller
```

---

## 3. Domínio e Modelagem de Dados

### 3.1 Entidade Principal (`Pedido`)
Representa a requisição a ser processada pela automação.

Os **Models** possuem responsabilidade exclusiva de armazenar e estruturar os dados do negócio. **É expressamente proibido inserir XPath, CSS Selectors, métodos do Selenium ou lógica da GUI dentro das classes do diretório `models/`.**

```text
Pedido
├── InformacoesGerais (Justificativa, Requisitante, etc.)
├── Custo (CustoCentro | CustoAPP)
└── Lista de Items [ItemMaterial | ItemServico]
```

---

## 4. Regras de Negócio Globais e Travas de Segurança

### 4.1 Validações de Pré-Execução (Travas de Pré-requisito)
O sistema deve executar validações preventivas antes de interagir com o navegador. Caso alguma falhe, a automação é abortada imediatamente com notificação visual ao usuário:
1. **Conexão com a Internet:** Confirmar conectividade ativa da máquina.
2. **Disponibilidade do Coupa:** Validar se a URL do ERP está respondendo (HTTP 200/302).
3. **Credenciais e Acessos:** Confirmar que o usuário executor possui permissões ativas.

### 4.2 Regras de Negócio Específicas
- **Conformidade Fiscal (NCM):** Todo item do tipo `Material` **deve obrigatoriamente** possuir NCM cadastrado e válido no ERP. Caso contrário, a inclusão é bloqueada.
- **Validação de Usuários (Solicitante / Observadores):** Os logins informados no formulário devem ser pré-validados para confirmar que estão ativos no cadastro do Coupa antes da submissão.
- **Alçada de Aprovação Financeira (US$ 5.000):** Quando o valor total do pedido exceder **US$ 5.000,00**, o sistema deve exibir um aviso explicativo informando que o prazo de aprovação sistêmica poderá ser estendido devido à alçada, exigindo confirmação explícita do usuário para prosseguir.

---

## 5. Mapeamento do Product Backlog & Sprints

### Épico 01: Infraestrutura Base & Reestruturação Arquitetural
- **HU01 - Validações de Ambiente e Conexão:**
  - *Critérios:* Validar internet, disponibilidade do Coupa e credenciais do executor antes de iniciar o browser.
- **Reestruturação Arquitetural em Camadas:**
  - *Critérios:* Criar diretórios (`frontend`, `backend/models`, `pages`, `services`, `automations`, `base`).
- **Base Selenium & Driver Manager:**
  - *Critérios:* Criar `BasePage` com métodos seguros de clique/waits e centralizar inicialização do WebDriver.

### Épico 02: Interface Desktop (PySide6)
- **HU02 - Interface de Entrada de Dados (GUI):**
  - *Critérios:* Formulários para preenchimento de Usuários (Solicitante/Observador), Informações Gerais, Tabela de Itens e Centro de Custo.
- **Mapeamento GUI x Models:**
  - *Critérios:* Converter entradas de tela em instâncias válidas das Dataclasses do `Pedido`.

### Épico 03: Automação de Fluxos Coupa (POM)
- **HU03 - Módulo de Informações Gerais:** Preenchimento do cabeçalho da PR no Coupa.
- **HU04 - Módulo de Itens e Faturamento:**
  - Inserção de materiais e serviços na grade do Coupa.
  - *Critérios:* Aplicar trava do NCM e modal de alerta para valores acima de $5.000.
- **HU05 - Módulo de Observadores e Finalização:**
  - Preenchimento do Solicitante e Observadores validados.
  - Emissão de feedback de sucesso e captura do número da PR gerada.

### Épico 04: Empacotamento e Entrega
- **Preparação para PyInstaller:**
  - Configuração do `app.spec` e suporte a carregamento de recursos via `sys._MEIPASS`.

---

## 6. Acordos de Qualidade (Definition of Done - DoD)

O projeto ou qualquer estória de usuário individual só será considerada **Pronta (Done)** quando atender aos critérios:
1. Código aderente às camadas definidas (Models limpos sem Selenium, Seletores restritos a Pages).
2. Validações prévias e regras fiscais executadas sem exceções não tratadas.
3. Execução bem-sucedida do fluxo completo com geração de uma PR de teste no **ambiente de homologação do Coupa**.