"""
    Author: Ojelle Rogero
    Date Created: October 20, 2021
    Definition: Linear Regression exercise from Andrew Ng's MAachine Learning course. Octave/Matlab script replicated using Python
                This script can be used for both 1-variable and multi-variable
"""

import numpy as np
import pandas as pd

class LinearRegression():
    """Linear Regression for one variable and multiple variable"""

    def __init__(self, file, theta, alpha, iter, normalize):
        self.file = file
        df = self.readData()
        self.X = df.iloc[:, 0:len(df.columns) - 1]
        self.y = df.iloc[:, len(df.columns) - 1]
        self.m = len(self.X)
        self.theta = theta
        self.alpha = alpha
        self.itr = iter
        self.norm = normalize

    def readData(self):
        df = pd.read_excel(self.file, sheet_name='Sheet1')
        return df

    def costFunction(self, tht):
       X = self.X_data()
       hyp = X.dot(tht)
       J = np.sum(pow(hyp - self.y, 2)) / (2 * self.m)
       return J

    def gradientDescent(self):
        X = self.X_data()
        theta = self.theta

        for i in range(0, self.itr):
            hyp = X.dot(theta)
            dJ = np.multiply(X.T, hyp - self.y).T
            thetaUp = theta - ((self.alpha / self.m) * np.sum(dJ))
            theta = thetaUp
        return thetaUp

    def normalEqn(self):
        X = self.featureNormalize()
        a = np.linalg.pinv(X.T.dot(X))
        b = X.T.dot(self.y)
        theta = a.dot(b)
        return theta

    def X_data(self):
        if self.norm == 'no':
            XData = self.XOnes()
        elif self.norm == 'yes':
            XData = self.featureNormalize()
        return XData

    def XOnes(self):
        X = self.X
        if "X0" not in X:
            X.insert(0, "X0", np.ones(self.m))
        return X

    def minCostFunction(self, thetaUp):
        minJ = self.costFunction(thetaUp)
        return minJ

    def featureNormalize(self):
        X = self.X
        mu = np.mean(X)
        sigma = np.std(X)
        X_norm = (X - mu) / sigma
        X_norm.insert(0, "X0", np.ones(self.m))
        return X_norm

    def oneVar(self):
        calcTht = self.gradientDescent()
        minJ = self.minCostFunction(calcTht)
        print('\nLinear Regression with One Variable')
        print(f'Calculated theta = [{round(calcTht[0], 4)}, {round(calcTht[1], 4)}]')
        print(f'Where minimized cost function J = {round(minJ, 4)}')

    def multiVar(self):
        calcThtGD = self.gradientDescent()
        calcThtNE = self.normalEqn()
        minJGD = self.minCostFunction(calcThtGD)
        minJNE = self.minCostFunction(calcThtNE)
        print('\nLinear Regression with Multiple Variable')
        print(f'Calculated theta from Gradient Descent = [{round(calcThtGD[0], 4)}, {round(calcThtGD[1], 4)}, {round(calcThtGD[2], 4)}]')
        print(f'Gradient Descent: Minimized cost function = {round(minJGD, 4)}')
        print(f'Calculated theta from Normal Equation = [{round(calcThtNE[0], 4)}, {round(calcThtNE[1], 4)}, {round(calcThtNE[2], 4)}]')
        print(f'Gradient Descent: Minimized cost function = {round(minJNE, 4)}')


if __name__ == "__main__":
    file_ex1 = r'C:\Users\ojell\Desktop\Oj\3_Coursera\ML\exercises\ex_python\data_ex1a.xlsx'  # file directory
    linreg1 = LinearRegression(file_ex1, theta = [0, 0], alpha = 0.01, iter = 1500, normalize = 'no')
    linreg1.oneVar()

    file_ex2 = r'C:\Users\ojell\Desktop\Oj\3_Coursera\ML\exercises\ex_python\data_ex1b.xlsx'  # file directory
    linreg2 = LinearRegression(file_ex2, theta = [0, 0, 0], alpha = 0.01, iter=400, normalize = 'yes')
    linreg2.multiVar()