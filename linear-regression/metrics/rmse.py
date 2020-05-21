import numpy as np


def rmse(predictions, actual):
    sum_squared_error = np.sum([(predictions[i] - actual[i])**2 for i in range(len(predictions))])
    return np.sqrt(sum_squared_error/len(predictions))
    


