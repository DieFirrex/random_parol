from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from random import *

class Widget(QMainWindow):
    def   __init__(self):
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
        for i in range(10):
            result += choice(signs)
        self.ui.label_3.setText(result)


    




app = QApplication([])
ex = Widget()
ex.show()
app.exec_()