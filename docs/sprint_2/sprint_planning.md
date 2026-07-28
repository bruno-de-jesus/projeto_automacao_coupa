# PLANEJAMENTO DE SPRINT — SPRINT 2

> **Épicos:** Épico 02 — Interface Desktop (PySide6) & Épico 03 — Automação Coupa (POM)
> **Status:** Em Andamento
> **Objetivo da Sprint:** Implementar a camada de Domain Models (Dataclasses), criar a janela principal em PySide6 com formulários completos (Usuários, Informações Gerais, Itens e Custo) e console de log, e construir a `HeaderPage` para o Coupa.

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

### 1.2 HU02 — Interface de Entrada de Dados (GUI) — [EM ANDAMENTO]
- **Como** planejador,  
- **Quero** uma interface gráfica intuitiva e centralizada,  
- **Para que** eu possa preencher todos os dados da PR em uma única tela e acompanhar a execução da automação em tempo real.

#### Critérios de Aceite (Ajustados):
- [ ] **Módulo de Usuários:** Campos para inserção/seleção de Solicitante e Observadores.
- [ ] **Módulo de Informações Gerais:** Formulário com Justificativa, Fornecedor e Tipo de Pedido.
- [ ] **Módulo de Alocação de Custo:** Seletor dinâmico para Centro de Custo ou Ordem APP.
- [ ] **Tabela de Itens:** Grade interativa para adição/remoção de Materiais/Serviços (Quantidade, Preço, NCM, etc.).
- [ ] **Console de Logs:** Área de exibição de status e logs em tempo real na interface.
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
│   ├── components/             # FormAtributos, TabelaItens, ConsoleLog
│   └── main_window.py          # Janela principal PySide6
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
├── main.py
└── requirements.txt
```

---

## 3. Definition of Done (DoD) da Sprint 2

A Sprint 2 será considerada **concluída** quando:
1. [x] Os dados e classes de domínio estiverem corrigidos, validados e estruturados em Dataclasses puras sem acoplamento.
2. [ ] A GUI em PySide6 permitir a inserção de Usuários, Informações Gerais, Alocação de Custo e Tabela de Itens, convertendo-os na Dataclass `Pedido`.
3. [ ] A `HeaderPage` for capaz de navegar e preencher o cabeçalho no ambiente de homologação do Coupa sem erros.
4. [ ] Os logs da execução forem exibidos em tempo real no console visual da GUI.