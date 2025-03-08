import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit)

from PySide6.QtCore import Qt

class Calculadora (QMainWindow):
    def __init__(self):
            super().__init__()
            self.setWindowTitle('Calculadora')
            
            #Configurar o visor
            self.visor = QLineEdit()
            self.visor.setReadOnly(True)
            self.visor.setAlignment(Qt.AlignRight)
            self.visor.setFixedHeight(35)
            
            #Configurar layout principal
            layout_principal = QVBoxLayout()
            layout_principal.addWidget(self.visor)
            
            #layout dos botoes
            layout_botoes = QVBoxLayout()
            
            layout_linha_superior = QHBoxLayout()
            
            botao_limpar = QPushButton('C')
            botao_limpar.setFixedSize(50,50)
            #evento de limpar
            layout_linha_superior.addWidget(botao_limpar)
            
            botao_parenteses_abrir = QPushButton('(')
            botao_parenteses_abrir.setFixedSize(50,50)
            #evento 
            layout_linha_superior.addWidget(botao_parenteses_abrir)
            
            botao_parenteses_fechar = QPushButton(')')
            botao_parenteses_fechar.setFixedSize(50,50)
            #evento 
            layout_linha_superior.addWidget(botao_parenteses_fechar)
            
            botao_x2 = QPushButton('x²')
            botao_x2.setFixedSize(50,50)
            #evento 
            layout_linha_superior.addWidget(botao_x2)
            
            layout_botoes.addLayout(layout_linha_superior)
            
            botoes = [
                ['7','8','9','/'],
                ['4','5','6','*'],
                ['1','2','3','-'],
                ['0','.','=','+']
            ]
            
            for linha in botoes:
                layout_linha = QHBoxLayout ()
                for texto in linha:
                    botao = QPushButton(texto)
                    botao.setFixedSize(50,50)
                    #evento
                    layout_linha.addWidget(botao)
                layout_botoes.addLayout(layout_linha)
            
            layout_principal.addLayout(layout_botoes)
            
            central_widget = QWidget()
            central_widget.setLayout(layout_principal)
            self.setCentralWidget(central_widget)
            
            #area dis netidis dis slots
            
if __name__ =="__main__":
    app = QApplication(sys.argv)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec())