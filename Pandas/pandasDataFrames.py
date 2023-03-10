import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'Gender': ['F', 'M', 'M', 'M', 'F'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
        'Salary': [50000, 60000, 70000, 80000, 90000]}



# Converting a dictionary into Pandas Dataframe.
dataset = pd.DataFrame(data)
print("1. Type of dataset variable is: ", type(dataset))

# * Printing head() of dataframe, head function will give us some top rows of the dataframe

# * Printing info() of dataframe, info function will give us the information about how many columns we have, 
# how many rows have null values in those columns, and,
# what is the datatype of each column

# * Printing shape of dataframe, it is attribute not a function, it gives us the rows and columns count (x,y)

# * Printing describe() of dataframe, this function gives the description about the numeric columns data frame like 
# 1. count of all non null values 
# 2. mean of numeric tables
# 3. standard deviations
# 4. median
# 5. min value of column
# 6. 25% of total values in that column
# 7. 50% of total values in that column
# 8. 75% of total values in that column
# 9. max value of column