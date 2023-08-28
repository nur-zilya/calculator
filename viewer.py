from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget

class CalculatorView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.resize(300, 500)
        self.setStyleSheet('QWidget {background: #333; font-size: 20px;}')

        self.main_layout = QVBoxLayout()
        self.button_layout = QGridLayout()

        self.historyBox = QListWidget()
        self.entryBox = QLineEdit()
        self.entryBox.setStyleSheet('color:white;')

        self.entryBox.setMaxLength(255)

        self.main_layout.addWidget(self.historyBox)
        self.main_layout.addWidget(self.entryBox)
        self.setLayout(self.main_layout)

        self.button1 = QPushButton(text='1')
        self.button2 = QPushButton(text='2')
        self. button3 = QPushButton(text='3')
        self.button4 = QPushButton(text='4')
        self.button5 = QPushButton(text='5')
        self.button6 = QPushButton(text='6')
        self.button7 = QPushButton(text='7')
        self.button8 = QPushButton(text='8')
        self.button9 = QPushButton(text='9')
        self.button0 = QPushButton(text='0')

        self.button_dot = QPushButton(text='.')
        self.button_op = QPushButton(text='(')
        self.button_cp = QPushButton(text=')')

        self.button_add = QPushButton(text='+')
        self.button_sub = QPushButton(text='-')
        self.button_mult = QPushButton(text='*')
        self.button_div = QPushButton(text='/')
        self.button_pow = QPushButton(text='^')

        self.button_cos = QPushButton(text='cos(x)')
        self.button_sin = QPushButton(text='sin(x)')
        self.button_tan = QPushButton(text='tan(x)')
        self.button_acos = QPushButton(text='acos(x)')
        self.button_asin = QPushButton(text='asin(x)')
        self.button_atan = QPushButton(text='atan(x)')
        self.button_sqrt = QPushButton(text='sqrt(x)')
        self.button_ln = QPushButton(text='ln(x)')
        self.button_log = QPushButton(text='log(x)')

        self.button_clear =QPushButton(text='C')
        self.button_calculate = QPushButton(text='=')

        self.button_clear_history = QPushButton(text='Clear History')
        self.button_load_history = QPushButton(text='Load History')

        self.button_layout.addWidget(self.button1, 1, 0)
        self.button_layout.addWidget(self.button2, 1, 1)
        self.button_layout.addWidget(self.button3, 1, 2)
        self.button_layout.addWidget(self.button4, 2, 0)
        self.button_layout.addWidget(self.button5, 2, 1)
        self.button_layout.addWidget(self.button6, 2, 2)
        self.button_layout.addWidget(self.button7, 3, 0)
        self.button_layout.addWidget(self.button8, 3, 1)
        self.button_layout.addWidget(self.button9, 3, 2)
        self.button_layout.addWidget(self.button0, 4, 1)

        self.button_layout.addWidget(self.button_dot, 4, 0)
        self.button_layout.addWidget(self.button_op, 5, 0)
        self.button_layout.addWidget(self.button_cp, 5, 1)
        self.button_layout.addWidget(self.button_pow, 5, 2)

        self.button_layout.addWidget(self.button_add, 1, 4)
        self.button_layout.addWidget(self.button_sub, 2, 4)
        self.button_layout.addWidget(self.button_mult, 3, 4)
        self.button_layout.addWidget(self.button_div, 4, 4)

        self.button_layout.addWidget(self.button_cos, 6, 0)
        self.button_layout.addWidget(self.button_sin, 6, 1)
        self.button_layout.addWidget(self.button_tan, 6, 2)
        self.button_layout.addWidget(self.button_acos, 7, 0)
        self.button_layout.addWidget(self.button_asin, 7, 1)
        self.button_layout.addWidget(self.button_atan, 7, 2)
        self.button_layout.addWidget(self.button_sqrt, 8, 0)
        self.button_layout.addWidget(self.button_ln, 8, 1)
        self.button_layout.addWidget(self.button_log, 8, 2)

        self.button_layout.addWidget(self.button_clear, 5, 4)
        self.button_layout.addWidget(self.button_calculate, 4, 2)

        self.button_layout.addWidget(self.button_clear_history, 6, 4)
        self.button_layout.addWidget(self.button_load_history, 7, 4)

        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

    def set_button_callback(self, button, callback):
        button.clicked.connect(callback)


    def insert_text(self, text):
        if text == '^':
            self.entryBox.insert('**')
        else:
            self.entryBox.insert(text)

    def clear_entry(self):
        self.entryBox.clear()

    def get_expression(self):
        return self.entryBox.text()

    def set_result(self, result):
        self.entryBox.setText(result)
        self.historyBox.addItem(result)

    def clear_history_box(self):
        self.historyBox.clear()

