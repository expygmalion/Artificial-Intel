import pandas as pd

df = pd.read_csv("car_sales - original.csv")
print(df)

Data = {"A": ['a', 'b', 'c', 'd'],"B":[1,2,3,4]}
df = pd.DataFrame(Data,  index = [1,2,3,4])

print(df)