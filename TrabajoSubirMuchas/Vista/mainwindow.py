# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append("../Controlador")
from controlador import *

class MainWindow(QtGui.QWidget):

  def __init__(self):
    super(MainWindow, self).__init__()
    self.controlador = MainController(self)
    self.init_ui()

  def init_ui(self):
    self.label = QtGui.QLabel("CANTIDAD DE PERSONAS")
    self.label2 = QtGui.QLabel()
    self.lineEdit = QtGui.QLineEdit()
    h_layout = QtGui.QHBoxLayout()
#    h_layout2 = QtGui.QHBoxLayout()
    button_subir = QtGui.QPushButton("Subir persona")
    button_bajar = QtGui.QPushButton("Bajar persona")
    button_subir5 = QtGui.QPushButton("Subir 5 personas")
    button_bajar5 = QtGui.QPushButton ("Bajar 5 personas")
    button_subirX = QtGui.QPushButton ("Subir esta cantidad:")
    button_bajarX = QtGui.QPushButton ("Bajar esta cantidad:")
    h_layout.addWidget(self.label)
    h_layout.addWidget(button_subir)
    h_layout.addWidget(button_bajar)
    h_layout.addWidget(button_subir5)
    h_layout.addWidget(button_bajar5)
    h_layout.addWidget(self.label2)
    h_layout.addWidget(button_subirX)
    h_layout.addWidget(button_bajarX)
    h_layout.addWidget(self.lineEdit)

#logica del controlador con los botones
    button_subir.clicked.connect(self.controlador.handler_subir_persona)
    button_bajar.clicked.connect(self.controlador.handler_bajar_persona)
    button_subir5.clicked.connect(self.controlador.handler_subir5_persona)
    button_bajar5.clicked.connect(self.controlador.handler_bajar5_persona)
    button_subirX.clicked.connect(self.controlador.hanlder_subirX_persona)
    button_bajarX.clicked.connect(self.controlador.hanlder_bajarX_persona)

#seteo de propiedades y widgets
    self.setLayout(h_layout)
    self.setWindowTitle("Maru y Mau lindos")
    self.setGeometry(200, 200, 200, 200)
    self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())

