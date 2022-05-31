import pandas as pd
df2=pd.read_csv('polaczenia_duze.csv')
result = df2['duration'].sum()
print(result)