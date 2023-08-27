class CalculatorModel:
    def calculate_expression(self, expression):
        try:
            result = eval(expression)
            return str(result)
        except ZeroDivisionError:
            return 'Division by zero'
        except:
            return 'Error'

