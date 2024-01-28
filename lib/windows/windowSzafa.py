from PyQt6.QtWidgets import *
from PyQt6 import uic

class WindowSzafa(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"lib/gui/gui.ui",self)

        self.__interface()
        self.__actions()

        self.show()

    def __interface(self):
        self.__x_size = self.findChild(QLineEdit, "x_size")
        self.__y_size = self.findChild(QLineEdit, "y_size")
        self.__z_size = self.findChild(QLineEdit, "z_size")

        self.__lblResult = self.findChild(QLabel, "label_dziala")

        self.__x_label = self.findChild(QLabel, "Xsize_label")
        self.__y_label = self.findChild(QLabel, "Ysize_label")
        self.__z_label = self.findChild(QLabel, "Zsize_label")

        self.__push_button = self.findChild(QPushButton, "count_sizes")



    def __actions(self):
        self.__push_button.clicked.connect(self.__oblicz)

    def __oblicz(self):
        # t = QLineEdit()
        self.__dl = self.__x_size.text()
        self.__sz = self.__y_size.text()
        self.__wy = self.__z_size.text()
        from lib.utils.validator import isNumber
        if isNumber(self.__dl) and isNumber(self.__sz) and isNumber(self.__wy):
            self.__dl = float(self.__dl)
            self.__sz = float(self.__sz)
            self.__wy = float(self.__wy)
            from lib.classes.cabinet import Cabinet
            self.__shafa = Cabinet(self.__dl, self.__sz, self.__wy)
            self.__lblResult.setText(f"Objętośż wynosi: {self.__shafa.volume():.2f}")



