import numpy as np
import math

def mae(x, y):
    sum_abs_error = np.sum(abs(np.array(x) - np.array(y)))
    return sum_abs_error/len(x)

    