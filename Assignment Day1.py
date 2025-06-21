# 1)Write print function to print strings

str1 = ( "Python" )
print("String =", str1)
a=10
b=5
print(a+b)
print(f"The sum of {a} and {b} = {a+b}")


# 2) Write a python program that takes in a student name, class. It should also take in five subject marks of the
# students and find the total mark and percentage. Display a result in such a way that their name, class,
# and percentage are printed.

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



# 2) Simple basic Calculator Program

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print('''
    Enter choice: 
    1) Addition
    2) Subtraction
    3) Multiplication
    4) Division
    5) Modulus
    6) Exit''')
    ch = int(input("Enter choice: "))

    if ch == 1:
        print(a + b)
    elif ch == 2:
        print(a - b)
    elif ch == 3:
        print(a * b)
    elif ch == 4:
        print(a / b)
    elif ch == 5:
        print(a % b)
    elif ch == 6:
        break
    else:
        print("Invalid choice")




