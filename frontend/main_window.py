import logging
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from frontend.components.log_console import LogConsoleWidget
from backend.services.environment_service import EnvironmentService, EnvironmentValidationError
from backend.base.driver_factory import DriverFactory

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    """Janela Principal da Aplicação de Automação Coupa."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automação de Requisições ERP Coupa (PR/PO)")
        self.resize(900, 650)
        self._setup_ui()

    def _setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Cabeçalho da Aplicação
        title_label = QLabel("Gerador de Requisições de Compra - Coupa")
        title_label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        main_layout.addWidget(title_label)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)

        # Container para os futuros formulários
        self.form_container = QVBoxLayout()
        placeholder_label = QLabel("Formulários de Entrada de Dados serão montados aqui nesta Sprint.")
        placeholder_label.setStyleSheet("color: #666; font-style: italic;")
        self.form_container.addWidget(placeholder_label)
        main_layout.addLayout(self.form_container)

        # Console de Logs Visual
        self.log_console = LogConsoleWidget()
        main_layout.addWidget(self.log_console)

        # Botão de Ação
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.btn_iniciar = QPushButton("Iniciar Automação")
        self.btn_iniciar.setStyleSheet("""
            QPushButton {
                background-color: #007ACC;
                color: white;
                font-weight: bold;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #005999;
            }
        """)
        self.btn_iniciar.clicked.connect(self._on_iniciar_click)
        button_layout.addWidget(self.btn_iniciar)

        main_layout.addLayout(button_layout)

    def _on_iniciar_click(self):
        """Dispara a validação e o fluxo de automação integrado à GUI."""
        logger.info("Iniciando processo de automação via Interface Gráfica...")
        
        env_service = EnvironmentService()
        
        try:
            # Step 1: Validações Pré-execução (HU01)
            env_service.validate_all()
            
            # Step 2: Teste do Browser
            logger.info("Iniciando WebDriver para teste de navegação...")
            driver = DriverFactory.create_driver(headless=False)
            driver.get(env_service.coupa_url)
            logger.info(f"Página acessada com sucesso: {driver.title}")
            
            driver.quit()
            logger.info("Validação prévia concluída com sucesso! Pronto para capturar os formulários.")

        except EnvironmentValidationError as e:
            logger.error(f"Execução bloqueada por trava de segurança: {e}")
        except Exception as e:
            logger.error(f"Erro não esperado durante a execução: {e}")