import pandas as pd


class linear_regression():
    """
       Author: Ojelle Rogero
       Date: July 21, 2021
       Definition: Linear Regression exercise from Andrew Ng's MAachine Learning course. Octave/Matlab script replicated using Python
    """
    
    
    # Define properties/attributes
    def __init__(self):
        self.data = r'C:\Users\ojell\Desktop\Oj\3_Coursera\ML\exercises\ex1_linreg\ex1data1.txt'
    
    # Define data file
    def read_data(self):
        df = pd.read_csv(self.data, header=None, names=['Profit', 'City Population'])
        X = df.iloc[:, 0]
        y = df.iloc[:, 1]
        theta = [0, 0]   # initialize theta value
        
        return print(len(X))
    
    # Define cost function
    def cost_function(self):
        J = 0
        for i in range(0, len(X)):
            J = J  # get back here
            
        pass
    
    
    # Define gradient descent

test = linear_regression()
test.read_data()