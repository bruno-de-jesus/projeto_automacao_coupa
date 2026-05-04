import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.edge.options import Options

# importando data class e ações
#from models.pedido import 
#from core.actions import

def conectar_navegador(): # configurar e conectar navegador
    load_dotenv()
    port = os.getenv("EDGE_DEBUG_PORT")

    edge_options = Options()
    edge_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")

    return webdriver.Edge(options=edge_options)

def main():
    # 1. preparação dos dados
    info_pedido = informacoes_gerais(
        titulo="material ou serviço"
    )

    itens_pedido = [

    ]

    meu_pedido = Pedido(informacoes=info_pedido, itens=itens_pedido)

    # 2. iniciar automação
    driver = conectar_navegador()

    try:
        print(f"conectando ao Edge. Criando pedido: {meu_pedido.informacoes.titulo}")

        # chamada para as funções de execução

        print("automação concluída")

    except Exception as e:
        print(f"Erro ao executar automação: {e}")

if __name__ == "__main__":
    main()