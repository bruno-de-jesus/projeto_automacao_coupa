"""
montar o passo a passo do que fazer após abrir o carrinho

1 - nome solicitante ✔️;
2 - informações coluna esquerda:
    . empresa - centro
    . texto cabeçalho
3 - informações coluna direita:
    . endereço: 7320 suzano
4 - orçamento:
    . anexar orçamento na aba do explorer
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from services.base.base_peencher import BasePreencher 


class PreencherInfoGerais(BasePreencher):
    
    def executar(self, info):
        self._preencher_solicitante(info.solicitante)
        self._preencher_coluna_esquerda(info)
        self._preencher_coluna_direita(info)
        self._anexar_orcamento(info.orcamento)

    def _preencher_solicitante(self, valor):
        em_nome_de = self.preencher_input(
            By.XPATH,
            "//input[@name='requisition_header[on_behalf_of]']",
            valor
            )
        self.selecionar_primeira_opcao(em_nome_de)

    def _preencher_coluna_esquerda(self, valor):
        print()
    def _preencher_coluna_direita(self, valor):
        print()
    def _anexar_orcamento(sel, valor):
        print()