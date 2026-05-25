from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from services.base.base_peencher import BasePreencher


class PreencherInfoGerais(BasePreencher):
    
    def executar(self, info):
        self._preencher_solicitante(info) #funcionando
        self._preencher_coluna_esquerda(info)
        self._preencher_coluna_direita()
        self._anexar_orcamento(info)

    def _preencher_solicitante(self, dado):
        em_nome_de = self.buscar_elemento(
            By.XPATH,
            "//input[@name='requisition_header[on_behalf_of]']"
        )
        self.preencher_input(em_nome_de, dado.solicitante)
        self.selecionar_primeira_opcao(em_nome_de)

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

    def _preencher_coluna_direita(self):
        endereco = self.buscar_elemento(
            By.XPATH,
            "//img[@title='Escolher um endereço']"
        )
        self.centralizar_botao(endereco)
        self.apertar_botao(endereco)
        
        pesquisa = self.buscar_elemento(
            By.XPATH,
            "//input[@id='sf_picker_address']"
        )
        self.preencher_input(pesquisa,"7320")

        botao_pesquisa = self.buscar_elemento(
            By.XPATH,
            "//a[@id='sfBtn_picker_address']"
        )
        self.apertar_botao(botao_pesquisa)


        botao_escolher = self.buscar_elemento(
            By.XPATH,
            "//tr[td[normalize-space()='7320']]//a"
        )
        self.apertar_botao(botao_escolher)
        
    def _anexar_orcamento(self, dado):
        arquivo = self.buscar_elemento(
            By.XPATH,
            "//a[@aria-label='Adicionar anexo de arquivo']"
        )
        self.apertar_botao(arquivo)
        enviar_fornecedor = self.buscar_elemento(
            By.XPATH,
            "//input[@id='requisition_header_attachments_attributes_attachment_intent']"
        )
        if not enviar_fornecedor.is_selected():
            self.apertar_botao(enviar_fornecedor)

        from selenium.webdriver.support.ui import WebDriverWait

        adicionar_anexo = self.buscar_elemento_lambda(
            By.CSS_SELECTOR,
            "#requisition_header_attachments_attributes_attachment input[type='file']"
        ) 

        self.preencher_input(adicionar_anexo, dado.orcamento)