import pandas as pd

if __name__ == '__main__':
    plik = input()
    df2=pd.read_csv(plik)
    result = df2['duration'].sum()
    print(result)