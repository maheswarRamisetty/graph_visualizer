import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, diff, sin, cos, tan, cot, sec, exp, lambdify
import re

class FunctionPlot:
    def __init__(self):
        pass
    
    def csc(self, x):
        return 1/sin(x)
    
    def preprocess_input(self, user_input):
        user_input = re.sub(r'(\d+)([a-zA-Z]+)', r'\1*\2', user_input)
        user_input = re.sub(r'(log)([a-zA-Z])', r'\1(\2)', user_input)
        return user_input

    def get_user_function(self,user_input):
        user_input = self.preprocess_input(user_input)
        return sympify(user_input)

    def plot_user_function(self, user_function, x_range=(-15, 15), num_points=1000):
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        y_range = (-10, 10) 
        try:
       
            f = lambdify('x', user_function, modules=['numpy'])
            f_derivative = lambdify('x', diff(user_function, 'x'), modules=['numpy'])


            y_values = f(x_values)
            y_values_derivative = f_derivative(x_values)

            plt.plot(x_values, y_values, label="Original Function: " + str(user_function))
            plt.plot(x_values, y_values_derivative, label="Derivative Function: " + str(diff(user_function, 'x')))

            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Function Plot')
            plt.legend()
            plt.grid(True)
            plt.xlim(x_range)
            plt.ylim(y_range)
            plt.axhline(0, color='black',linewidth=0.5)
            plt.axvline(0, color='black',linewidth=0.5)
            plt.show()
        except Exception as e:
            print("Error:", e)

