import logging
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtCore import QObject, Signal, Slot

class QSignalingLogHandler(QObject, logging.Handler):
    """Handler customizado do logging que envia mensagens via sinais Qt (Thread-Safe)."""
    log_signal = Signal(str)

    def __init__(self):
        QObject.__init__(self)
        logging.Handler.__init__(self)

    def emit(self, record):
        msg = self.format(record)
        self.log_signal.emit(msg)

class LogConsoleWidget(QWidget):
    """Componente visual de console de logs em tempo real."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
        self._setup_logging()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel("Console de Execução / Logs:")
        label.setFont(QFont("Segoe UI", 9, QFont.Bold))
        layout.addWidget(label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setFont(QFont("Consolas", 9))
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #D4D4D4;
                border: 1px solid #3C3C3C;
                border-radius: 4px;
            }
        """)
        layout.addWidget(self.text_edit)

    def _setup_logging(self):
        self.handler = QSignalingLogHandler()
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%H:%M:%S")
        self.handler.setFormatter(formatter)
        self.handler.log_signal.connect(self.append_log)

        # Registra o handler no logger raiz
        root_logger = logging.getLogger()
        root_logger.addHandler(self.handler)
        root_logger.setLevel(logging.INFO)

    @Slot(str)
    def append_log(self, text: str):
        """Adiciona uma nova linha de log ao console e rola automaticamente para o fim."""
        self.text_edit.append(text)
        self.text_edit.moveCursor(QTextCursor.End)