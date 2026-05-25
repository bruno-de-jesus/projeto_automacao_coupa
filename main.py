import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.edge.options import Options

# importando data class e ações
from models.Pedido import Pedido
from models.InformacoesGerais import InformacoesGerais 
from models.TipoPedido import TipoPedido
from services.steps.preencher_info_gerais import PreencherInfoGerais
from services.steps.navegar_coupa import NavegarPedido


def conectar_navegador(): # configurar e conectar navegador
    load_dotenv()
    port = os.getenv("EDGE_DEBUG_PORT")

    edge_options = Options()
    edge_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")

    return webdriver.Edge(options=edge_options)

def main():
    # 1. preparação dos dados
    
    solicitante = "f57491"
    fornecedor = "C1 DIMENSIONAL"
    texto_cabecalho = f"COMPRA DE MATERIAIS ELETRICOS #12345 - {fornecedor}"
    tipo = TipoPedido.MATERIAL
    orcamento = "C:/ORÇAMENTOS/DIMENSIONAL/14508_5080661.PDF"

    pedido_info = InformacoesGerais(
        solicitante = solicitante,
        fornecedor = fornecedor,
        texto_cabecalho = texto_cabecalho,
        tipo = tipo,
        orcamento = orcamento
    )

    pedido_itens = [

    ]

    pedido_faturamento = [

    ]

    pedido_obj = Pedido(informacoes=pedido_info, itens=pedido_itens, faturamento=pedido_faturamento)

    # 2. iniciar automação
    driver = conectar_navegador()

    navegacao = NavegarPedido(driver) #abrir/navegar site
    navegacao.acessar_coupa()
    navegacao.acessar_pedido()

    try:
        # chamada para as funções de execução
        preenchimento = PreencherInfoGerais(driver)
        preenchimento.executar(pedido_obj.informacoes)

    except Exception as e:
        print(f"Erro ao executar automação: {e}")

if __name__ == "__main__":
    main()