import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão 1')
botao.setStyleSheet('font-size: 40px; color: red')

botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size: 40px; color: red')

botao3 = QPushButton('Texto do botão 3')
botao3.setStyleSheet('font-size: 40px; color: red')

central_widget = QWidget()

layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

##botao = elemento, 1°= linha 2°= coluna 3°= quantas linhas 4°= quantas colunas

central_widget.show()

app.exec()