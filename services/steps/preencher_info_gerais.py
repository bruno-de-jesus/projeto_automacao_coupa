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

    def _preencher_solicitante(self, dado):
        em_nome_de = self.buscar_elemento(
            By.XPATH,
            "//input[@name='requisition_header[on_behalf_of]']"
        )
        self.preencher_input(em_nome_de, dado.solicitante)
        self.selecionar_primeira_opcao(em_nome_de)

        print("fim do solicitante")

    def _preencher_coluna_esquerda(self, dado):

        empresa_centro = self.buscar_elemento(
            By.XPATH,
            "//div[@id='requisition_header_custom_field_4_id_chosen']"
        )
        
        texto_cabecalho = self.buscar_elemento(
            By.XPATH,
            "//textarea[@name='requisition_header[custom_field_5]']"
        )
        botao_locacao = self.buscar_elemento(
            By.XPATH,
            "//input[@id='requisition_header_custom_field_7_no']"
        )
        self.centralizar_botao(empresa_centro)
        self.apertar_botao(empresa_centro)
        
        empresa_centro_input = self.buscar_elemento(
            By.XPATH,
            "//input[@aria-label='Empresa - Centro']",
        )
        
        self.preencher_input(empresa_centro_input, "0545")
        self.selecionar_primeira_opcao(empresa_centro_input)
        self.preencher_input(empresa_centro_input, "7320")
        self.selecionar_primeira_opcao(empresa_centro_input)
        self.preencher_input(texto_cabecalho, dado.texto_cabecalho)
        
        self.centralizar_botao(botao_locacao)
        if not botao_locacao.is_selected():
            self.apertar_botao(botao_locacao)

        print("fim da coluna esquerda")

    def _preencher_coluna_direita(self, valor):
        endereco = self.buscar_elemento(
            By.XPATH,
            "//img[@title='Escolher um endereço']"
        )
        self.centralizar_botao(endereco)
        self.apertar_botao(endereco)
        
        #selecionando endereço 7320
        
        
        
        
    def _anexar_orcamento(self, valor):
        print()