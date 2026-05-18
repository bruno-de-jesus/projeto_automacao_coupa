import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class BasePreencher:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def buscar_elemento(self, by, value):
        return self.wait.until(
            EC.element_to_be_clickable(
                (by, value)
            )
        )

    def preencher_input(self, element, texto):
        element.clear()
        element.send_keys(texto)

    def selecionar_primeira_opcao(self, element):
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def apertar_botao(self, element):
        element.click()
    
    def centralizar_botao(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )