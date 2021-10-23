"""
    Author: Ojelle Rogero
    Date Created: July 21, 2021
    Date Finished: July 27, 2021
    Definition: Linear Regression exercise from Andrew Ng's MAachine Learning course. Octave/Matlab script replicated using Python
"""

import pandas as pd
import matplotlib.pyplot as plt

class Data():
    """Read txt data and create dataframe"""
    
    # Define properties/attributes
    def __init__(self):
        self.X_data = self.readData().loc[:, 'Profit']
        self.y_data = self.readData().loc[:, 'City Population']
    
    # Read data from the text file
    def readData(self):
        path = r'C:\Users\ojell\Desktop\Oj\3_Coursera\ML\exercises\ex1_linreg'
        df = pd.read_csv(path + r'\ex1data1.txt', header=None, names=['Profit', 'City Population'])
        return df    
    
class PlotData():
    
    # Define properties/attributes
    def __init__(self):
        input_data = Data()
        self.X = input_data.X_data
        self.y = input_data.y_data
    
    # Plot the data
    def plot(self):
        plt.plot(self.X, self.y, 'rx')
        plt.xlabel('City Population in 10,000')
        plt.ylabel('Profit in $10,000s')
        plt.title('City Population vs Profit')
        return plt
    
    # Plot h(x) which corresponds to the fitted model - linear regression
    def plotHyp(self, theta_up):
        y = theta_up[0] + theta_up[1] * self.X
        plt = self.plot()
        plt.plot(self.X, y, '-b')
        plt.legend(['Training Data', 'Linear Regression'])
        return plt
    

class linear_regression():    
    """Linear Regression with 1 Feature"""
    
    # Define properties/attributes
    def __init__(self):
        input_data = Data()
        self.X = input_data.X_data
        self.y = input_data.y_data
        self.m = len(self.X)

    # Hypothesis h(x)
    def hypothesis(self, theta):
        h = theta[0] + theta[1] * self.X
        return h

    # Cost function J(theta)
    def costFunction(self, theta):
        m = self.m
        temp = 0
        for i in range(0, m):
            temp += pow((theta[0] + theta[1] * self.X[i]) - self.y[i], 2)
        
        J = temp / (2 * m)
        return J
    
    # Update theta values
    def thetaUpdate(self, theta):
        m = self.m
        tmp0, tmp1, temp0, temp1 = 0, 0, 0, 0
        for i in range(0, m):
            tmp0 += (theta[0] + theta[1] * self.X[i]) - self.y[i]
            tmp1 += ((theta[0] + theta[1] * self.X[i]) - self.y[i]) * self.X[i]
        temp0 = theta[0] - ((alpha / m) * tmp0)
        temp1 = theta[1] - ((alpha / m) * tmp1)
        theta_up = [temp0, temp1]
    
        return theta_up
    
    # Gradient descent calculates the updated J(theta) from the updated theta for each iteration
    def gradientDescent(self, theta, iters):
        for itr in range(0, iters):
            thetaUp = self.thetaUpdate(theta)            
            J_up = self.costFunction(thetaUp)
            theta = thetaUp
            
        return J_up, theta


if __name__ == "__main__":
    
    # Plot the Data
    pltData = PlotData()
    plot = pltData.plot()
    plot.show()
    
    # Calculate cost function and Gradient Descent
    theta = [0, 0]
    alpha = 0.01
    iterations = 1500
    linreg = linear_regression()
    costF1 = linreg.costFunction(theta)
    costF2 = linreg.costFunction([-1, 2])
    min_J = linreg.gradientDescent(theta, iterations)[0]
    theta_updated = linreg.gradientDescent(theta, iterations)[1]
    print(f"With theta = {theta}\nComputed cost function J = {round(costF1, 2)}\n")
    print(f"With theta = {[-1, 2]}\nComputed cost function J = {round(costF2, 2)}\n")
    print(f"The minimized cost function J is equal to {round(min_J, 2)}")
    print(f"With calculated theta = {[round(i, 4) for i in theta_updated]}\n")

    # Plot the Data with the model (which is the h = theta_updated[0] + theta_updated[1] * x)
    plt_h = pltData.plotHyp(theta_updated)
    plt_h.show()
    
    # Predict values using the updated theta values
    print("Predict values for population sizes of 35,000 and 70,000")
    predict1 = theta_updated[0] + theta_updated[1] * 3.5
    predict2 = theta_updated[0] + theta_updated[1] * 7
    print(f"For population = 35,000, the predicted profit is {round(predict1*10000, 4)}")
    print(f"For population = 70,000, the predicted profit is {round(predict2*10000, 4)}")