        s

        self.add_botao(QPushButton('9'), 1, 2, 1, 1)
        self.add_botao(QPushButton('÷'), 1, 3, 1, 1)
        self.add_botao(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #91C3F2; color: #fff; font-weight: 700;'
        )

        self.add_botao(QPushButton('4'), 2, 0, 1, 1)
        self.add_botao(QPushButton('5'), 2, 1, 1, 1)
        self.add_botao(QPushButton('6'), 2, 2, 1, 1)
        self.add_botao(QPushButton('*'), 2, 3, 1, 1)


        self.add_botao(QPushButton('1'), 3, 0, 1, 1)
        self.add_botao(QPushButton('2'), 3, 1, 1, 1)
        self.add_botao(QPushButton('3'), 3, 2, 1, 1)
        self.add_botao(QPushButton('-'), 3, 3, 1, 1)
        self.add_botao(
            QPushButton('⌫'), 3, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1],
            ),
            'background: #C091F2; color: #fff; font-weight: 700;'
        )

        self.add_botao(QPushButton('.'), 4, 0, 1, 1)
        self.add_botao(QPushButton('0'), 4, 1, 1, 1)
        self.add_botao(QPushButton(''), 4, 2, 1, 1)
        self.add_botao(QPushButton('+'), 4, 3, 1, 1)
        self.add_botao(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background: #F091F2; color: #fff; font-weight: 700;'
        )