import sys
from validacpf import valida_cpf
from geradorcpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import desing


class GeraValidaCPF(QMainWindow, desing.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCpf.clicked.connect(self.gera_cpf)
        self.btnValidaCpf.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setText(
            str(gera_cpf())
        )

    def valida_cpf(self):
        cpf = self.inputValidaCpf.text()
        self.labelRetorno.setText(
            str(valida_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()