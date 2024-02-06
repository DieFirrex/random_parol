from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from random import *

    

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.example)
    
    def example(self):
        signs = ''
        if self.ui.checkBox_2.isChecked():
            signs = 'qwertyuiopasdfghjklzxcvbnmcm'
        if self.ui.checkBox.isChecked():
            signs += '0123456789'
        result = ''
        try:
            length = int(self.ui.lineEdit.text())
            for i in range(length):
                result += choice(signs)
            self.ui.lineEdit_2.setText(result)
        except ValueError:
            self.ui.lineEdit_2.setText("Будьласка введіть довжину пароля")


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
