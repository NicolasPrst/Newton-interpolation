import matplotlib.pyplot as plt
from numpy import copy, linspace
from pip._vendor.distlib.compat import raw_input


def Get_Value():  #Function that get all the points of the function
    x_values = []
    y_values = []
    size = int(raw_input("Please enter the number of values of the function: "))
    for i in range(size):
        enter_x = raw_input("Please enter the value of x: ")
        enter_fx = raw_input("Please enter the value of f("+enter_x+"): ")
        x_values.append(float(enter_x))
        y_values.append(float(enter_fx))
    return(x_values, y_values)

def Coeff_Newton(x, y): #Function that calculate all the divided differnces coefficients
    size_x = len(x)
    cop_x = copy(x)
    coeff_list = copy(y)
    for j in range(1, size_x):
        coeff_list[j:size_x] = (coeff_list[j:size_x] - coeff_list[j - 1]) / (cop_x[j:size_x] - cop_x[j - 1])
        #Calculation of the formula (y(n) - y(n-1)) / (x(n) - x(n-1)) for each coefficient
    return (coeff_list)

def Interpol_Newton(x, y, X): #Function that calculate the Interpolation function
    Y = Coeff_Newton(x, y)
    size_x = len(x) - 1
    pi = Y[size_x]
    for k in range(1, size_x + 1):
        pi = Y[size_x - k] + (X - x[size_x - k]) * pi
        #Calculation of the interpolation polynome
    return (pi)


if __name__ == "__main__":  #Programm launch
    x_list, y_list = Get_Value()
    X = linspace(min(x_list), max(x_list), 200)
    Y = Interpol_Newton(x_list, y_list, X)

    #Print the graph of the programm
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(u'Newton Interpolation', fontsize=14)
    plt.plot(x_list, y_list, 'ro')  #Print the values in red
    plt.plot(X, Y, 'b')  #Print the function f' in blue that goes in each point
    plt.show()