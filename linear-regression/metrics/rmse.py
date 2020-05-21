import numpy as np
from sklearn.metrics import mean_squared_error

def rmse(predictions, actual):
    sum_squared_error = np.sum([(predictions[i] - actual[i])**2 for i in range(len(predictions))])
    return np.sqrt(sum_squared_error/len(predictions))
    


if __name__ == '__main__':
    preds = [1,2,3,4,5]
    actual = [2, 2, 4, 7, 5]
    print(rmse(preds, actual))
