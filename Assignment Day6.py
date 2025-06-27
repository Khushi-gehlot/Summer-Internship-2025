# # How to convert a series of date-strings to a timeseries?
import pandas as pd
date = pd.Series(["2025-12-02","2024-10-27","2024-11-01"])
timeSer = pd.to_datetime(date)
print(timeSer)
# #
# # Create two DataFrames, df1 and df2, with a common column (e.g., 'ID').
df1 = pd.DataFrame({
    "ID":[101,102,103,104,105],
    "Name":["A","B","C","D","E"],
    "Marks" : [98,97,79,85,90]
       })
df2 = pd.DataFrame({
    "ID":[102,103,106,107,108],
    "Name":["B","C","A","D","E"],
    "email":["mnp@653","qwe@567","bhf@978","sfs@345","abc@123"],
    "age": [22,27,18,20,25]
})
# #
# # Perform an inner merge on this common column and display the resulting DataFrame.
print(df1.merge(df2, how='inner', on='ID'))
# #
# # Perform a left join of df1 and df2 on the 'ID' column. Explain how missing values are handled in the resulting DataFrame. Right Join and Index-Based Join.
print(df1.merge(df2, how='left', on='ID'))
print(df1.merge(df2, how='right', on='ID'))
print(df1.join(df2, lsuffix='_left', rsuffix='_right'))
print("Missing values are handled in the resulting DataFrame by Nan ")
# #
# # Perform a right join using pd.merge() on a common column, then perform a join using df.join() based on the index. Compare the results. Merging with Multiple Keys.
print("By Merge with multiple keys - \n",df1.merge(df2, on=['ID','Name']))
print("By Join - \n",df1.join(df2, lsuffix='_left', rsuffix='_right'))
print("pd.merge() joins on columns (e.g., ID), while df.join() joins on index. Right join keeps all right-side rows. ")

# #
# # Create three DataFrames. Vertically concatenate two of them using pd.concat(), then merge the resulting DataFrame with the third DataFrame on a common key. Understand join() vs. merge().
f1 = pd.DataFrame({
    "ID":[101,102,103,104,105],
    "Name":["A","B","C","D","E"],
    "Marks" : [98,97,79,85,90]
       })
df2 = pd.DataFrame({
    "ID":[102,103,106,107,108],
    "Name":["B","C","A","D","E"],
    "email":["mnp@653","qwe@567","bhf@978","sfs@345","abc@123"],
    "age": [22,27,18,20,25]
})
df3 = pd.DataFrame({
    "Name":["B","C","A","D","E"],
    "Marks" : [98,97,79,85,90],
    "age": [22,27,18,20,25]
})
res = pd.concat([df1,df2],ignore_index=True)
res = pd.concat([res,df3], ignore_index=True)
print(res)