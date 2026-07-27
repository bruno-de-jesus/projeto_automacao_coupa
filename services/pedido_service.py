from services.steps.preencher_info_gerais import PreencherInfoGerais
from services.steps.preencher_custos import PreencherCustos


class PedidoService:

    def __init__(self, driver):
        self.driver = driver

        self.info_gerais = PreencherInfoGerais(driver)

    def executar(self, info, custo):
        self.info_gerais.executar(info)