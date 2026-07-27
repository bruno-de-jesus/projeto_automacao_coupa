import logging
from typing import Tuple, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class BasePage:
    """Classe base genérica que encapsula comandos do Selenium com Explicit Waits."""

    def __init__(self, driver: WebDriver, default_timeout: int = 10):
        self.driver = driver
        self.timeout = default_timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """Aguarda e localiza um elemento visível na página."""
        logger.debug(f"Aguardando visibilidade do elemento: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Aguarda a presença de múltiplos elementos na página."""
        logger.debug(f"Aguardando presença dos elementos: {locator}")
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: Tuple[str, str]) -> None:
        """Aguarda o elemento estar clicável e executa o clique."""
        logger.debug(f"Aguardando elemento ser clicável para clique: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator: Tuple[str, str], text: str, clear_first: bool = True) -> None:
        """Aguarda o campo de texto estar visível, limpa seu conteúdo e digita o texto."""
        element = self.find(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
        logger.debug(f"Texto inserido no elemento {locator}")

    def is_visible(self, locator: Tuple[str, str], timeout: int = 3) -> bool:
        """Verifica se um elemento está visível em tela sem estourar exceção impeditiva."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Mapeia o texto visível de um elemento."""
        return self.find(locator).text