import pandas as pd

data = {"date": ["2018-01-01", "2018-02-01", "2019-01-01", "2019-02-01"],
        "temperature": [20, 25, 18, 22]}
df = pd.DataFrame(data)


data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Alice', "Mike","Alice"],
        'Age': [25, 30, 35, 40, 45,25,30],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F","M"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America","Chicago"],
        'Salary': [60000, 60000, 70000, 80000, 90000,55000,60000]}

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

def pct40(column):
    return column.quantile(0.4)

x = dataset["Salary"].agg(pct30)
print("\n Agg() function on salary column:\n",x)
# agg() function can also be use for multiple columns
x = dataset[["Age","Salary"]].agg(pct30)
print("\n Agg() function on multiple columns age and salary:\n",x)

# We can pass multiple functions to agg function as well 
x = dataset["Salary"].agg([pct40,pct30])
print("\n Agg() function can accept multiple functions: \n",x)

# TODO: need to be check
# ! agg function cannot accept multiple functions with mulitple columns 



# *Dropping duplicates: 
x = dataset["Salary"].drop_duplicates()
print("\n Dropped duplicate value of 60000 from the Salary Column:\n",x)

# * 2nd Syntax of dropping duplicates: 
# This syntax will return the whole dataset
print("\n 2nd syntax for Dropped duplicate value of 60000 from the Salary Column:\n", dataset.drop_duplicates(subset="Salary"))
# As you can see from the output that, There are 3 girls named with alice SO,
# We can also apply the dropduplicates on multiple columns
# Below syntax will drop the duplicat only where Name and Salary match in same record
# If name is Alice and Salary is 50000, and Name is Alice and Salary 60000, These are not duplicates 
# They have difference values for columns matched in the dropduplicates column
print("\n dropping duplicate from multiple columns Salary and Name:\n", dataset.drop_duplicates(subset=["Name","Salary"]))
x = dataset[["Name","Salary"]].drop_duplicates()
print("\n 2nd syntax od dropping multiple columns that are duplicates, and it will return only the those columns that we have mentioned for the dropping duplicates:\n",x)

# ____________________________________________________________________________________________________________
# *