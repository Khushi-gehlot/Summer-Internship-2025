import pandas as pd
# 1) Practise Pandas Series
#
# Create a Pandas Series from Dictionary

dt = {1: 43,2: 21, 3:86, 4:18, 5:60}
s = pd.Series(dt)
print(s)
#
# # Create a Pandas Series from Lists
l = [23,45,76,12,50]
s = pd.Series(l)
print(s)
# # Access the elements of a Series in Pandas
print(s[1]) #access sisngle element
print(s[[0,1,2]]) #access multiple elements
print(s[0:3])


#
# 2) DataFrames
#
# Make a Pandas DataFrame with a two-dimensional Python list
l1 = [['Name','RollNo','Marks'],["Harvey", '101', '98'], ["Mike", '102', '89'], ["Donna",' 103', '92'], ["Rachel", '104','79']]
df = pd.DataFrame(l1, index=['a','b','c','d','e'])
print(df)
# Create DataFrame from Python dict
dt = {"Name":["Harvey",'Mike','Donna','Rachel'], "Rollno": [101,102,103,104] , "Marks": [98,90,92,79],}
df = pd.DataFrame(dt)
print(df)
# Create Pandas dataframe using list of lists
l1 = [['Name','RollNo','Marks'],["Harvey", '101', '98'], ["Mike", '102', '89'], ["Donna",' 103', '92'], ["Rachel", '104','79']]
df = pd.DataFrame(l1, index=['a','b','c','d','e'])
print(df)

# Create a Pandas dataframe using list of tuples
l = [('Name','RollNo','Marks'),("Harvey", '101', '98'), ("Mike", '102', '89'), ("Donna",' 103', '92'), ("Rachel", '104','79')]
df = pd.DataFrame(l)
print(df)
# Create a Pandas DataFrame from List of Dicts
l= [
    {"Name": "Harvey", "RollNo": "101", "Marks": 98},
    {"Name": "Mike", "RollNo": "102", "Marks": 89},
    {"Name": "Donna", "RollNo": "103", "Marks": 92},
    {"Name": "Rachel", "RollNo": "104", "Marks": 79}
]
df = pd.DataFrame(l)
print(df)
#
# 3) Data iteration
#
# Different ways to iterate over rows in Pandas Dataframe
#
for row in df.index:
    print(df.iloc[row])

for row in df.index:
    print(df.loc[row])

# Selecting rows in pandas DataFrame based on conditions
GradeA = df[df['Marks'] > 90]
print("GradeA\n", GradeA)
failed = df[df['Marks'] < 80]
print("Failed - \n", failed)


# Select any row from a Dataframe using iloc[]
print(df.iloc[0,:])
# Limited rows selection with given column
print(df.iloc[1:3,1])
# Drop rows from the dataframe based on certain condition applied on a column
result = df[df["marks"] < 80]
print(result)

# Create a list from rows in Pandas dataframe
# for row in df.iterrows():
    # print(row.tolist())


#
