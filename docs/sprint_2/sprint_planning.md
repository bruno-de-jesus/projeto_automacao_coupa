# PLANEJAMENTO DE SPRINT — SPRINT 2

> **Épicos:** Épico 02 — Interface Desktop (PySide6) & Épico 03 — Automação Coupa (POM)
> **Status:** Em Andamento
> **Objetivo da Sprint:** Implementar a camada de Domain Models (Dataclasses), criar a janela principal em PySide6 com formulários completos (Usuários, Informações Gerais, Itens e Custo) e console de log em tempo real com suporte a Multithreading (Worker Thread / Cancelamento), e construir a `HeaderPage` para o Coupa.

---

## 1. Escopo & Histórias de Usuário / Tasks

### 1.1 Camada de Domain Models (Task Técnica) — [CONCLUÍDO]
- **Descrição:** Criar as Dataclasses puras em `backend/models/` para estruturar os dados do pedido sem acoplamento com Selenium ou GUI.
- **Histórico de Atualizações:**
  - Ajuste na hierarquia de herança da classe base `Custo` (`CustoAPP` e `CustoCentro`).
  - Correção de sintaxe em `typing.List[Item]` dentro de `Pedido`.
  - Refatoração dos caminhos de importação para o padrão em camadas do projeto (`backend/models/...`).
  - Adição de valores padrão e importação correta de `date` em `ItemServico`.
- **Entregáveis Finalizados:**
  - `backend/models/tipo_pedido.py`: Enum `TipoPedido`.
  - `backend/models/custo.py`: Dataclasses `Custo`, `CustoAPP` e `CustoCentro`.
  - `backend/models/item.py`: Dataclasses `Item`, `ItemMaterial` e `ItemServico`.
  - `backend/models/informacoes_gerais.py`: Dataclass `InformacoesGerais` com validações.
  - `backend/models/pedido.py`: Dataclass agregadora `Pedido`.

---

### 1.2 HU02 — Interface de Entrada de Dados (GUI) & Infraestrutura Assíncrona — [EM ANDAMENTO]
- **Como** planejador,  
- **Quero** uma interface gráfica intuitiva, responsiva e não-bloqueante,  
- **Para que** eu possa preencher todos os dados da PR em uma única tela, acompanhar a execução em tempo real e cancelar o processo se necessário.

#### Critérios de Aceite & Evoluções Aplicadas:
- [x] **Infraestrutura Multithread (`QThread`):** Implementado `AutomationWorker` em `frontend/automation_worker.py` para isolar tarefas bloqueantes de Selenium/Rede da Main UI Thread.
- [x] **Controle de Cancelamento:** Botão "Cancelar" com tamanho padronizado (160px) adicionado ao lado do botão "Iniciar Automação", com suporte a interrupção graciosa via `stop_process()`.
- [x] **Console de Logs:** Redirecionamento de logs do `logging` nativo via `QSignalingLogHandler` em tempo real para a interface (`LogConsoleWidget`).
- [ ] **Módulo de Usuários:** Campos para inserção/seleção de Solicitante e Observadores.
- [ ] **Módulo de Informações Gerais:** Formulário com Justificativa, Fornecedor e Tipo de Pedido.
- [ ] **Módulo de Alocação de Custo:** Seletor dinâmico para Centro de Custo ou Ordem APP.
- [ ] **Tabela de Itens:** Grade interativa para adição/remoção de Materiais/Serviços (Quantidade, Preço, NCM, etc.).
- [ ] **Disparo e Conversão:** Botão que valida os campos da GUI e gera uma instância válida da Dataclass `Pedido`.

---

### 1.3 Mapeamento POM: HeaderPage (Task Técnica) — [A INICIAR]
- **Descrição:** Mapear a página de Informações Gerais do Coupa herdando de `BasePage`.
- **Entregáveis:**
  - `backend/pages/header_page.py`: Métodos para preencher justificativa, solicitante e selecionar o centro de custo no ERP.

---

## 2. Estrutura de Arquivos Atualizada da Sprint 2

```text
projeto_automacao_coupa/
│
├── frontend/
│   ├── views/
│   ├── components/
│   │   └── log_console.py      # Console de logs Qt em tempo real [CONCLUÍDO]
│   ├── automation_worker.py    # Thread assíncrona QThread com stop_process() [CONCLUÍDO]
│   └── main_window.py          # Janela principal PySide6 [CONCLUÍDO]
│
├── backend/
│   ├── base/
│   │   ├── driver_factory.py
│   │   └── base_page.py
│   ├── models/                 # [CONCLUÍDO]
│   │   ├── tipo_pedido.py
│   │   ├── custo.py
│   │   ├── item.py
│   │   ├── informacoes_gerais.py
│   │   └── pedido.py
│   ├── pages/
│   │   └── header_page.py      # Mapeamento POM das Informações Gerais
│   ├── services/
│   │   └── environment_service.py
│   └── automations/
│
├── resources/
├── .env
├── main.py                     # Entry point da GUI Qt
└── requirements.txt
```

---

## 3. Definition of Done (DoD) da Sprint 2

A Sprint 2 será considerada **concluída** quando:
1. [x] Os dados e classes de domínio estiverem corrigidos, validados e estruturados em Dataclasses puras sem acoplamento.
2. [x] A interface possuir execução assíncrona via `QThread`, garantindo responsividade da janela e opção de cancelamento sem congelamento da tela.
3. [ ] A GUI em PySide6 permitir a inserção de Usuários, Informações Gerais, Alocação de Custo e Tabela de Itens, convertendo-os na Dataclass `Pedido`.
4. [ ] A `HeaderPage` for capaz de navegar e preencher o cabeçalho no ambiente de homologação do Coupa sem erros.