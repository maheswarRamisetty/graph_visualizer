import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, diff
import re

class LinearPlot:
    def __init__(self):
        pass

    def preprocess_input(self, user_input):
        user_input = re.sub(r'(\d+)([a-zA-Z]+)', r'\1*\2', user_input)
        user_input = re.sub(r'log([a-zA-Z])', r'log(\1)', user_input)
        return user_input

    def get_user_function(self,user_input):
        user_input = self.preprocess_input(user_input)
        return sympify(user_input)

    def plot_user_function(self, user_function, x_range=(-10, 10), num_points=1000):
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        try:
            y_values = np.array([user_function.subs('x', x_val) for x_val in x_values], dtype=float)
            plt.plot(x_values, y_values, label="Original Function: " + str(user_function))
            user_function_derivative = diff(user_function, 'x')
            y_values_derivative = np.array([user_function_derivative.subs('x', x_val) for x_val in x_values], dtype=float)
            plt.plot(x_values, y_values_derivative, label="Derivative Function: " + str(user_function_derivative))

            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Function Plot')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            print("Error:", e)

if __name__=="__main__":
    pass