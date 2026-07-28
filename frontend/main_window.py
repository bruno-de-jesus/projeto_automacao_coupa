import logging
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QFrame
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Slot

from frontend.components.log_console import LogConsoleWidget
from frontend.automation_worker import AutomationWorker

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    """Janela Principal da Aplicação de Automação Coupa."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automação de Requisições ERP Coupa (PR/PO)")
        self.resize(900, 650)
        self.worker = None
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

        # Container para os futuros formulários de entrada de dados
        self.form_container = QVBoxLayout()
        placeholder_label = QLabel("Formulários de Entrada de Dados (Usuários, Cabeçalho, Custo e Itens) serão montados aqui.")
        placeholder_label.setStyleSheet("color: #666; font-style: italic;")
        self.form_container.addWidget(placeholder_label)
        main_layout.addLayout(self.form_container)

        # Console de Logs em Tempo Real
        self.log_console = LogConsoleWidget()
        main_layout.addWidget(self.log_console)

        # Painel de Botões / Controle
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
            QPushButton:disabled {
                background-color: #A0A0A0;
            }
        """)
        self.btn_iniciar.clicked.connect(self._on_iniciar_click)
        button_layout.addWidget(self.btn_iniciar)

        main_layout.addLayout(button_layout)

    def _on_iniciar_click(self):
        """Slot disparado ao clicar no botão 'Iniciar Automação'."""
        logger.info("Iniciando requisição de automação em background...")
        
        # Desabilita o botão para impedir disparos múltiplos concorrentes
        self.btn_iniciar.setEnabled(False)
        self.btn_iniciar.setText("Executando...")

        # Instancia e configura a Worker Thread
        self.worker = AutomationWorker()
        self.worker.finished_signal.connect(self._on_automation_finished)
        
        # Inicia a execução em background (chama a função run() do worker)
        self.worker.start()

    @Slot(bool, str)
    def _on_automation_finished(self, success: bool, message: str):
        """Slot executado quando a Worker Thread encerra seu trabalho."""
        if success:
            logger.info(f"Status da Automação: {message}")
        else:
            logger.error(f"Falha na Automação: {message}")

        # Restaura o estado original do botão na interface
        self.btn_iniciar.setEnabled(True)
        self.btn_iniciar.setText("Iniciar Automação")