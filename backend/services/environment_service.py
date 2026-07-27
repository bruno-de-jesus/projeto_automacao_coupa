import os
import logging
import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

class EnvironmentValidationError(Exception):
    """Exceção customizada lançada quando uma validação de ambiente falha."""
    pass

class EnvironmentService:
    """Serviço responsável por validar pré-requisitos operacionais (HU01) antes de iniciar a automação."""

    def __init__(self):
        # Carrega variáveis registradas no arquivo .env
        load_dotenv()
        self.coupa_url = os.getenv("COUPA_URL")

    def check_internet_connection(self, host: str = "8.8.8.8", port: int = 53, timeout: int = 3) -> bool:
        """Valida se o computador possui conectividade de rede ativa."""
        import socket
        logger.info("Checando conectividade com a internet...")
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            logger.info("Conexão com a internet confirmada.")
            return True
        except Exception:
            logger.error("Falha de conexão com a internet.")
            return False

    def check_coupa_availability(self, timeout: int = 5) -> bool:
        """Dispara uma requisição HTTP HEAD/GET para confirmar se o ERP Coupa está acessível."""
        if not self.coupa_url:
            logger.error("A URL do Coupa não foi definida no arquivo .env (COUPA_URL).")
            return False

        logger.info(f"Validando disponibilidade do ERP Coupa no endereço: {self.coupa_url}")
        try:
            response = requests.get(self.coupa_url, timeout=timeout, allow_redirects=True)
            # Aceita status 200 (OK) ou redirecionamentos de login padrão (302/301)
            if response.status_code in [200, 301, 302]:
                logger.info(f"ERP Coupa respondeu com status código {response.status_code}.")
                return True
            else:
                logger.warning(f"ERP Coupa respondeu com status código inesperado: {response.status_code}")
                return False
        except requests.RequestException as e:
            logger.error(f"Não foi possível alcançar a URL do Coupa: {e}")
            return False

    def validate_all(self) -> None:
        """
        Executa a suíte completa de validações prévias.
        Lança EnvironmentValidationError caso algum pré-requisito falhe.
        """
        logger.info("Iniciando bateria de validações de ambiente (HU01)...")
        
        if not self.check_internet_connection():
            raise EnvironmentValidationError("Sem conexão com a internet. Verifique sua rede e tente novamente.")

        if not self.coupa_url:
            raise EnvironmentValidationError("Variável COUPA_URL não configurada no arquivo .env.")

        if not self.check_coupa_availability():
            raise EnvironmentValidationError("O sistema Coupa está indisponível ou inacessível no momento.")

        logger.info("Todas as validações de ambiente (HU01) foram concluídas com sucesso!")