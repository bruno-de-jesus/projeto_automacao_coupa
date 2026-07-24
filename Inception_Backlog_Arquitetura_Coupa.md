# Documentação Inicial — Evolução Arquitetural do Projeto Automação Coupa

> Documento derivado exclusivamente das definições realizadas até o momento.
> Não foram adicionados requisitos funcionais não discutidos.

---

# Objetivo da Evolução Técnica

Evoluir a aplicação atual de automação Coupa para uma arquitetura baseada em:

```text
Layered Architecture
+
Page Object Model (POM)
+
PySide6 (Frontend Desktop)
+
PyInstaller (Distribuição)
```

Objetivos esperados:

- Melhor separação de responsabilidades
- Redução de acoplamento
- Reutilização de código
- Facilidade de manutenção
- Evolução futura da interface gráfica
- Padronização da automação Selenium
- Melhor suporte ao empacotamento via PyInstaller

---

# Arquitetura Alvo

## Fluxo Geral

```text
Frontend (PySide6)
        ↓
Automations
        ↓
Services
        ↓
Pages (POM)
        ↓
BasePage
        ↓
Selenium
```

---

# Estrutura Alvo

```text
projeto_automacao_coupa/
│
├── frontend/
│   ├── views/
│   ├── components/
│   └── main_window.py
│
├── backend/
│   ├── pages/
│   ├── services/
│   ├── automations/
│   ├── models/
│   └── base/
│
├── resources/
│
├── .env
├── main.py
└── app.spec
```

---

# Domínio Atual Identificado

## Entidade Principal

```python
Pedido
```

Composta por:

```text
InformacoesGerais
CustoCentro ou CustoAPP
Lista de Itens
```

---

## Models Existentes

```text
Pedido
InformacoesGerais
Item
ItemMaterial
ItemServico
Custo
CustoCentro
CustoAPP
TipoPedido
```

---

# Decisão Arquitetural

Os Models atuais permanecerão responsáveis exclusivamente por representar dados do domínio.

Não devem conter:

```text
Selenium
XPath
CSS Selector
find_element
click
send_keys
Interface gráfica
```

Responsabilidade dos Models:

```text
Representação dos dados do negócio.
```

---

# Padrão POM Definido

## Pages

Responsáveis por:

```text
Mapeamento de elementos
Seletores
Preenchimentos
Cliques
Leitura de informações de tela
Navegação entre páginas
```

Exemplos previstos:

```text
LoginPage
HomePage
PedidoPage
AprovacaoPage
```

---

## Services

Responsáveis por:

```text
Orquestração do processo
Regras de negócio
Validações
Integração entre Models e Pages
```

Não devem conter:

```text
XPath
find_element
Seletores
```

---

## Automations

Responsáveis por:

```text
Fluxos completos de execução
Casos de uso da automação
Sequenciamento de Services
```

---

## BasePage

Responsável por:

```text
Métodos reutilizáveis
Waits
Cliques
Preenchimentos
Interações genéricas Selenium
```

---

# Frontend Definido

## Biblioteca Escolhida

```text
PySide6
```

Motivadores:

```text
Compatibilidade com PyInstaller
Escalabilidade
Componentes corporativos
Suporte a múltiplas telas
Suporte a tabelas complexas
Organização por Views
```

---

# Itens para Inception

## Visão Técnica

### Tema

```text
Modernização da arquitetura da automação Coupa.
```

### Objetivo

```text
Transformar a automação atual em uma aplicação desktop estruturada, utilizando PySide6 no frontend e arquitetura Layered + POM no backend.
```

---

## Decisões Técnicas

### Arquitetura

```text
Layered Architecture
Page Object Model (POM)
```

### Frontend

```text
PySide6
```

### Automação

```text
Selenium
```

### Empacotamento

```text
PyInstaller
```

### Modelagem

```text
Dataclasses
```

---

# Product Backlog Inicial

## Epic 01 — Reestruturação Arquitetural

### Item

```text
Criar estrutura backend baseada em camadas.
```

### Critério

```text
Pastas base, pages, services, automations e models criadas.
```

---

### Item

```text
Migrar automação atual baseada em Steps para POM.
```

### Critério

```text
Seletores removidos da camada de fluxo e centralizados em Pages.
```

---

## Epic 02 — Base Selenium

### Item

```text
Criar BasePage compartilhada.
```

### Critério

```text
Métodos genéricos de clique, preenchimento e busca implementados.
```

---

### Item

```text
Padronizar gerenciamento do WebDriver.
```

### Critério

```text
Inicialização centralizada do navegador.
```

---

## Epic 03 — Frontend Desktop

### Item

```text
Criar estrutura inicial PySide6.
```

### Critério

```text
Janela principal funcionando.
```

---

### Item

```text
Criar navegação entre telas.
```

### Critério

```text
Frontend preparado para expansão futura.
```

---

## Epic 04 — Integração Frontend x Backend

### Item

```text
Permitir execução da automação pela interface.
```

### Critério

```text
Frontend dispara fluxo da automação.
```

---

### Item

```text
Mapear dados do formulário para o model Pedido.
```

### Critério

```text
Instância de Pedido criada a partir dos dados informados pelo usuário.
```

---

## Epic 05 — Empacotamento

### Item

```text
Preparar projeto para PyInstaller.
```

### Critério

```text
Estrutura compatível com app.spec.
```

---

### Item

```text
Implementar carregamento de recursos utilizando sys._MEIPASS.
```

### Critério

```text
Aplicação executa corretamente empacotada.
```

---

# Informações Pendentes

Os seguintes tópicos ainda não foram discutidos e deverão ser complementados posteriormente:

```text
Requisitos funcionais da interface
Fluxos completos do Coupa
Telas necessárias
Perfis de usuário
Tratamento de erros
Persistência de dados
Logs
Configuração de ambiente
Estratégia de testes
Pipeline de build
```
