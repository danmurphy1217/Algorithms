import numpy as np
import matplotlib.pyplot as plt
"""
Implementation of Linear Regression

y = b0 + b1*x

"""

#1. Estimating the coefficient

# Generate Mock Data
np.random.seed(42)
x = np.arange(2500)
delta = np.random.uniform(-10, 10, size = (2500, ))
y = .4*x + delta + 3


# Generate Estimates

def generate_estimates(x_data, y_data):
    # b1 = sum([Xi - mean(X)]*[Yi - mean)(Y)])/sum((Xi - mean(Xi))^2)
    x = np.array(x_data)
    y = np.array(y_data)
    b1 = [np.sum((x[i] - np.mean(x))*(y[i] - np.mean(y)))/np.sum((x[i] - np.mean(x))**2) for i in range(len(x))]
    # b0 = mean(Y) - b1*mean(X)
    b0 = [np.mean(y[i]) - b1[i]*np.mean(x[i]) for i in range(len(x))]
    return np.mean(b0), np.mean(b1)




if __name__ == "__main__":
    print(generate_estimates(x, y))