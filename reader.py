import pandas as pd 

df = pd.read_csv('data.csv')

numEntradas = int(input("Informe quantas entradas você deseja visualizar: "))

print(df.head(numEntradas))
