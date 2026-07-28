import logging
from PySide6.QtCore import QThread, Signal
from backend.services.environment_service import EnvironmentService, EnvironmentValidationError
from backend.base.driver_factory import DriverFactory

logger = logging.getLogger(__name__)

class AutomationWorker(QThread):
    """Thread em segundo plano para executar tarefas pesadas de automação sem congelar a GUI."""
    
    # Sinais para comunicação assíncrona com a Interface
    finished_signal = Signal(bool, str) # (Sucesso/Falha, Mensagem)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        """Método executado automaticamente ao chamar worker.start()."""
        logger.info("Worker iniciou a execução da automação em background...")
        env_service = EnvironmentService()
        
        try:
            # Step 1: Validações Pré-execução (HU01)
            env_service.validate_all()
            
            # Step 2: Teste de Inicialização do Browser
            logger.info("Iniciando WebDriver para navegação...")
            driver = DriverFactory.create_driver(headless=False)
            driver.get(env_service.coupa_url)
            logger.info(f"Página acessada com sucesso: {driver.title}")
            
            # Encerra o driver ao concluir esta etapa de teste
            driver.quit()
            logger.info("Validação prévia e teste de browser concluídos com sucesso!")
            
            # Notifica a interface sobre a conclusão bem-sucedida
            self.finished_signal.emit(True, "Validação de ambiente realizada com sucesso!")

        except EnvironmentValidationError as e:
            logger.error(f"Execução bloqueada por trava de segurança: {e}")
            self.finished_signal.emit(False, str(e))
        except Exception as e:
            logger.error(f"Erro não esperado durante a execução da automação: {e}")
            self.finished_signal.emit(False, f"Erro inesperado: {e}")