import numpy as np
import matplotlib.pyplot as plt
from metrics.rmse import rmse
from metrics.mae import mae
"""
Implementation of Linear Regression

y = b0 + b1*x

"""

#1. Estimating the coefficient

# Generate Mock Data
np.random.seed(42)
x = np.random.rand(100, 1)
y = 3*x + np.random.rand(100, 1)


# Generate Estimates

def generate_estimates(x_data, y_data):
    # b1 = sum([Xi - mean(X)]*[Yi - mean)(Y)])/sum((Xi - mean(Xi))^2)
    x = np.array(x_data)
    y = np.array(y_data)
    b1 = [np.sum((x[i] - np.mean(x))*(y[i] - np.mean(y)))/np.sum((x[i] - np.mean(x))**2) for i in range(len(x))]
    # b0 = mean(Y) - b1*mean(X)
    b0 = [np.mean(y[i]) - b1[i]*np.mean(x[i]) for i in range(len(x))]
    return np.mean(b0), np.mean(b1)

def mean(data):
    return np.sum(data)/len(data)

def variance(data, mean):
    squared_error = [(data[i] - mean)**2 for i in range(len(data))]
    sum_squared_error = np.sum(squared_error)
    return (sum_squared_error/(len(data) - 1))

def stdev(data, mean):
    return np.sqrt(variance(data, mean))

def cov(x, x_bar, y, y_bar):
    x_y_errors = [(x[i]-x_bar)*(y[i]-y_bar) for i in range(len(x))]
    sum_xy_errors = np.sum(x_y_errors)
    return sum_xy_errors/len(x)

def coef_estimator(x, y):
    b1 = (cov(x, np.mean(x), y, np.mean(y))/variance(x, np.mean(x)))
    b0 = np.mean(y) - b1*np.mean(x)
    return b0, b1


if __name__ == "__main__":
    x_bar, y_bar = mean(x), mean(y)
    b_naught, b_1 = coef_estimator(x, y)
    preds = [(b_naught + b_1*x[i]) for i in range(len(x))]
    print(rmse(preds, actual = y))
    print(mae(preds, y))
    plt.plot(x, preds)
    plt.plot(x, y, linestyle="none", marker=".")
    plt.show()

