import pandas as pd 
import numpy as np


data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', "Mike"],
        'Age': [25, 30, 35, 40, 45,25],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America"],
        'Salary': [50000, 60000, 70000, 80000, 90000,55000]}

dataset = pd.DataFrame(data)

# chunk = dataset["Name", "Age"]
# print(type(chunk))