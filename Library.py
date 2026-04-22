import pandas as pd
 
data = {
    "Product" : ["Laptop", "Phone", "Tablet", "Micro", "Keyboard", "Mouse"],
    "Price" : [50000, 60000, 20000, 50000, 20000, 70000],
    "Sales" : [10,20,15, 25, 30, 35]
}
df = pd.DataFrame(data)
print(df)
print(df.head(3))
print(df.info())
df["revenue"] = df ["Price"] * df ["Sales"]
print (df)
df.loc[len(df)] = ["laptop", 1000, 13, 1000*13]
Total_revenue = df["revenue"].sum()
print(Total_revenue)
df.loc[len(df)] = ["keybord1", 1000, 13, 1000*13]
Total_revenue = df["revenue"].sum()
print(Total_revenue)
print(df.loc[[0,1]])
df.loc[2,"sales"] = None
print(df)
df["Sales"] = df["Sales"].fillna(0)
high_value = df[df["Price"]> 1300]
print(high_value)

data1 = [
    ["Laptop", 50000, 10],
    ["Phone", None, 20],
    ["Tablet", 20000, 15]
]
df = pd.DataFrame(data, columns=["Product", "Price", "Sales"])
print(df)
df.fillna(0, inplace = True)
print(df)