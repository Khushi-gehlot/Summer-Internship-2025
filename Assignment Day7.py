# 1) Explore more regex patterns
# 	Eg. The regex pattern used to validate email addresses, mobile no, string, and more
import re
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,3}$'
print(re.match(email_pattern, "user@example.com"))
mobile_pattern = r'^[6-9]\d{9}$'
print(re.match(mobile_pattern, "9876543210"))
alphanumeric_pattern = r'^[a-zA-Z0-9]{5,10}$'
print(re.match(alphanumeric_pattern, "abc123"))
date_pattern = r'^\d{2}-\d{2}-\d{4}$'
print(re.match(date_pattern, "26-06-2025"))
#

# 2) Explore more datetime function and uses in pandas
import pandas as pd

# Sample datetime data
data = {'date': ['2025-06-26', '2024-12-25', '2023-01-01']}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

# Extract datetime features
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()
df['is_weekend'] = df['date'].dt.weekday >= 5

print(df)
#
# 3) Import an meaningful csv file for data analysis and perform data cleaning, and analysis for meaningful output

df = pd.read_csv('titanic.csv')

# Show basic info
print(df.info())
print(df.describe())

# Data Cleaning
df.drop(columns=['Cabin'], inplace=True)  # Drop column with too many NaNs
df['Age'].fillna(df['Age'].median(), inplace=True)  # Fill missing age

# Analysis
survival_rate = df['Survived'].mean()
avg_fare = df['Fare'].mean()
avg_age = df['Age'].mean()

print(f"Survival Rate: {survival_rate*100:.2f}%")
print(f"Average Fare: ${avg_fare:.2f}")
print(f"Average Age: {avg_age:.2f}")

survival_by_class = df.groupby('Pclass')['Survived'].mean()
print("Survival Rate by Passenger Class:")
print(survival_by_class)
