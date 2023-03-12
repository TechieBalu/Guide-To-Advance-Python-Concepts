import pandas as pd

data = {"date": ["2018-01-01", "2018-02-01", "2019-01-01", "2019-02-01"],
        "temperature": [20, 25, 18, 22]}
df = pd.DataFrame(data)

# Extract year from date column
df["year"] = pd.DatetimeIndex(df["date"]).year

# Show the updated dataframe
print(df)