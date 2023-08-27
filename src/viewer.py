from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget
#
#
# class Main(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Calculator')
#         self.resize(300, 500)
#         self.show()
#         self.setStyleSheet('QWidget {background: #333; font-size: 20px;}')
#
#         main_layout = QVBoxLayout()
#         button_layout = QGridLayout()
#
#         self.historyBox = QListWidget()
#         self.entryBox = QLineEdit()
#         self.entryBox.setStyleSheet('color:white;')
#
#         main_layout.addWidget(self.historyBox)
#         main_layout.addWidget(self.entryBox)
#
#         button1 = QPushButton(text='1', clicked=lambda:self.insertNum('1'))
#         button2 = QPushButton(text='2', clicked=lambda: self.insertNum('2'))
#         button3 = QPushButton(text='3', clicked=lambda: self.insertNum('3'))
#         button4 = QPushButton(text='4', clicked=lambda: self.insertNum('4'))
#         button5 = QPushButton(text='5', clicked=lambda: self.insertNum('5'))
#         button6 = QPushButton(text='6', clicked=lambda: self.insertNum('6'))
#         button7 = QPushButton(text='7', clicked=lambda: self.insertNum('7'))
#         button8 = QPushButton(text='8', clicked=lambda: self.insertNum('8'))
#         button9 = QPushButton(text='9', clicked=lambda: self.insertNum('9'))
#         button0 = QPushButton(text='0', clicked=lambda: self.insertNum('0'))
#
#         button_dot = QPushButton(text='.', clicked=lambda: self.insertNum('.'))
#         button_op = QPushButton(text='(', clicked=lambda: self.insertNum('('))
#         button_cp = QPushButton(text=')', clicked=lambda: self.insertNum(')'))
#
#         button_add = QPushButton(text='+', clicked=lambda: self.insertNum('+'))
#         button_sub = QPushButton(text='-', clicked=lambda: self.insertNum('-'))
#         button_mult = QPushButton(text='*', clicked=lambda: self.insertNum('*'))
#         button_div = QPushButton(text='/', clicked=lambda: self.insertNum('/'))
#         button_clear =QPushButton(text='C', clicked=self.clear_items)
#         button_calculate = QPushButton(text='=', clicked=self.calculate)
#
#         button_layout.addWidget(button1, 0, 0)
#         button_layout.addWidget(button1, 0, 0)
#         button_layout.addWidget(button2, 0, 1)
#         button_layout.addWidget(button3, 0, 2)
#         button_layout.addWidget(button4, 1, 0)
#         button_layout.addWidget(button5, 1, 1)
#         button_layout.addWidget(button6, 1, 2)
#         button_layout.addWidget(button7, 2, 0)
#         button_layout.addWidget(button8, 2, 1)
#         button_layout.addWidget(button9, 2, 2)
#         button_layout.addWidget(button0, 3, 0)
#         button_layout.addWidget(button_dot, 3, 1)
#         button_layout.addWidget(button_op, 4, 0)
#         button_layout.addWidget(button_cp, 4, 1)
#
#         button_layout.addWidget(button_add, 1, 3)
#         button_layout.addWidget(button_sub, 2, 3)
#         button_layout.addWidget(button_mult, 3, 3)
#         button_layout.addWidget(button_div, 3, 2)
#
#         button_layout.addWidget(button_clear, 0, 3)
#         button_layout.addWidget(button_calculate, 4, 2, 1, 2)
#
#         main_layout.addLayout(button_layout)
#         self.setLayout(main_layout)
#
#     def insertNum(self, num):
#         self.entryBox.insert(num)
#
#     def clear_items(self):
#         self.entryBox.clear()
#
#     def calculate(self):
#         items_to_calc = self.entryBox.text()
#         try:
#             if items_to_calc:
#                 items_to_calc = str(items_to_calc)
#                 res = eval(items_to_calc)
#                 self.entryBox.setText(str(res))
#                 self.historyBox.addItem(f"{items_to_calc}={res}")
#         except:
#             self.entryBox.setText('Incorrect expression')
#
#
#
#
# app = QApplication([])
# app.setStyle('fusion')
# main = Main()
# app.exec_()


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
        self.button_clear =QPushButton(text='C')
        self.button_calculate = QPushButton(text='=')

        self.button_layout.addWidget(self.button1, 0, 0)
        self.button_layout.addWidget(self.button1, 0, 0)
        self.button_layout.addWidget(self.button2, 0, 1)
        self.button_layout.addWidget(self.button3, 0, 2)
        self.button_layout.addWidget(self.button4, 1, 0)
        self.button_layout.addWidget(self.button5, 1, 1)
        self.button_layout.addWidget(self.button6, 1, 2)
        self.button_layout.addWidget(self.button7, 2, 0)
        self.button_layout.addWidget(self.button8, 2, 1)
        self.button_layout.addWidget(self.button9, 2, 2)
        self.button_layout.addWidget(self.button0, 3, 0)
        self.button_layout.addWidget(self.button_dot, 3, 1)
        self.button_layout.addWidget(self.button_op, 4, 0)
        self.button_layout.addWidget(self.button_cp, 4, 1)

        self.button_layout.addWidget(self.button_add, 1, 3)
        self.button_layout.addWidget(self.button_sub, 2, 3)
        self.button_layout.addWidget(self.button_mult, 3, 3)
        self.button_layout.addWidget(self.button_div, 3, 2)

        self.button_layout.addWidget(self.button_clear, 0, 3)
        self.button_layout.addWidget(self.button_calculate, 4, 2, 1, 2)

        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

    def set_button_callback(self, button, callback):
        button.clicked.connect(callback)

    def insert_text(self, text):
        self.entryBox.insert(text)

    def clear_entry(self):
        self.entryBox.clear()

    def get_expression(self):
        return self.entryBox.text()

    def set_result(self, result):
        self.entryBox.setText(result)
        self.historyBox.addItem(result)
