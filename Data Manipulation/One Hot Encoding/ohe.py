import pandas as pd

hour_df = pd.read_csv("hour_df.csv")
founders_df = pd.read_csv("founder_V0.3_founder.csv")

# first, generate unique list of values
def OneHotEncoding(data, col):
    """
    converts a column of categorical data into a one-hot-encoded group
    of columns
    @params: data, a pandas dataframe and col, the col to transform
    @returns: one-hot encoded group of columns
    """

    # set of unique categories within the column
    unique_categories = set(
        data[col]
    )
    # empty dataframe with categories converted to individual columns
    ohe_df = pd.DataFrame(
        columns = [category for category in unique_categories]
    )

    # fill each row in each column of the empty df with 1 or 0
    for i in list(ohe_df.columns):
        ohe_df[i] = [1 if val == i else 0 for val in data[col]]
    return ohe_df

if __name__ == "__main__":
    print(OneHotEncoding(founders_df, 'Headquarters Location '))
    print(OneHotEncoding(founders_df, 'Number of Founders'))
    print(OneHotEncoding(hour_df, 'hour'))