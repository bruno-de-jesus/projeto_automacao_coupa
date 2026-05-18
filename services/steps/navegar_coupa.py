import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from services.base.base_peencher import BasePreencher


class NavegarPedido(BasePreencher):
    pass

    def acessar_coupa(self):
        # acessa o site do Coupa
        load_dotenv()
        url_coupa = os.getenv("COUPA_URL")
        
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.get(url_coupa)
        print("Coupa acessado")

    def acessar_pedido(self):
        # aqui você pode adicionar navegação interna depois
        print("Acessando tela de pedido")
        
        carrinho = self.buscar_elemento(By.XPATH, "//span[@data-testid='cartCount']")
        
        if int(carrinho.text) == 0:
            
            self.apertar_botao(carrinho)
            
            revisar_carrinho = self.buscar_elemento(By.XPATH, "//div[@class='coupaCartPopover__footer']/a")
            self.apertar_botao(revisar_carrinho)
        else:
            
            print("O carrinho não esta zerado. Por favor, finalize o pedido em andamento primeiro.")