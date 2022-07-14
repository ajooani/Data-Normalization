import pandas as pd
import numpy as np


# Decimal scaling function
def dec_scale(data_df):
    for x in data_df:
        p = np.array(data_df[x].values.tolist())  # convert df data to array
        j = len(str(int(np.max(abs(p)))))   # get len(absolute max from each feature attribute)
        data_df[x] = data_df[x] / (10 ** j)  # Vi' = Vi/(10^j)


# Main
df = pd.read_csv('sample.csv')  # read data as dataframe
dec_scale(df)  # decimal scaling
np.savetxt("decimal_scaled_data.csv", df, delimiter=',', fmt='%s')  # write scaled data
