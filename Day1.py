print('Hello World',"Welcome to Python", sep=',', end=" & ")
#end for the end of line, default end = /n
#sep for separation object ,default = " "
print(78 ,end=" END ")
print("Arithmetic operations")
print(8/3)
print(f"{8/3:.2F}")
#no of decimal places at xF
print(8//3)
print(67%3)
print("The sum of 8 and 6 = ", 8+6)
print("the product of 8 and 6", 8*6, sep=" = ")
print(5<10)
a=10
b=5
print(a+b)
print(f"The sum of {a} and {b} = {a+b}", sep="+")
#f = formatting and string formatting
print(f"sum of {a} & {b}", f"{a+b}", sep= " = ")

#INPUTS
#name = input("Enter your name: ")
#print(name)
#print("Enter your last name: ")
#last_name = input()
#print(last_name)

n = int(input("Enter any no: "))
#if not int() no will be saved as string (typecasting)
#no arithmetic operation can't be performed on strings
print(n)
print(n+1)

m = int(input("Enter any no: "))
print(m+n)



#VARIABLES
#containers that store data values
#start with letter or underscore
#no space in btw
#no. , alphabets, underscores can be used
#cases sensitive
#shouldn't be a python keyword like def if false raise none del import return elif in try , etc
#help("keywords")
help("keywords")

#typecasting
str = str(30)
integer_val = int(str)
float_val = float(str)

#get type of data
# type(variable_name)
print(type(str))
print(type(integer_val))


#print multiple
print('''
hi, python , welcome 
fhdso
''')
#memory address
#memory address is same for same value (variables can be diff)
print(id(str))

#String Concatenate
str1 = "Hello"
str2 = "World"
print(str1+str2)
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.capitalize())
print(str1.isupper())
print(str1.islower())
print(str1.isdigit())
print(str1.isnumeric())
print(str1.isalpha())
print(str1.isalnum())
print(str1.isspace())
print(str1.center(30))
print(str1.count("o"))
#startswith(sub, beg, end)
print(str1.startswith("h"))
print(str1.endswith("h"))

print(str1.expandtabs(40))
newstr = "785"
print(newstr.isnumeric())
s = "@"
s1 = (str1, "str2")
print(s.join(s1))
sb = "This is python"
print(sb.replace("is", "is great"))
sbnames = "Names:\nA\nB\nC"
print(sbnames.splitlines())
print(sb.split())
l = "tpions"
e = "123486"
enc = str.maketrans(l, e)
print(str.translate(enc))

