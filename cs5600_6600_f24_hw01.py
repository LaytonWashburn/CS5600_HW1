
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
        self.and_weights = np.array([0.51, 0.51])
        self.and_bias = 1
        self.or_weights = np.array([0.51, 0.51])
        self.or_bias = 0
        self.not_weights = np.array([1])
        self.not_bias = 1



    def output(self, x):
        ## your code here
        ### Or
        res = 0 # Variable to hold result of summation of dot products
        for i in range(0, len(x)):
            res += (x[i] * self.or_weights[i])
        or_res =  1 if res > (self.or_bias) else 0

        ### And 1
        res = 0 # Variable to hold result of summation of dot products
        for i in range(0, len(x)):
            res += (x[i] * self.and_weights[i])
        and_res =  np.array([1 if res > (self.and_bias) else 0])

        ### NOT
        res = 0 # Variable to hold result of summation of dot products
        for i in range(0, len(and_res)):
            res += (and_res[i] * self.not_weights[i])
        not_res = 1 if res < (self.not_bias) else 0

        ### Turn the results of two inputs into array
        final_res = np.array([or_res, not_res])

        ### AND 2
        res = 0 # Variable to hold result of summation of dot products
        for i in range(0, len(final_res)):
            res += (final_res[i] * self.and_weights[i])
        
        ### Return the results as an numpy array
        return  np.array([1 if res > (self.and_bias) else 0])


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
    
        





