import pandas as pd

data = {"date": ["2018-01-01", "2018-02-01", "2019-01-01", "2019-02-01"],
        "temperature": [20, 25, 18, 22]}
df = pd.DataFrame(data)


data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', "Mike"],
        'Age': [25, 30, 35, 40, 45,25],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America"],
        'Salary': [50000, 60000, 70000, 80000, 90000,55000]}

dataset = pd.DataFrame(data2)


# Extract year from date column
df["year"] = pd.DatetimeIndex(df["date"]).year

# Show the updated dataframe
print(df)



# * Taking mean of whole column
x = dataset["Salary"].mean()
print("\nMean of Salary is:\n", x)

# * Taking median of whole column
x = dataset["Salary"].median()
print("\nMedian of Salary is:\n", x)

# * Taking mode of whole column
x = dataset["Salary"].mode()
print("\nMode of Salary is:\n", x)

# * Taking sum of whole column
x = dataset["Salary"].sum()
print("\nSum of Salary is:\n", x)

# * Taking min of whole column
x = dataset["Salary"].min()
print("\nMin of Salary is:\n", x)

# * Taking max of whole column
x = dataset["Salary"].max()
print("\nMax of Salary is:\n", x)

# * Taking quantile of whole column
x = dataset["Salary"].quantile(.20)
print("\nQuantile of Salary is:\n", x)

# * Taking cumulativeSum of whole column
x = dataset["Salary"].cumsum()
print("\nCumulative Sum of Salary is:\n", x)

# * Taking Cumulative Product of whole column
x = dataset["Salary"].cumprod()
print("\nCumulative Product of Salary is:\n", x)

# * Taking cumulative Min of whole column
x = dataset["Salary"].cummin()
print("\nCumulative Min of Salary is:\n", x)

# * Taking cumulative Max of whole column
x = dataset["Salary"].cummax()
print("\nCumulative Max of Salary is:\n", x)




# TODO: ________________________________________________ agg() FUNCTION: _______________________________________________________________
# The aggregate, or agg, method allows you to compute custom summary statistics. 
# Here, we create a function called pct30 that computes the thirtieth percentile of a DataFrame column

def pct30(column):
    return column.quantile(0.3)

x = dataset["Salary"].agg(pct30)
print("\n Agg() function on salary column:\n",x)
# agg() function can also be use for multiple columns
x = dataset[["Age","Salary"]].agg(pct30)
print("\n Agg() function on multiple columns age and salary:\n",x)

