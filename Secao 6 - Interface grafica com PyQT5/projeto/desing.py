# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desing.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 185)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inputValidaCpf = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        self.inputValidaCpf.setFont(font)
        self.inputValidaCpf.setObjectName("inputValidaCpf")
        self.gridLayout.addWidget(self.inputValidaCpf, 0, 1, 1, 1)
        self.btnValidaCpf = QtWidgets.QPushButton(self.centralwidget)
        self.btnValidaCpf.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        self.btnValidaCpf.setFont(font)
        self.btnValidaCpf.setObjectName("btnValidaCpf")
        self.gridLayout.addWidget(self.btnValidaCpf, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.btnGeraCpf = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        self.btnGeraCpf.setFont(font)
        self.btnGeraCpf.setObjectName("btnGeraCpf")
        self.gridLayout.addWidget(self.btnGeraCpf, 1, 2, 1, 1)
        self.labelRetorno = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelRetorno.setFont(font)
        self.labelRetorno.setStyleSheet("color: green")
        self.labelRetorno.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRetorno.setReadOnly(True)
        self.labelRetorno.setObjectName("labelRetorno")
        self.gridLayout.addWidget(self.labelRetorno, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Valida ou gera CPF"))
        self.label.setText(_translate("MainWindow", "Validar CPF:"))
        self.btnValidaCpf.setText(_translate("MainWindow", "VALIDAR"))
        self.label_2.setText(_translate("MainWindow", "Gerar CPF:"))
        self.btnGeraCpf.setText(_translate("MainWindow", "GERAR"))