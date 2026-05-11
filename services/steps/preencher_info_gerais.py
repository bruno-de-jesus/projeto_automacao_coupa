"""
montar o passo a passo do que fazer após abrir o carrinho

1 - nome solicitante ✔️;
2 - informações coluna esquerda:
    . empresa - centro ✔️
    . texto cabeçalho ✔️
3 - informações coluna direita:
    . endereço: 7320 suzano
4 - orçamento:
    . anexar orçamento na aba do explorer


comando do console para saber quantos elementos com esse atributo existe:
$x ("//input[@name='requisition_header[on_behalf_of]']")
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from services.base.base_peencher import BasePreencher


class PreencherInfoGerais(BasePreencher):
    
    def executar(self, info):
        self._preencher_solicitante(info) #funcionando
        self._preencher_coluna_esquerda(info)
        self._preencher_coluna_direita(info)
        self._anexar_orcamento(info)

    def _preencher_solicitante(self, valor):
        em_nome_de = self.preencher_input(
            By.XPATH,
            "//input[@name='requisition_header[on_behalf_of]']",
            valor.solicitante
            )
        self.selecionar_primeira_opcao(em_nome_de)

        print("fim do solicitante")

    def _preencher_coluna_esquerda(self, valor):
        empresa_centro = self.preencher_input(
            By.XPATH,
            "//input[@aria-label='Empresa - Centro']",
            "0545"
        )
        self.selecionar_primeira_opcao()
        
        empresa_centro.send_keys("7320")
        self.selecionar_primeira_opcao()

        texto_cabecalho = self.preencher_input(
            By.XPATH,
            "//textarea[@name='requisition_header[custom_field_5]']",
            valor.texto_cabecalho
        )

        botao_locacao = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='requisition_header_custom_field_7_no']")
            )
        )

        if not botao_locacao.is_selected():
            botao_locacao.click()

        print("fim da coluna esquerda")

    def _preencher_coluna_direita(self, valor):
        print()
    def _anexar_orcamento(self, valor):
        print()