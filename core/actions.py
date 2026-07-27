from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.pedido import (
    Pedido,
    TipoPedido,
    ItemServico, # se o item for serviço
    ItemMaterial, # se o item for material
    CustoAPP, # se o faturamento for em APP
    CustoCentro, # se o faturamento for em centro de custo
    InformacoesGerais,
)

def preencher_informacoes_gerais(driver, informacoes):
    # preencher informações gerais do pedido Coupa
    print(f"preenchendo informações gerais do pedido: {informacoes.texto_cabecalho}")
    wait = WebDriverWait(driver, 15)

    try:
        # colocando solicitante no pedido
        campo_solicitante = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[id='requisition_header_on_behalf_of'")))
        campo_solicitante.clear()
        campo_solicitante.send_keys(informacoes.solicitante)

    except Exception as e:
        print(f"error: {e}")