# Análise da Arquitetura Atual e Plano de Migração para Layered Architecture + POM

## Estrutura Atual

```text
projeto_automacao_coupa/
│
├── models/
├── scripts/
│   └── abrir_edge.bat
│
├── services/
│   ├── base/
│   │   └── base_preencher.py
│   │
│   ├── steps/
│   │   ├── navegar_coupa.py
│   │   ├── preencher_custo.py
│   │   ├── preencher_info_gerais.py
│   │   └── preencher_itens.py
│   │
│   ├── pedido_service.py
│   │
│   └── __init__.py
│
├── .env
├── main.py
└── requirements.txt
```

---

## Qual arquitetura está sendo utilizada atualmente?

A estrutura atual não caracteriza um Page Object Model (POM) clássico.

Ela está mais próxima de uma arquitetura baseada em fluxo de execução (Workflow/Steps Architecture), onde cada arquivo representa uma etapa do processo de negócio.

Exemplo:

```text
PedidoService
    ↓
Navegar Coupa
    ↓
Preencher Informações Gerais
    ↓
Preencher Centro de Custo
    ↓
Preencher Itens
```

### Características observadas

#### Camada Base

```text
services/base/
```

Provavelmente contém métodos compartilhados:

```python
clicar()
preencher()
aguardar()
selecionar()
```

#### Camada Steps

```text
services/steps/
```

Cada arquivo representa uma etapa específica da automação.

Exemplo:

```python
navegar_coupa.py
preencher_info_gerais.py
preencher_custo.py
preencher_itens.py
```

#### Service

```text
pedido_service.py
```

Responsável por coordenar a execução do processo.

Exemplo:

```python
def executar():
    navegar()
    preencher_info()
    preencher_itens()
```

---

## Isso é POM?

Resposta curta:

```text
Não.
```

Resposta técnica:

```text
É uma arquitetura baseada em Steps.
```

No POM verdadeiro, a organização acontece por páginas do sistema, e não por etapas do fluxo.

---

## Diferença entre Steps e POM

### Atual (Steps)

```text
steps/
├── navegar_coupa.py
├── preencher_info_gerais.py
├── preencher_custo.py
└── preencher_itens.py
```

A organização está baseada na ação executada.

---

### POM

```text
pages/
├── login_page.py
├── home_page.py
├── pedido_page.py
└── aprovacao_page.py
```

A organização está baseada nas páginas reais do sistema.

---

## Problema da estrutura atual

Exemplo comum:

```python
# preencher_info_gerais.py

driver.find_element(...)
driver.find_element(...)
driver.find_element(...)
```

Se outro fluxo precisar preencher as mesmas informações, haverá duplicação de código.

---

## Como ficaria utilizando POM

### Exemplo

```python
class PedidoPage:

    def preencher_info_gerais(self):
        pass

    def preencher_centro_custo(self):
        pass

    def adicionar_item(self):
        pass
```

Agora qualquer fluxo reutiliza os mesmos métodos.

---

# Arquitetura Recomendada

## Layered Architecture + POM

Fluxo:

```text
Frontend
    ↓
Automation
    ↓
Service
    ↓
Page Object
    ↓
BasePage
    ↓
Selenium
```

---

## Estrutura Recomendada

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
│   │   ├── login_page.py
│   │   ├── home_page.py
│   │   ├── pedido_page.py
│   │   └── aprovacao_page.py
│   │
│   ├── services/
│   │   ├── login_service.py
│   │   └── pedido_service.py
│   │
│   ├── automations/
│   │   ├── criar_pedido.py
│   │   └── aprovar_pedido.py
│   │
│   ├── models/
│   │   ├── pedido.py
│   │   └── usuario.py
│   │
│   └── base/
│       ├── base_page.py
│       ├── driver_manager.py
│       └── waits.py
│
├── resources/
│   ├── icons/
│   ├── images/
│   ├── templates/
│   └── config/
│
├── .env
├── main.py
├── requirements.txt
└── app.spec
```

---

# Plano de Migração

## Etapa 1 — Criar a camada Pages

Criar:

```text
backend/pages/
```

---

## Etapa 2 — Migrar seletores para as Pages

Hoje:

```text
services/steps/preencher_info_gerais.py
```

Passa para:

```text
backend/pages/pedido_page.py
```

Exemplo:

```python
class PedidoPage:

    def preencher_info_gerais(self):
        pass
```

---

## Etapa 3 — Services passam a orquestrar Pages

Antes:

```python
driver.find_element(...)
```

Depois:

```python
pedido_page.preencher_info_gerais()
pedido_page.preencher_centro_custo()
pedido_page.adicionar_item()
```

---

## Etapa 4 — Criar camada de Automações

```text
backend/automations/
```

Exemplo:

```python
class CriarPedidoAutomation:

    def executar(self):
        LoginService().realizar_login()
        PedidoService().criar_pedido()
```

---

## Mapeamento sugerido dos arquivos atuais

### Atual

```text
services/steps/navegar_coupa.py
```

### Futuro

```text
backend/pages/home_page.py
```

---

### Atual

```text
services/steps/preencher_info_gerais.py
```

### Futuro

```text
backend/pages/pedido_page.py
```

---

### Atual

```text
services/steps/preencher_custo.py
```

### Futuro

```text
backend/pages/pedido_page.py
```

---

### Atual

```text
services/steps/preencher_itens.py
```

### Futuro

```text
backend/pages/pedido_page.py
```

---

## Benefícios da nova arquitetura

### POM

```text
✅ Baixo acoplamento
✅ Reutilização de código
✅ Manutenção simplificada
✅ Centralização de seletores
✅ Facilidade para mudanças na UI do Coupa
```

### Layered Architecture

```text
✅ Separação clara de responsabilidades
✅ Melhor testabilidade
✅ Escalabilidade
✅ Facilidade de integração com frontend
✅ Organização compatível com PyInstaller
```

---

## Observação para PyInstaller

Manter recursos externos em uma pasta dedicada:

```text
resources/
```

E acessar sempre utilizando:

```python
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)
```

Para empacotamento:

```bash
pyinstaller --clean --noconfirm app.spec
```

Adicionar recursos no `.spec`:

```python
datas=[
    ('resources', 'resources'),
    ('.env', '.'),
]
```
