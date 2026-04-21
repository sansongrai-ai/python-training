import pandas as pd

data1 = [
    ["Laptop", 50000, 10],
    ["Phone", None, 20],
    ["Tablet", 20000, 15]
]
df = pd.DataFrame(data1, columns=["Product", "Price", "Sales"])
print(df)
df = df.dropna()
print(df)