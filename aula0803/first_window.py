import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app = QApplication(sys.argv)

central_widget = QWidget()
window = QMainWindow()

window.setCentralWidget(central_widget)
window.setWindowTitle('Minha primeira janela')

botao = QPushButton('Texto do botão 1')
botao.setStyleSheet('font-size: 40px; color: red')
botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size: 40px; color: red')
botao3 = QPushButton('Texto do botão 3')
botao3.setStyleSheet('font-size: 40px; color: red')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

def slot_exemple(status_bar):
    status_bar.showMessage('O meu slot foi executado')
    
status_bar = window.statusBar()

menu = window.menuBar()

primeiro_menu = menu.addMenu ('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')

primeira_acao.triggered.connect(
    lambda: slot_exemple(status_bar)
)

window.show()
app.exec()
