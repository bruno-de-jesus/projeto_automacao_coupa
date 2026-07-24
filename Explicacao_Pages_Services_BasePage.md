# Onde Devem Ficar as Funções de Preencher Inputs e Clicar em Botões na Arquitetura Layered + POM

## Resposta Curta

Na arquitetura **Layered Architecture + Page Object Model (POM)**:

- Seletores ficam nas **Pages**
- Ações da interface ficam nas **Pages**
- Operações reutilizáveis ficam na **BasePage**
- Regras de negócio ficam nos **Services**
- Fluxos completos ficam nas **Automations**

---

# Estrutura Recomendada

```text
backend/
│
├── pages/
│   ├── login_page.py
│   └── pedido_page.py
│
├── services/
│   └── pedido_service.py
│
└── base/
    └── base_page.py
```

---

# Onde Fica o Localizador do Botão?

Arquivo:

```text
backend/pages/pedido_page.py
```

Exemplo:

```python
from selenium.webdriver.common.by import By

class PedidoPage:

    BTN_CRIAR_PEDIDO = (
        By.XPATH,
        "//button[contains(., 'Criar Pedido')]"
    )
```

Os seletores devem ficar centralizados na própria página.

---

# Onde Fica o Clique do Botão?

Também na própria Page.

```python
class PedidoPage:

    BTN_CRIAR_PEDIDO = (
        By.XPATH,
        "//button[contains(., 'Criar Pedido')]"
    )

    def clicar_criar_pedido(self):
        self.driver.find_element(
            *self.BTN_CRIAR_PEDIDO
        ).click()
```

---

# Onde Fica o Preenchimento de um Input?

Também na Page.

```python
class PedidoPage:

    TXT_DESCRICAO = (
        By.ID,
        "description"
    )

    def preencher_descricao(self, texto):

        campo = self.driver.find_element(
            *self.TXT_DESCRICAO
        )

        campo.clear()
        campo.send_keys(texto)
```

---

# O Que Fica no Service?

O Service deve conter apenas regras de negócio e orquestração.

```python
class PedidoService:

    def criar_pedido(self, pedido):

        page = PedidoPage(self.driver)

        page.preencher_descricao(
            pedido.descricao
        )

        page.preencher_centro_custo(
            pedido.centro_custo
        )

        page.clicar_salvar()
```

O Service:

```text
✅ Sabe o fluxo
✅ Sabe as regras de negócio
❌ Não conhece XPath
❌ Não conhece CSS Selectors
❌ Não utiliza find_element diretamente
```

---

# O Que Fica na BasePage?

Tudo que é repetido em várias páginas.

```python
class BasePage:

    def clicar(self, locator):
        self.driver.find_element(*locator).click()

    def preencher(self, locator, texto):

        elemento = self.driver.find_element(
            *locator
        )

        elemento.clear()
        elemento.send_keys(texto)

    def obter_texto(self, locator):

        return self.driver.find_element(
            *locator
        ).text
```

---

# Exemplo Profissional

```python
class PedidoPage(BasePage):

    TXT_DESCRICAO = (
        By.ID,
        "description"
    )

    BTN_SALVAR = (
        By.ID,
        "save-btn"
    )

    def preencher_descricao(self, descricao):
        self.preencher(
            self.TXT_DESCRICAO,
            descricao
        )

    def salvar(self):
        self.clicar(
            self.BTN_SALVAR
        )
```

Com isso, toda a lógica de Selenium fica encapsulada.

---

# Estrutura Ideal para o Projeto Coupa

```text
backend/
│
├── base/
│   ├── base_page.py
│   └── driver_manager.py
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   ├── pedido_page.py
│   └── aprovacao_page.py
│
├── services/
│   ├── login_service.py
│   └── pedido_service.py
│
├── automations/
│   └── criar_pedido_automation.py
│
└── models/
```

---

# Fluxo Completo

```text
Automation
    ↓
Service
    ↓
Page
    ↓
BasePage
    ↓
Selenium
```

---

# Regra Prática

```text
find_element()       → Pages/BasePage

XPath/CSS/ID         → Pages

click()              → Pages/BasePage

send_keys()          → Pages/BasePage

Fluxo de negócio     → Services

Execução completa    → Automations

Dados                → Models
```

---

# Aplicando ao Projeto Atual

Os arquivos atuais:

```text
services/steps/preencher_info_gerais.py
services/steps/preencher_custo.py
services/steps/preencher_itens.py
```

São fortes candidatos para migração para:

```text
backend/pages/pedido_page.py
```

Centralizando:

```text
✅ Seletores
✅ Cliques
✅ Preenchimentos
✅ Navegações da página
```

Enquanto os Services ficam responsáveis apenas pela orquestração e regras de negócio.
