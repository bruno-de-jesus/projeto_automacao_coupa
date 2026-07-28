import sys
import logging
from PySide6.QtWidgets import QApplication
from frontend.main_window import MainWindow

def setup_global_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

def main():
    setup_global_logging()
    
    # Inicializa o loop de eventos da interface gráfica
    app = QApplication(sys.argv)
    
    # Instancia e exibe a janela principal
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()