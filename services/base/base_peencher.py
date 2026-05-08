from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePreencher:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def preencher_input(self, by, value, texto):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.clear()
        element.send_keys(texto)

    def selecionar_primeira_opcao(self, element):
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)