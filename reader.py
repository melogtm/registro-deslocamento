import pandas as pd 


df = pd.read_csv('data.csv')

numEntradas = int(input())

print(df.head(numEntradas))
