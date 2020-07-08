import pandas as pd

def normalization(data, columns):
    """
    returns a dataset with the specified columns normalized.
    The equation for normalization is (x - x_min)/(x_max - x_min)
    where x_min is the minimum in the column and x_max is the max
    in the column.
    @params: data, a dataset with columns, and columns, a list of columns
    to normalize. Even if only if one column is to be normalized, it must
    still be contained within a list -> ['column']
    @returns: the dataset with normalized columns
    """

    # loop through columns
    for i in range(len(columns)):
        # set x_min and x_max for current column
        x_min = min(data[columns[i]])
        x_max = max(data[columns[i]])

        data[columns[i]] = data[columns[i]].apply(
            lambda x : (x - x_min)/(x_max - x_min)
        )
    return data



if __name__ == '__main__':
   # test case
    df = pd.read_csv('~/Desktop/heroku-classification-models/sql/esp8266readings1.csv')
    normalization(
        df,
        ['photoresistor', 'temperature', 'humidity']
    )

    
     