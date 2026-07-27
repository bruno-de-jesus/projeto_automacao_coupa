import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

logger = logging.getLogger(__name__)

class DriverFactory:
    """Responsável por instanciar e configurar o WebDriver do Selenium."""

    @staticmethod
    def create_driver(headless: bool = False) -> webdriver.Chrome:
        """
        Cria e retorna uma instância configurada do Chrome WebDriver.
        
        :param headless: Se True, executa o navegador em segundo plano (sem GUI).
        :return: Instância do Chrome WebDriver.
        """
        logger.info("Inicializando instância do Chrome WebDriver...")
        options = ChromeOptions()
        
        # Argumentos de estabilidade e performance
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if headless:
            options.add_argument("--headless=new")

        try:
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(2)  # Baixo implicit wait pois usaremos Explicit Waits na BasePage
            logger.info("WebDriver inicializado com sucesso.")
            return driver
        except Exception as e:
            logger.error(f"Falha ao inicializar o WebDriver: {e}")
            raise e