import math

class CalculatorModel:
    def calculate_expression(self, expression):
        try:
            expression = expression.replace('^', '**')

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
