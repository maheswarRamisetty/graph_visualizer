import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, diff, sin, cos, tan ,cot,sec
import re

class FunctionPlot:
    def __init__(self):
        pass
    
    def derv(self,x):
        return 1
    
    def csc(self, x):
        return 1/sin(x)
    
    def preprocess_input(self, user_input):
        user_input = re.sub(r'(\d+)([a-zA-Z]+)', r'\1*\2', user_input)
        user_input = re.sub(r'(sin|cos|tan|cot|sec|csc)([a-zA-Z])', r'\1(\2)', user_input)
        return user_input

    def get_user_function(self,user_input):
        user_input = self.preprocess_input(user_input)
        return sympify(user_input)

    def plot_user_function(self, user_function, x_range=(-15, 15), num_points=100):
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        y_range = (-10, 10) 
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
            plt.xlim(x_range)
            plt.ylim(y_range)
            plt.axhline(0, color='black',linewidth=0.5)
            plt.axvline(0, color='black',linewidth=0.5)
            plt.show()
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    plotter = FunctionPlot()
    user_function = plotter.get_user_function()
    plotter.plot_user_function(user_function)
