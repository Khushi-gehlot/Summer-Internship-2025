# #Dictionary - datatype to store values in key-value format
# #{} , sep by comma
# d = {1: "Python", 2: "Java", 3: "C++" , "Name": "Programming"}
# d[9] = "Ruby"
# print(d)
# print(type(d))
# print(d[3]) # d[key]
# #nested dict (key can be repeated in nested)
# d1 = {1: "shf" , 2: {1: "one ", 2: "two"}}
# print(d1[2])
# print(d1[2][1])
# print(d.values())
#
#
# # Delete an element in dict
# del(d[9])
# print(d)
# d.pop(2)
# d.popitem() #pops the last item
# d1.clear()
#
#
# d1 = d.copy()
#
# print(d.items()) #returns a list containing a tuple for each key
# print(d.keys()) #return list of keys
# d.update({1: "One"})
# d.update({2: "Two"})
# print(d)
# d2 = {7: "seven", 5: "Five"}
# d.update(d2)
# print(d)
from operator import index

# #TUPLES - ordered datatype
# t = (10, 20, 30, 40, 50)
# print(t)
# for x in t :
#     print(x)
# l = len(t)
# for x in range(l) :
#     print(t[x])
# t1 = (1,2,3)*3
# print(t1)
# #Slicing tuples'
# print(t[1:])
# print(t[:2])
#
# # tuple methods
# # min(), max(), len(), count(), index() sum()
# t3 = (2,5,7,34,12, 5)
# print(t3)
# print(min(t3))
# print(max(t3))
# print(sum(t3))
# print(t3.count(5))
# print(t3.index(5))
#
# #sets - unordered , unchangeable(remove and add possible) , unindexed, no duplicate values
# #written with {}
# # set1 = {"A", "B", "C", "D", "E", "F"}
# set1 = {1,2,3,4,5}
# print(set1)
# set1.add(6)
# print(set1)
# s2 = {1, 2,"a","b", 5}
# print(set1.union(s2))
# print(set1.intersection(s2))
# s3 = set()
# for i in range(3,9):
#     s3.add(i)
# print(s3)
# s4 = set1 & s2
# print(s4)
# def f1() :
#     print("Python")
# f1()
#
# def f2(a, b) :
#     c = a+ b
#     return c
# sum1 = f2(1, 2)
# print(sum1)
#
# def f3(name):
#     print("Hello", name)
# f3("Khushi")
# #use * for multiple nd uknown no of arguments
# def f4(*city):
#     print(city)
#     l = len(city)
#     print("Last city is: ", city[l-1])
#     print("First city is: ", city[0])
# f4("Ajmer", "Jaipur", "Kota")
# # use ** when unknown no of key words arguments

print("File Handling : ")
# f = open("f1.txt","w") #r for read w for write
# f.write("THIS IS A FILE")
# f.write("THIS IS Also the FILE")
# f.close()

# f = open("f1.txt","r")
# for x in f:
#     print(x, end="&")
# print()

with open("f1.txt","r") as f2:
    # data = f2.read()
    # print(data)
    # print()
    data = f2.readlines()
    for line in data:
        word = line.split()
        print("Word = ",word)


