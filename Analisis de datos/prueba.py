import pandas as pd
tabla = pd.read_csv("tested.csv")
print(tabla["Pclass"].value_counts(normalize=True, ascending=True))