import math
import sqlite3

class CalculatorModel:
    def calculate_expression(self, expression):
        try:
            if 'cos(' in expression:
                expression = expression.replace('cos(', 'math.cos(')
            if 'sin(' in expression:
                expression = expression.replace('sin(', 'math.sin(')
            if 'tan(' in expression:
                expression = expression.replace('tan(', 'math.tan(')
            if 'acos(' in expression:
                expression = expression.replace('acos(', 'math.acos(')
            if 'asin(' in expression:
                expression = expression.replace('asin(', 'math.asin(')
            if 'atan(' in expression:
                expression = expression.replace('atan(', 'math.atan(')
            if 'sqrt(' in expression:
                expression = expression.replace('sqrt(', 'math.sqrt(')
            if 'ln(' in expression:
                expression = expression.replace('ln(', 'math.log(')
            if 'log(' in expression:
                expression = expression.replace('log(', 'math.log10(')

            result = eval(expression)
            return str(result)
        except ZeroDivisionError:
            return 'Division by zero'
        except:
            return 'Error'

    def add_record_to_db(self, expression, result):
        with sqlite3.connect('calculator.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO `history` (expression, result) VALUES (?, ?)"
            cursor.execute(query, (expression, result))
            conn.commit()

    def load_history_db(self):
        with sqlite3.connect('calculator.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT expression, result FROM `history`")
            history_records = cursor.fetchall()
            return history_records


    def init_db(self):
        with sqlite3.connect('calculator.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `history` (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                expression VARCHAR(255),
                result VARCHAR
                );
            """)
