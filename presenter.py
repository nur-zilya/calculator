from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget
from model import CalculatorModel, init_db
from viewer import CalculatorView
import sqlite3

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
        self.view.set_button_callback(self.view.button_pow, lambda: self.view.insert_text('^'))

        self.view.set_button_callback(self.view.button_cos, lambda: self.view.insert_text('cos('))
        self.view.set_button_callback(self.view.button_sin, lambda: self.view.insert_text('sin('))
        self.view.set_button_callback(self.view.button_tan, lambda: self.view.insert_text('tan('))
        self.view.set_button_callback(self.view.button_acos, lambda: self.view.insert_text('acos('))
        self.view.set_button_callback(self.view.button_asin, lambda: self.view.insert_text('asin('))
        self.view.set_button_callback(self.view.button_atan, lambda: self.view.insert_text('atan('))
        self.view.set_button_callback(self.view.button_sqrt, lambda: self.view.insert_text('sqrt('))
        self.view.set_button_callback(self.view.button_ln, lambda: self.view.insert_text('ln('))
        self.view.set_button_callback(self.view.button_log, lambda: self.view.insert_text('log('))

        self.view.set_button_callback(self.view.button_clear, self.view.clear_entry)
        self.view.set_button_callback(self.view.button_calculate, self.calculate)

        self.view.set_button_callback(self.view.button_clear_history, self.view.clear_history_box)
        self.view.set_button_callback(self.view.button_load_history, self.load_hist)


    def calculate(self):
        expression = self.view.get_expression()
        try:
            if expression:
                if self.has_invalid_input(expression):
                    self.view.set_result('Input out of range for trigonometric functions')
                else:
                    result = self.model.calculate_expression(expression)
                    if not self.is_within_range(result):
                        self.view.set_result('Result is out of range')
                    else:
                        self.view.set_result(f"{expression} = {result}")
                        self.model.add_record_to_db(expression, result)
        except:
            self.view.set_result('Incorrect expression')

    def has_invalid_input(self, expression):
        trig_functions = ['cos', 'sin', 'tan', 'acos', 'asin', 'atan']
        for func in trig_functions:
            if func in expression:
                start = expression.find(func) + len(func)
                end = expression.find(')', start)
                if start != -1 and end != -1:
                    value = expression[start:end]
                    try:
                        value = float(value)
                        if not (-1000000 <= value <= 1000000):
                            return True
                    except ValueError:
                        return True
        return False

    def is_within_range(self, result):
        try:
            result_value = float(result)
            return -1000000 <= result_value <= 1000000
        except ValueError:
            return False

    def load_hist(self):
        records = self.model.load_history_db()
        for expression, result in records:
            view.historyBox.addItem(f"{expression} = {result}")


if __name__ == '__main__':
    init_db()
    app = QApplication([])
    app.setStyle('fusion')

    model = CalculatorModel()
    view = CalculatorView()
    presenter = CalculatorPresenter(model, view)

    # Load history from the database and populate the historyBox
    # with sqlite3.connect('calculator.db') as conn:
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT expression, result FROM history")
    #     history_records = cursor.fetchall()
    #     for record in history_records:
    #         expression, result = record
    #         view.historyBox.addItem(f"{expression} = {result}")

    view.show()
    app.exec_()
