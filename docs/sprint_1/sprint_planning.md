# PLANEJAMENTO DE SPRINT — SPRINT 1

> **Épico:** Épico 01 — Infraestrutura Base & Reestruturação Arquitetural  
> **Status:** Em Andamento (Kick-off)  
> **Objetivo da Sprint:** Construir a estrutura de diretórios em camadas, implementar a infraestrutura base do Selenium/WebDriver e entregar o módulo de validações de pré-execução de ambiente (HU01).

---

## 1. Escopo & Histórias de Usuário / Tasks

### 1.1 Reestruturação Arquitetural em Camadas (Task Técnica)
- **Descrição:** Criar a estrutura física do repositório garantindo a separação entre Frontend (PySide6) e Backend (Models, Pages, Services, Automations, Base).
- **Entregáveis:**
  - Árvore de diretórios completa (`frontend/`, `backend/`, `resources/`).
  - Arquivos base e de configuração (`main.py`, `.env`, `requirements.txt`).

---

### 1.2 HU01 — Validações de Ambiente e Conexão (História de Usuário)
- **Como** sistema de automação,  
- **Quero** validar a conectividade com a internet, a disponibilidade do ERP Coupa e as credenciais do usuário antes de inicializar o navegador,  
- **Para que** a automação não falhe no meio do processo ou trave por indisponibilidade técnica.

#### Critérios de Aceite:
- [ ] Validar conexão ativa com a internet (`check_internet_connection`).
- [ ] Validar se o endpoint do Coupa está acessível e respondendo com status HTTP válido (200/302).
- [ ] Validar presença de credenciais/dados mínimos necessários de execução.
- [ ] Bloquear o disparo do WebDriver e emitir log/notificação clara de erro caso qualquer pré-requisito falhe.

---

### 1.3 Base Selenium & Driver Manager (Task Técnica)
- **Descrição:** Abstrair o ciclo de vida do navegador e isolar as chamadas diretas do Selenium com tratamentos de erro e *Explicit Waits*.
- **Entregáveis:**
  - `backend/base/driver_factory.py`: Gerenciamento centralizado da instância do `WebDriver` (Chrome/Edge, parâmetros e flags).
  - `backend/base/base_page.py`: Classe base com métodos wrappers genéricos (`find`, `click`, `type`, `wait_for_element`, `is_visible`).

---

## 2. Estrutura de Arquivos da Sprint 1

```text
projeto_automacao_coupa/
│
├── frontend/
│   ├── views/
│   ├── components/
│   └── main_window.py
│
├── backend/
│   ├── base/
│   │   ├── driver_factory.py     # Gerenciamento e inicialização do WebDriver
│   │   └── base_page.py          # Métodos genéricos e seguros do Selenium
│   ├── models/                   # Dataclasses puras de negócio
│   ├── pages/                    # Mapeamento POM (Coupa)
│   ├── services/
│   │   └── environment_service.py # Lógica de validação da HU01
│   └── automations/              # Orquestração dos fluxos
│
├── resources/
├── .env                          # Variáveis de ambiente
├── main.py                       # Ponto de entrada
└── requirements.txt              # Dependências do projeto
```

---

## 3. Definition of Done (DoD) da Sprint 1

A Sprint 1 será considerada **concluída** quando:
1. A estrutura de diretórios estiver criada e com imports funcionais.
2. O script de validação de ambiente (`environment_service.py`) for capaz de validar internet e Coupa antes de subir o browser.
3. A `BasePage` e o `DriverFactory` permitirem abrir e fechar o navegador de forma automatizada e segura sem vazamento de processos (`driver.quit()`).