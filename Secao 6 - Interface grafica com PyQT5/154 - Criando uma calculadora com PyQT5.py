import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Thalles')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet('*{background: white; color: #000; font-size: 30px;}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_botao(
            QPushButton('CE'), 1, 0, 1, 1,
            lambda: self.display.setText(''),
            'background: #8ABEEF; color: #fff; font-weight: 700;'
        )
        self.add_botao(
            QPushButton('C'), 1, 1, 1, 1,
            lambda: self.display.setText(''),
            'background: #8ABEEF; color: #fff; font-weight: 700;'
        )
        self.add_botao(
            QPushButton('⌫'), 1, 2, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1],
            ),
            'background: #8ABEEF; color: #fff; font-weight: 700;'
        )
        self.add_botao(QPushButton('÷'), 1, 3, 1, 1)

        self.add_botao(QPushButton('7'), 2, 0, 1, 1)
        self.add_botao(QPushButton('8'), 2, 1, 1, 1)
        self.add_botao(QPushButton('9'), 2, 2, 1, 1)
        self.add_botao(QPushButton('*'), 2, 3, 1, 1)

        self.add_botao(QPushButton('4'), 3, 0, 1, 1)
        self.add_botao(QPushButton('5'), 3, 1, 1, 1)
        self.add_botao(QPushButton('6'), 3, 2, 1, 1)
        self.add_botao(QPushButton('-'), 3, 3, 1, 1)

        self.add_botao(QPushButton('1'), 4, 0, 1, 1)
        self.add_botao(QPushButton('2'), 4, 1, 1, 1)
        self.add_botao(QPushButton('3'), 4, 2, 1, 1)
        self.add_botao(QPushButton('+'), 4, 3, 1, 1)

        self.add_botao(QPushButton('1'), 4, 0, 1, 1)
        self.add_botao(QPushButton('2'), 4, 1, 1, 1)
        self.add_botao(QPushButton('3'), 4, 2, 1, 1)
        self.add_botao(QPushButton('+'), 4, 3, 1, 1)

        self.add_botao(QPushButton('+/-'), 5, 0, 1, 1)
        self.add_botao(QPushButton('0'), 5, 1, 1, 1)
        self.add_botao(QPushButton('.'), 5, 2, 1, 1)
        self.add_botao(
            QPushButton('='), 5, 3, 1, 1,
            self.eval_igual,
            'background: #F091F2; color: #fff; font-weight: 700;'
        )

        self.setCentralWidget(self.cw)

    def add_botao(self, botao, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(botao, row, col, rowspan, colspan)

        if not funcao:
            botao.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + botao.text()
                )
            )
        else:
            botao.clicked.connect(funcao)

        if style:
            botao.setStyleSheet(style)

        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
