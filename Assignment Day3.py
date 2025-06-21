#1) Practise -Dictionary, Tuple, Set


d = {1: "Python", 2: "Java", 3: "C++" , "Name": "Programming"}
d[9] = "Ruby"
print(d)
print(type(d))
print(d[3]) # d[key]
#nested dict (key can be repeated in nested)
d1 = {1: "shf" , 2: {1: "one ", 2: "two"}}
print(d1[2])
print(d1[2][1])
print(d.values())


# Delete an element in dict
del(d[9])
print(d)
d.pop(2)
d.popitem() #pops the last item
d1.clear()


d1 = d.copy()

print(d.items()) #returns a list containing a tuple for each key
print(d.keys()) #return list of keys
d.update({1: "One"})
d.update({2: "Two"})
print(d)
d2 = {7: "seven", 5: "Five"}
d.update(d2)
print(d)

#TUPLES - ordered datatype
t = (10, 20, 30, 40, 50)
print(t)
for x in t :
    print(x)
l = len(t)
for x in range(l) :
    print(t[x])
t1 = (1,2,3)*3
print(t1)
#Slicing tuples'
print(t[1:])
print(t[:2])

# tuple methods
# min(), max(), len(), count(), index() sum()
t3 = (2,5,7,34,12, 5)
print(t3)
print(min(t3))
print(max(t3))
print(sum(t3))
print(t3.count(5))
print(t3.index(5))

#sets - unordered , unchangeable(remove and add possible) , unindexed, no duplicate values
#written with {}
set1 = {"A", "B", "C", "D", "E", "F"}
set1 = {1,2,3,4,5}
print(set1)
set1.add(6)
print(set1)
s2 = {1, 2,"a","b", 5}
print(set1.union(s2))
print(set1.intersection(s2))
s3 = set()
for i in range(3,9):
    s3.add(i)
print(s3)
s4 = set1 & s2
print(s4)



#2) Write a function for basic math operations like add multiply substract divide and use this in your program, take 2 number input from user.

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


#3) Write a program to check Palindrome Number
#
# The Number  which is equal to reverse number know as Palindrome Number.
#  For example Number 12321 is a Palindrome Number, because 12321 is equal to its reverse Number 12321.
# Steps for checking Palindrome number
# 1. Find reverse of the given number.
# 2. Compare that number with the reverse number.
# 3. If number and its reverse is equal then it is a Palindrome Number otherwise not.

n = int(input("Enter number to check if its palindrome or not: "))
temp = n
reverseN = 0
while temp > 0:
    rem = temp % 10
    reverseN = reverseN * 10 + rem
    temp = temp // 10
if n == reverseN:
    print("Palindrome")
else:
    print("Not Palindrome")