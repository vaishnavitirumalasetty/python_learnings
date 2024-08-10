#lambda,filter,map

#lambda()
#what is lambda?
#lambda is an "anonymous function"
#"anonymous function' means this function doesn't have name.
'''def f1(x):
    return(x)
print(f1(10))'''
#syntax for lambda():- "lambda arguments:expression"
#so lambda is an anonymous it can have many arguments and single expression.
#what is an expression?
#expression is some kind of statement/calculation/step using that value to give single value
#Lambda is an anonymous function how can you call it.
#we generally use this function where it has some name.
#means we can create a variable to call this function.

'''x=lambda a: a+10
#where your calling the lambda function use the variable name
print(x(5))'''
'''x=lambda  a,b,c : a+b+c
print(x(5,6,7))'''
#when we can use lambda function?
#create function that can give square of every number?
'''def square(x):
    return x ** 2
def cube(x):
    return x ** 3j
def four(x):
    return x ** 4
def sqrt(x):
    return x ** 0.5
print(square(4))
print(cube(4))
print(four(4))
print(sqrt(4))'''

'''def power(n):
    return lambda a: a ** n
square = power(2)
cube = power(3)
print(square(6))
print(cube(3))'''
#simliaray try the lambda function for the multiplication.
#global and local variable
#what is global variable
#Global variable is a variable that can create outside the function
#you can access the global variable and it is a permanent''x="amazing"
'''def f():
    return x
print(f())'''
#what is local variable?
#creating variable inside the function is know as local variable.
'''def f():
    x ="fantastic"
    return x
print(f())
print(x)'''
""":- even the variable names are same the local varaiables never affect the global variables"""

#Map():
#what is iterables?
#list ,tuple,dict,set,array
#Map will take an function and run it over the iterables.
#Functions are the 1st class objects which means one function can act as an argument for another function
#Syntax :- Map = (function,iterables)
'''a = ['apples','banana','cherries','pineapple']
l=[]
for i in a:
    l.append(len(i))
print(l)
#do same thing LC
l=[len(i) for i in a]
print(l)'''
'''a = ['apples','banana','cherries','pineapple']
#if you want to display the output by using the map function we need to decide in which the output has tober
length = tuple(map(len,a))
print(length)'''

'''a = ['apples','banana','cherries','pineapple']
def f1(x):
    return "hello "  +  x
#print(f1("apples"))
#apply the function for each item in the collection.
l=list(map(f1,a))
print(l)'''
#when we have to use the map function?
#when we are having collection then we can use the
# user = input()
# print(user)
# print(type(user))
#i want to separatenthis value

# user = input().split()
# print(user)
# print(type(user))
#how to convert above thing in integer
# number = []
# for c in user:
#     number.append(int(c))
# print(number)
# print(type(number))

# user = input().split()
# number = tuple(map(int.user))
# print(number)
"""31.07.2024"""
#take a set of numbers being separated with the spaces
#if i want to separate this number
# user = input().split()
# print(user)
# print(type(user))

#how to convert this string of elements in list to integer?
"""user=input().split()
print(user)
print(type(user))
number=[]
for x in user:
    number.append(int(x))
print(number)
print(type(number))"""

# user = input().split()
# number = tuple(map(int,user))
# print(number)

# number=tuple(map(int,input().split()))
# print(number)
#note--- before executing the map() we need to decide in what type of collection,do we need the output.
#how can we print the following 10 20 30 40 50 in double that to in tuple?
#lambda -- you can have many arguments but single expression
# double= tuple(map(lambda a:a*2, number))
# print(double)

# double= tuple(map(lambda a:a*2,map(int,input().split())))
# print(double)
#map(int,input().split())---> map storing entire thing/data, if we want it to be in a readable need to add "tuple","list","set".
#===================================================================================================================================

"""filter()-->collectionk name(filter(function,iterable))
filter gives output of the collection if the condition is true"""
#age=[18,33,21,40,23,46,47,34,26,9,37]
"""def adult(x):
    if x>= 18:
        return x
f1=list(filter(adult,age))
print(f1)"""
# f1=list(filter(lambda a:a>=18,age))
# print(f1)
#how can i give more expression when i'm using conditional statement
#shall we use logical operators in lambda
# f1=list(filter(lambda a:a>=18 and a <=30,age))
# print(f1)
'''f1=list(filter(lambda a:18<=a<=30,age))
print(f1)'''

"""so fliters basically filters your original collection that returns true or false,
any value that comes out to be true the original value can be stored as a collection(list,tuple,set) of items"""

"""age=[18,33,21,40,23,46,12,14,26,9,37]
def adult(x):
    if x>= 18:
        return x
m1=list(map(adult,age))
print(m1)"""

#regular expression:- is a built in package which is known as "re"
#A RegEx, or regular expressions is a sequence of characters that forms a search patterns


# import re
# txt = "hello world!"
# #search weather world is present or not
# x=re.search("world!$",txt)
# print(x)
#regular expression function
#findall()-->returns a list containing all matches--->list
#search--> return match objects
#split-->returns a list
#sub--> replace one or many matches with the string



