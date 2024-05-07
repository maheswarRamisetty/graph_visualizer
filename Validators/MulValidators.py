import re

class FunctionValidator:
    def __init__(self):
        self.function_types = {
            r'^\d+x$': 'Linear',
            r'^\d+x\s*[\+\-]\s*\d+$': 'Linear',
            r'^\d+x\^2$': 'Quadratic',
            r'^\d+x\^2\s*[\+\-]\s*\d+$': 'Quadratic',
            r'^e\^x$': 'Exponential',
            r'^\d+\*\w+\(x\)$': 'Trigonometric',
            r'^\w+\(x\)$': 'Trigonometric',
            r'^\w+\(x\)\s*[\+\-]\s*\d+$': 'Trigonometric',
            r'^\w+\(x\)\^2$': 'Trigonometric',
            r'^\w+\(x\)\^2\s*[\+\-]\s*\d+$': 'Trigonometric',
            r'^\d+\*\w+\(x\)\^2$': 'Trigonometric',
            r'^\d+\*\w+\(x\)\^2\s*[\+\-]\s*\d+$': 'Trigonometric',
            r'^\d+\*\w+\(x\)\s*[\+\-]\s*\d+$': 'Trigonometric',
            r'^\log\(\d+x\)$': 'Logarithmic',
            r'^\log\(\d+x\)\s*[\+\-]\s*\d+$': 'Logarithmic',
            r'^\log\(\d+\*\w+\(x\)\)$': 'Logarithmic',
            r'^\log\(\d+\*\w+\(x\)\)\s*[\+\-]\s*\d+$': 'Logarithmic',
            r'^\log\(\w+\(x\)\)$': 'Logarithmic',
            r'^\log\(\w+\(x\)\)\s*[\+\-]\s*\d+$': 'Logarithmic',
            r'^\log\(\d+x\)\s*[\+\-]\s*\w+\(x\)$': 'Invalid',
            r'^\log\(\d+\*\w+\(x\)\)\s*[\+\-]\s*\w+\(x\)$': 'Invalid'
        }
        self.patterns = {
            'linear': r'^\d*x\s*[\+\-]?\s*\d*$',
            'quadratic': r'^\d*x\^2\s*[\+\-]?\s*\d*x\s*[\+\-]?\s*\d*$',
            'cubic': r'^\d*x\^3\s*[\+\-]?\s*\d*x\^2\s*[\+\-]?\s*\d*x\s*[\+\-]?\s*\d*$',
            'trigonometric': r'^(\d+\*)?(sin|cos|tan)\(x\)\s*[\+\-]?\s*\d*$',
            'logarithmic': r'^log\(\d*x\)\s*[\+\-]?\s*\d*$',
            'exponential': r'^exp\^x\s*[\+\-]?\s*\d*$'
        }

    def validate_function(self, user_input):
        if 'x^3' in user_input:
            return 'cubic'
        if 'e' in user_input:
            return 'exponential'
        for func_type, pattern in self.patterns.items():
            if re.match(pattern, user_input):
                return func_type
        return "Invalid"

if __name__ == "__main__":
    pass
