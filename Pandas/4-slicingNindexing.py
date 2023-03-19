import numpy as np 
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Alice', "Mike","Alice", "Alice"],
        'Age': [25, 30, 35, 40, 45,25,30,90],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F","M","F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America","Chicago","Lahore"],
        'Salary': [60000, 60000, 70000, 80000, 95000,60000,60000,60000]}

dataset = pd.DataFrame(data)


# * Indexing of dataframe using the set_index method:
# You can move a column from the body of the DataFrame to the index. This is called "setting an index," 
# and it uses the set_index method. Notice that the output has changed slightly; 
# in particular, a quick visual clue that name is now in the index is that the 
# index values are left-aligned rather than right-aligned.
x = dataset.set_index(keys="Name")
print("\n1-Setting index of dataframe as Name:\n",x)
# Now we have set the index of dataframe as Name and whenever we apply the .loc attribute, it will be applied on the 
# Name column 

print("\n2-Apply loc attribute:\n" , x.loc["Alice"])
# I passed the "Alice" to the loc, it will show all the records in which the Name is "Alice" but
# if I give it "Houston" from the City column, Pandas will throw an  error that this KeyError : "Houston"


# We can reset the index by appling the rest_index() method 
x = x.reset_index()
print("\n3-Resetting the index:\n", x.reset_index())

print("\n4-Printing whole dataframe after resetting the index:\n",x)

# let's set the index again to continue our work:
x = dataset.set_index(keys="Name")

# we can alos drop the indexed column using the reset_index() function 
print("\n5-Dropping indexed column:\n", x.reset_index(drop=True))