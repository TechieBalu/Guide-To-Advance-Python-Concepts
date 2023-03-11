import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', "Mike"],
        'Age': [25, 30, 35, 40, 45,25],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America"],
        'Salary': [50000, 60000, 70000, 80000, 90000,55000]}

dataset = pd.DataFrame(data)

# *Sorting data frame
print("________________________________________________________________________________________")
print("\nSorted dataframe:\n", dataset.sort_values("Salary") )

# * Sorting in descending order
print("________________________________________________________________________________________")
print("\nSorted dataframe:\n", dataset.sort_values("Salary", ascending = False) )

#* Sorting on multiple colums 
print("________________________________________________________________________________________")
print("\nSorted dataframe:\n", dataset.sort_values(["City","Salary"], ascending = [False,True]) )

# * Taking column out of the dataframe
print("________________________________________________________________________________________")
print("\nColumn from the dataframe:\n",dataset["Name"])

# *Taking multiple columns
# ! we cannot take out multiple columns in single list, like below, we need to make it in 2D list
# print("\nMultiple Columns:\n", dataset["Name","Gender"])
print("________________________________________________________________________________________")
print("\nMultiple Columns:\n", dataset[["Name","Gender"]])

# # *Another way to selecting multiple colummns from the dataframe
# print("________________________________________________________________________________________")
# chunk = dataset["Name", "Gender"]
# print("\nAnother way:\n", dataset[chunk])

# *Applying conditions on the dataframes
# Let's say we want to get the row of dataframe where Name is "Mike"
print("________________________________________________________________________________________")
print("\nCondition on Columns where name is Mike\n",dataset[dataset["Name"] == "Mike"])

# We can do the same for the salary
print("________________________________________________________________________________________")
print("\nCondition on Columns salary name is > 55000\n", dataset[dataset["Salary"] > 55000])



# * We can get the boolean results on the specified conditions
print("________________________________________________________________________________________")
print("\nBOOLEAN RESULTS Condition on Columns salary name is > 55000\n",dataset["Salary"] > 55000)


# * AND and OR operators for boolean results: 
print("________________________________________________________________________________________")
print("\nBOOLEAN RESULTS Condition on Columns salary name is > 55000\n",(dataset["Gender"] == "M" ) & ((dataset["Salary"] > 55000 )) )



