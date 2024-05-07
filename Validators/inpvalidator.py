import sympy as sp

class FunctionAnalyzer:
    def __init__(self):
        self.x = sp.symbols('x')

    def function_type(self, expression):
        expression = expression.replace('x', '*x')
        if 'x' not in expression:
            return "Constant"
        
        try:
            expr = sp.sympify(expression)
        except sp.SympifyError:
            return "Invalid"
        if self.x not in expr.free_symbols:

            return "Constant"
        elif expr.is_polynomial(self.x):
            degree = sp.degree(expr, self.x)
            if degree == 1:
                return "Linear"
            elif degree == 2:
                return "Quadratic"
            elif degree == 3:
                return "Cubic"
            else:
                return f"Polynomial of degree {degree}"
        elif any(func_name in expression for func_name in ['sin', 'cos', 'tan', 'cot', 'cosec', 'sec']):
            return "Trigonometric"
        elif any(func_name in expression for func_name in ['exp', 'log']):
            return "Exponential or Logarithmic"
        else:
            return "Unknown"

if __name__ == "__main__":
    analyzer = FunctionAnalyzer()
    user_input = input("Enter a function in terms of 'x' (e.g., '2x', '2x+3', 'log(x)', 'sin(x)', etc.): ")
    print("Function type:", analyzer.function_type(user_input))


