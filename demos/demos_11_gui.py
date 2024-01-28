from PyQt6.QtWidgets import QApplication
from lib.windows.windowSzafa import *
import sys

def demo_10_gui():
    app = QApplication(sys.argv)
    okno=WindowSzafa()

    sys.exit(app.exec())


