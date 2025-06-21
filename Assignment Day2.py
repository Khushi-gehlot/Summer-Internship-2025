# 1) Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class, and percentage are printed.

name = input("What is your name? ")
Class = int(input("What is your class? "))
print("Enter marks of 5 sub: ")
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100
print("Result : Name =", name, ", Class =", Class, ", Percentage =", percentage)

# 2)Input 2 strings, concatenate them and store in another variable and then perform generally used string methods on it like:lower(), upper(), title(), swapcase(), capitalize(), casefold(), center(), count(), endswith(), find(), isalnum(), isdigit(), isnumeric(), isspace(), replace()

str1 = input("Enter a string : ")
str2 = input("Enter a string : ")
str3 = str1+str2
print(str3.lower())
print(str3.upper())
print(str3.title())
print(str3.capitalize())
print(str3.count("a"))
print(str3.swapcase())
print(str3.center(8))
print(str3.endswith("a"))
print(str3.find("a"))
print(str3.isalnum())
print(str3.isnumeric())
print(str3.isalpha())
print(str3.isdigit())
print(str3.islower())
print(str3.replace("is", "isn't"))


#3) Do practise of the operators session
#Operators-
# 1. Arithmetic Operators
a = 20
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)
#2. Assignment Operator
a = b
a += b
a -= b
a *= b
a %= b
a /= b #a = a/b
a //= b #a = a//b
a **= b

#3. Comparison Operator
# == < > <= >= !=

#4. Logical Operator
# and or not is not
a = 4
if a is not b and a > b :
    print(a)
else:
    print("a is equal to b and a is greater than b")

st = "Python"
if "P" in st :
    print(st)

#boolean and or not
a = 10 #1010
b = 8 #1000
print(a & b) #1000
print(bin(a))
#print(oct(a))
#print(hex(a))
print(bin(b))
print(a & b)
print(a | b)




#4) In your last program where you find the total and percentage of a student's marks of 5 subject, find the grade of the student using conditional statement. Eg. grade 'A' if percentage is greator than or equals to 60, 'B' for  percentage is greator than or equals to 50 and less than 60,  'C' for  percentage is greator than or equals to 40 and less than 50,  'D' for  percentage is greator than or equals to 33 and less than 40, otherwise 'Fail'
per = int(input("Enter your percentage: "))
if per > 60 :
    print("Grade A")
elif per > 50:
    print("Grade B")
elif per > 40:
    print("Grade C")
elif per > 33:
    print("Grade D")
else :
    print("Fail")



#5) Input a number from user and find its factorial using for loop


fact = 1
num = int(input("Enter a number: "))
for i in range(1, num+1):
    fact *= i
print("Factorial = " , fact)



#6) Create a billing program using list. Program should have options to
# 1. Create Bill
# 2. Display Item Price and total bill amount
# 3. Display Total
# 4. Exit


print('''
Enter choice :
1. Create Bill
2. Display Item Price and total bill amount
3. Display Total
4. Exit
''')
l1 = []
while True:
    ch = int(input("Enter your choice: "))
    if ch == 1:
        bill = int(input("Enter your bill: "))
        l1.append(bill)
    elif ch == 2:
        total = 0
        for i in l1 :
            total += i
        print("Total: ", total)

    elif ch == 3:
        print(l1)
    elif ch == 4:
        break
    else :
        print("Invalid choice")

#
# 7) Write a  Python program to find the smallest number in a list.
# Write a  Python program to find the second greatest number in a list.
# Write a  Python program to find the second smallest number in a list.

l = [10,20,3,8,50,6]
smallest = l[0]
for i in l:
    if smallest < i :
        smallest = i
print(smallest)

largest = l[0]
for i in l:
    if i > largest:
        largest = i
second_largest = l[0]
for i in l:
    if i > second_largest and i != largest :
        second_largest = i
print(second_largest)

second_smallest = l[0]
for i in l:
    if i > second_smallest and i != smallest :
        second_smallest = i
print(second_smallest)


