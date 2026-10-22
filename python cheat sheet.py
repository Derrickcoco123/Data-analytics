
import pandas as pd

data = {
    "Name": ["John", "Sarah", "Mike", "Anna", "David"],
    "Age": [25, 30, 22, 35, 28],
    "Money_Spent": [100, 250, 150, 300, 200]
}

df = pd.DataFrame(data)

#average money spent
average = df["Money_Spent"].mean()
print("Average money spent:", average)

#total money spent
total = df["Money_Spent"].sum()
print("Total money spent:", total)

#Sort customers by money spent, highest to lowest
sorted_data = df.sort_values(
    by="Money_Spent", ascending=False
)
print(sorted_data)
