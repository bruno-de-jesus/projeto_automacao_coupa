import logging
from backend.services.environment_service import EnvironmentService, EnvironmentValidationError
from backend.base.driver_factory import DriverFactory

# Configuração de Logs no Console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

def run():
    env_service = EnvironmentService()
    
    try:
        # Step 1: Validações Pré-execução (HU01)
        env_service.validate_all()
        
        # Step 2: Teste de Inicialização da Infraestrutura do Browser
        print("\n--- Iniciando Teste de WebDriver ---")
        driver = DriverFactory.create_driver(headless=False)
        driver.get(env_service.coupa_url)
        print(f"Página acessada com sucesso: {driver.title}")
        
        # Encerra com segurança
        driver.quit()
        print("--- Teste da Sprint 1 Concluído com Sucesso! ---")

    except EnvironmentValidationError as e:
        logging.error(f"Execução bloqueada por trava de segurança: {e}")
    except Exception as e:
        logging.error(f"Erro não esperado durante a execução: {e}")

if __name__ == "__main__":
    run()