import pandas as pd

data = pd.read_csv("data.csv")

sliced_data = data["Primary Fur Color"]

to_csv = sliced_data.value_counts()

to_csv.to_csv("output.csv")