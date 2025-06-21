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

#Conditional Statements
#n = int(input("Enter a number: "))
n = 98
if n == 0: print("Zero") #one line statement
elif n % 2 == 0:
    print("Even")
else :
    print("Odd")
#nested if else
if n != 0:
    if n % 2 == 0:
        print("Even")
    else :
        print("Odd")
else :
    print("Zero")

if n == 0 and n % 2 == 0 :
    print("Even")
elif n % 2 != 0 :
    print("Odd")
else :
    print("Zero")
per = 70
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

#a = int(input("Enter number"))
#b = int(input("Enter number"))
#op = input("Enter operation")
op = "-"
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '//':
    print(a // b)
elif op == '**':
    print(a ** b)
elif op == '%':
    print(a % b)
else :
    print("Invalid operation")


#ONE Line Statements
print("number is even") if n % 2 == 0 else print("number is odd")


#Loops in Python
for i in range(10) : #range(n) is a class that will generate no from 0 to less than n
    print(i)
#range(m,n) : m = start n = condition(end - 1)
#range(m, n, p) : m = start , n = condition(end - 1); p = step
print("loop with step ")
for i in range(1, 11, 2): print(i)
print("REVERSE LOOP")
for x in range(10,0, -1): print(x)
#pass = no operation
for x in range(1, 0, -1) :
    pass
    print("Python")
print("Half reverse Loop")
for x in range(1,10) :
    if x > 5 : print(10-x)
    else: print(x)
#use of break
print("Break Statement")
for x in range(1,10) :
    if x > 5 : break;
    print(x)
print("Continue statement")
for x in range(1,6) :
    if x == 3: continue;
    print(x)

for x in range(1,11, 2) :
    print(4, "*", x, "=", x*4)

print("NESTED Loops")
for i in range (2,5) :
    for j in range (1,11):
        print(i, "*", j, "=", j*i)

#1
#12
#123
#1234
for i in range(1,5,1):
    for j in range (1,i+1,1):
        print(j , end=" ")
    print()

print("WHILE LOOPS")
num = 1
while num <= 5:
    print(num)
    num += 1

# while True :
#     n = int(input("Enter a number (0 to Exit)"))
#     if n == 0:
#         break
#     print(n)

#String Indexing
str1 = "Pyhton Program"
print(str1[3])
print(str1[0:3])
print(str1[-3])
print(str1[-2:])
print(str1[:3])
print(str1[0::2])
print(str1[-1::-1]) #reverse
print(str1[-1:-10:-1])

#ord(): char to ascii
#char(): ascii to char

#list = store multiple ele in single variable
#list can contain int str and objects
#list are mutable
l = [10 , 20 , 30, 40 , 50]
print(l)
print(l[2])
print(type(l))
#mixed list
l2 = [3,6,7,"afe"]
print(l2)
#nested list
l3 = [3,6,7,"afe", [4,5,6]]
print(2*l)
l.reverse()
print(l)
#for loop of list
for x in l2 :
    print(x)

#split() splits a string into list where each alphabet is a list item separate by space
x = input("Enter elements: sep by space: ")
l4 = x.split()
print(l4)

print(l)
l.append(78)
print(l)
#we can also append a list into a list
l.append(l3)
print(l)
# l.insert() to insert element at desired pos
# l.extend() : add multiple elements at last like append does with single element
#extend can only take one argument if multiple add as list but the list2 if extended to list1 then elements of list2 becomes element of list1 but list2 doesnt become an element of list1

l.extend([45, 9])
print(l)

#removing element from last -
l.pop()
#removing element from a specific pos :
# l.pop(pos)
l.pop(2)

