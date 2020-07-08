import numpy as np
import pandas as pd

def mean(data, column):
    """
    Helper function to return the mean of the specified column.
    Returns the value of the mean.
    @params: data, the dataset and column, the column to calculate
    @returns: the value of the mean
    """
    cum_sum = sum(data[column])
    return cum_sum/len(data[column])

def stdDeviation(data, column):
    """
    Helper function to return the standard deviation of the
    specified column. Returns the value of the Standard Dev.
    @params: data, the dataset and column, the column to calculate
    the standard deviation of
    @returns: the value of the standard deviation
    """
    x_mean = mean(data, column)
    sum_squared_diff = sum([(val - x_mean)**2 for val in data[column]])
    return (sum_squared_diff/len(data[column]))**.5


def standardization(data, columns):
    """
    returns a dataset with the specified columns normalized.
    The equation for standardization is (x - mean)/(standard deviation)
    where mean is the mean value in the column and standard deviation is 
    the standard deviation in the column.
    @params: data, a dataset with columns, and columns, a list of columns
    to normalize. Even if only if one column is to be normalized, it must
    still be contained within a list -> ['column']
    @returns: the dataset with normalized columns
    """
    # loop through columns
    for i in range(len(columns)):
        # set x_min and x_max for current column
        x_mean = mean(data, columns[i])
        x_std = stdDeviation(data, columns[i])

        data[columns[i]] = data[columns[i]].apply(
            lambda x : (x - x_mean)/(x_std)
        )
    return data

if __name__ == '__main__':
    df = pd.read_csv('~/Desktop/heroku-classification-models/sql/esp8266readings1.csv')
    print(standardization(
        df,
        ['photoresistor', 'temperature', 'humidity']
    ))
    