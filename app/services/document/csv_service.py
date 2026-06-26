import pandas as pd

def read_csv(path):

    df = pd.read_csv(path)

    return df.to_string(index=False)