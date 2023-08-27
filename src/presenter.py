from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget
from model import CalculatorModel
from viewer import CalculatorView


class CalculatorPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.set_button_callback(self.view.button1, lambda: self.view.insert_text('1'))
        self.view.set_button_callback(self.view.button2, lambda: self.view.insert_text('2'))
        self.view.set_button_callback(self.view.button3, lambda: self.view.insert_text('3'))
        self.view.set_button_callback(self.view.button4, lambda: self.view.insert_text('4'))
        self.view.set_button_callback(self.view.button5, lambda: self.view.insert_text('5'))
        self.view.set_button_callback(self.view.button6, lambda: self.view.insert_text('6'))
        self.view.set_button_callback(self.view.button7, lambda: self.view.insert_text('7'))
        self.view.set_button_callback(self.view.button8, lambda: self.view.insert_text('8'))
        self.view.set_button_callback(self.view.button9, lambda: self.view.insert_text('9'))
        self.view.set_button_callback(self.view.button0, lambda: self.view.insert_text('0'))

        self.view.set_button_callback(self.view.button_dot, lambda: self.view.insert_text('.'))
        self.view.set_button_callback(self.view.button_op, lambda: self.view.insert_text('('))
        self.view.set_button_callback(self.view.button_cp, lambda: self.view.insert_text(')'))

        self.view.set_button_callback(self.view.button_add, lambda: self.view.insert_text('+'))
        self.view.set_button_callback(self.view.button_sub, lambda: self.view.insert_text('-'))
        self.view.set_button_callback(self.view.button_mult, lambda: self.view.insert_text('*'))
        self.view.set_button_callback(self.view.button_div, lambda: self.view.insert_text('/'))
        self.view.set_button_callback(self.view.button_clear, self.view.clear_entry)
        self.view.set_button_callback(self.view.button_calculate, self.calculate)

    def calculate(self):
        expression = self.view.get_expression()
        try:
            if expression:
                result = self.model.calculate_expression(expression)
                self.view.set_result(f"{expression} = {result}")
        except:
            self.view.set_result('Incorrect expression')


app = QApplication([])
app.setStyle('fusion')

model = CalculatorModel()
view = CalculatorView()
presenter = CalculatorPresenter(model, view)

view.show()
app.exec_()
