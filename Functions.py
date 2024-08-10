#Functions:
'''create a sum() so it can take's 2 arguments to do sum'''
'''def sum(a,b):
    print(a+b)
a=int(input("enter the number"))
b=int(input("enter the number"))
sum(a,b)'''

#write a python function to sum all the numbers in a list.
#sample list :[8,2,3,0,7]
#expected output : 20
'''def sum(numbers):
    total = 0
    for x in numbers:
        total = total + x
    print(total)
numbers = [8,2,3,0,7]
sum(numbers)
'''
#write a function to multiply all the elements in a collections
'''def d1(numbers):
    total=1
    for x in numbers:
        total = total * x
    print(total)
numbers=[1,2,3,4]
d1(numbers)'''

#write a python function tp print even numbers from given list.
#sample test ---> [1,2,3,4,5,6,7,8,9]
#expected--> [2,3,6,8]

'''def d1(number):
    total =1
    for i in number:
        total=total+2
    print(total)
d1(number)'''

#write a function converts a decimal number into binary number
'''def dectobin(num):
    if num>1:
        dectobin(num//2)
    print(num%2, end="")
dectobin(11)
'''
#return()-->
'''sum = 10
def f1(x):
    return x + sum
print(f1(5))'''

"""Return:- special keyword that we can use inside a function or method(nothing but we can use in a function) to send the function results to the caller."""
'''len("hello")
type("hello")'''

'''def f1(x):
    print(x)
f1(10)'''
'''
def f2(x):
    return x
print(f2(10))'''

#what is the purpose of return?
"""when you return the value you can decide what you gonna do with value"""
#x= len(input("enter the string:"))
#print(x ** 2)

'''def f1(x):
    print(x)
print(f1(10))  #--> None'''
#why we are getting None?
""" when i use print(x) and given the argument f1(10) the 10 will gets to the f1(x) place and 1st prints the 10 """

'''def f1(x):
    return x
print(f1(10))'''

'''sum = 10
def fun_sum(x):
    return x+sum
print(fun_sum(100))'''

'''sum=10
def fun_sum(x):
    a = x+sum
    return a
print(fun_sum(100))'''

#write a program to print sum of range of numbers.
#sample input;- 7
#expected output:- 28

'''num = int(input("enter the number: "))
sum = 0
for i in range(0,num+1):
    sum=sum+i
print(sum)'''

'''num = int(input("enter the number: "))
sum=sum(range(1,num+1))
print(sum)'''



