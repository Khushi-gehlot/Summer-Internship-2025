# 1) Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data


import csv
data = [
["Name", "Address", "Mobile", "Email"],
["Khushi", "Ajmer", "902314829", "khushi@gmail.com"],
["Ananya", "Bihar", "824730342", "Ananya@gmail.com"],
["Vidushi", "Jaipur", "2374922753", "Vidushi@gmail.com"],
["Akshit", "SWM", "9837261583", "Akshit@gmail.com"]
]
with open("AddressBook.csv", "w") as file :
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)
#
# 2) Refer to our example of weather data and get more details. Display them
import requests

def weather(c):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={c}&appid=ccb979c831ab6f9cf4fdcb32b6514112"
    try:
        response = requests.get(url)
        data = response.json()
        humidity = data['main']['humidity']
        print(f"Temperature : {data['main']['temp']} Kelvin (Feels like: {data['main']['feels_like']}Kelvin)")
        print(f"Humidity : {humidity}%\nCountry = {data['sys']['country']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data : {e}")


weather(input("Enter City Name: "))

#
# 3) Practice DATABASE
# Create Database
# Create 2-3 tables
# Insert some records
# Perform different select operations
# Update some data
# Delete some data

import sqlite3
conn = sqlite3.connect("DB_assignment.db")
conn.execute('''
create table stud(
name varchar(20),
rollno integer primary key AUTOINCREMENT,
age integer ,
email varchar(30))
''')

conn.execute('insert into stud(name,age , email) values ("Ak", 20, "aks@gmail.com")')
conn.execute('insert into stud(name,age , email) values ("Bk", 18, "aks@gmail.com")')
conn.execute('insert into stud(name,age , email) values ("Ck", 19, "aks@gmail.com")')
conn.execute('insert into stud(name,age , email) values ("Dk", 22, "aks@gmail.com")')

data = conn.execute('Select * from stud')
for row in data :
    print(row)
id = input("Enter rolno = to delete: ") #TAKE ID IN STRING

conn.execute('Delete from stud where rollno ='+id)
conn.commit()

print("After deleting: ")
data = conn.execute('select * from stud')
for row in data:
    print(row)

conn.execute('Update stud set name = "khushi" where rollno = 3')
conn.commit()

conn.close()
