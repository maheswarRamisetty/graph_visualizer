import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, diff
from Validators import MulValidaors
from Plotters import LinearPlotter
from Plotters import ExpoPlotter
from Plotters import TrigoPlotter
from Plotters import LogPlotter
import re
def preprocess_input(user_input):
    user_input = re.sub(r'(\d+)([a-zA-Z]+)', r'\1*\2', user_input)
    user_input = re.sub(r'log([a-zA-Z])', r'log(\1)', user_input)
    return user_input

def get_user_function():
    print("Enter function : ")
    user_input = input()
    user_input = preprocess_input(user_input)
    return sympify(user_input)

def plot_user_function(user_function, x_range=(-10, 10), num_points=1000):
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


if __name__ == "__main__":
    
    user=input("Enter Function : ")    
    fv=MulValidaors.FunctionValidator()
    type_user=fv.validate_function(user)
    print(type_user)
    if type_user=="linear":
        
        lp=LinearPlotter.LinearPlot()
        LinearPlotter.LinearPlot().plot_user_function(lp.get_user_function(user))
        
    elif type_user=="quadratic":
        
        lp=LinearPlotter.LinearPlot()
        LinearPlotter.LinearPlot().plot_user_function(lp.get_user_function(user))
        
    elif type_user=="cubic":
        
        lp=LinearPlotter.LinearPlot()
        LinearPlotter.LinearPlot().plot_user_function(lp.get_user_function(user))
        
    elif type_user=="exponential":
        
        ep=ExpoPlotter.FunctionPlot()
        ExpoPlotter.FunctionPlot().plot_user_function(ep.get_user_function(user))
    
    elif type_user=="trigonometric":
        
        tp=TrigoPlotter.FunctionPlot()
        TrigoPlotter.FunctionPlot().plot_user_function(tp.get_user_function(user))
        
    else:
        lp=LogPlotter.FunctionPlot()
        LogPlotter.FunctionPlot().plot_user_function(lp.get_user_function(user))
        