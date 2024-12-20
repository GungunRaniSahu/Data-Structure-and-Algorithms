#Compiler Creater
class SimpleCompiler:
    def __init__(self):
        self.operators = {'+', '-', '*', '/'}
    
    def tokenize(self, expression):
        """Tokenizes the input string into numbers, operators, and parentheses."""
        tokens = []
        num = ''
        for char in expression:
            if char.isdigit() or char == '.':  # For numbers (including decimals)
                num += char
            else:
                if num:
                    tokens.append(float(num) if '.' in num else int(num))
                    num = ''
                if char in self.operators or char in "()":
                    tokens.append(char)
        if num:
            tokens.append(float(num) if '.' in num else int(num))
        return tokens

    def parse(self, tokens):
        """Parses the tokens and evaluates the expression."""
        def helper(index):
            stack = []
            num = 0
            op = '+'  # Default operator
            while index < len(tokens):
                token = tokens[index]
                if isinstance(token, (int, float)):  # If the token is a number
                    num = token
                elif token in self.operators:  # If the token is an operator
                    op = token
                elif token == '(':  # Handle parentheses
                    num, index = helper(index + 1)
                elif token == ')':  # End of a parenthesis
                    break

                # Perform operation when encountering an operator or at the end
                if token in self.operators or token == ')' or index == len(tokens) - 1:
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op == '*':
                        if stack:
                            stack[-1] *= num
                        else:
                            raise ValueError("Invalid expression: No operand for multiplication")
                    elif op == '/':
                        if stack:
                            stack[-1] /= num
                        else:
                            raise ValueError("Invalid expression: No operand for division")
                    num = 0

                index += 1

            return sum(stack), index

        result, _ = helper(0)
        return result

    def evaluate(self, expression):
        """Evaluates the given arithmetic expression."""
        tokens = self.tokenize(expression)
        return self.parse(tokens)
