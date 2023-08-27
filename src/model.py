import math

class CalculatorModel:
    def calculate_expression(self, expression, notation):
        try:
            if notation == "infix":
                postfix_expression = self.infix_to_postfix(expression)
                result = self.evaluate_postfix(postfix_expression)
            elif notation == "prefix":
                postfix_expression = self.prefix_to_postfix(expression)
                result = self.evaluate_postfix(postfix_expression)
            elif notation == "postfix":
                result = self.evaluate_postfix(expression)
            return str(result)
        except ZeroDivisionError:
            return 'Division by zero'
        except:
            return 'Error'

    def infix_to_postfix(self, infix_expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Operator precedence
        output = []
        operator_stack = []

        tokens = []
        current_token = ''
        for i, char in enumerate(infix_expression):
            if char.isnumeric() or char.isalpha() or char == '.':
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                if char.strip():
                    tokens.append(char)
        if current_token:
            tokens.append(current_token)

        for i, token in enumerate(tokens):
            if token == '-' and (i == 0 or tokens[i - 1] in "+-*/^("):
                # Handle unary minus
                output.append('0')  # Add a 0 before the unary minus
                operator_stack.append('-')
            elif token.isnumeric() or token.isalpha():
                output.append(token)
            elif token in precedence:
                while (
                        operator_stack
                        and operator_stack[-1] != '('
                        and precedence.get(operator_stack[-1], 0) >= precedence[token]
                ):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()

        while operator_stack:
            output.append(operator_stack.pop())

        return " ".join(output)

    def prefix_to_postfix(self, prefix_expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        output = []
        stack = []

        tokens = prefix_expression.split()[::-1]  # Reverse the prefix expression
        for i, token in enumerate(tokens):
            if token.isnumeric() or token.isalpha():
                output.append(token)
            elif token in precedence:
                while (
                        stack and stack[-1] != ')' and precedence.get(stack[-1], 0) >= precedence[token]
                ):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                while stack and stack[-1] != ')':
                    output.append(stack.pop())
                stack.pop()
            elif token == '-':
                if i == len(tokens) - 1 or tokens[i + 1] in "+-*/^(":
                    # Handle unary minus
                    stack.append('u-')
                else:
                    while stack and stack[-1] != ')' and precedence.get(stack[-1], 0) >= precedence[token]:
                        output.append(stack.pop())
                    stack.append(token)

        while stack:
            output.append(stack.pop())

        return " ".join(output)

    def evaluate_postfix(self, postfix_expression):
        stack = []

        for token in postfix_expression.split():
            if token.isnumeric():
                stack.append(float(token))
            elif token == 'u-':
                operand = stack.pop()
                stack.append(-operand)  # Perform unary negation
            elif token in "+-*/^":
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    stack.append(operand1 / operand2)
                elif token == '^':
                    stack.append(operand1 ** operand2)

        return stack[0]



