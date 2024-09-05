
####################################################
# CS 5600/6600: F24: Assignment 1
# YOUR NAME
# YOUR A#
# Starter code for Assignment 1
#####################################################

import numpy as np

class and_percep:

    def __init__(self):
        ## your code here
        self.weights = np.array([0.51, 0.51])
        self.bias = 1

    def output(self, x):
        ## your code here
        # Loop through the nodes
        # Do the dot product
        res = 0 # Variable to hold result of summation of dot products
        for i in range(0, len(x)):
            res += (x[i] * self.weights[i])
        return 1 if res > (self.bias) else 0
           
class or_percep:
    
    def __init__(self):
        ## your code here
        self.weights = np.array([0.51, 0.51])
        self.bias = 0

    def output(self, x):
        ## your code here
        res = 0 # Variable to hold result of summation of dot products
        for i in range(0, len(x)):
            res += (x[i] * self.weights[i])
        return 1 if res > (self.bias) else 0


class not_percep:
    
    def __init__(self):
        ## your code here
        ## your code here
        self.weights = np.array([1])
        self.bias = 1

    def output(self, x):
        ## your code here
        ## your code here
        res = 0 # Variable to hold result of summation of dot products
        for i in range(0, len(x)):
            res += (x[i] * self.weights[i])
        return 1 if res < (self.bias) else 0


class xor_percep:
    
    def __init__(self):
        self.and_percep = and_percep()
        self.or_percep = or_percep()
        self.not_percep = not_percep()

    def output(self, x):
        ## your code here
        a = self.or_percep.output(x)
        b = self.and_percep.output(x)
        b = self.not_percep.output(np.array([b]))
        return self.and_percep.output(np.array([a,b]))

class xor_percep2:
    def __init__(self):
        ## your code here
        self.x1_weights = np.array([1.05, -1.05])
        self.x2_weights = np.array([-1.05, 1.05])
        self.x3_weights = np.array([1.05, 1.05])
        self.x1_bias = -1
        self.x2_bias = -1
        self.x3_bias = -1
        

    def output(self, x):
        ## your code here
        
        ## Perceptron 1
        res1 = x.dot(self.x1_weights) + self.x1_bias

        ## Perceptron 2
        res2 = x.dot(self.x2_weights) + self.x2_bias

        input_3 = np.array([1 if res1 > 0 else 0, 1 if res2 > 0 else 0])

        ## Perceptron 3
        res3 = input_3.dot(self.x3_weights) + self.x3_bias
        
        ### Return the results as an numpy array
        return  np.array([1 if res3 > 0 else 0])


class percep_net:
    
    def __init__(self):
        ## your code here
        self.and_percep = and_percep()
        self.or_percep = or_percep()
        self.not_precep = not_percep()

    def output(self, x):
        ## your code here
        or_res = self.or_percep.output(np.array([x[0],x[1]]))
        not_res = self.not_precep.output(np.array([x[2]]))
        and_res = self.and_percep.output(np.array([or_res, not_res]))
        return self.or_percep.output(np.array([and_res, x[3]]))
    
        





