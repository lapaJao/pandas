import pandas as pd

df = pd.read_csv("/content/datapacket/Gapminder.csv", error_bad_lines=False, sep=";")

df.head()

df = df.rename(columns={"country":"países", "continent":"continentes", "pop":"população"})

df.shape
