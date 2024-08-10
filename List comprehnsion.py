#List comprehnsion:-
"""" It offers you a smaller line of code that you can create a new list from the existing list."""
'''List_fruits = ["Apple","banana","pineapple","mango","kiwi"]
#print the fruits with letter "A" in it and store it in new list
new_list=[]
for i in List_fruits:
    if "A" in i:
        new_list.append(i)
print(new_list)'''

'''list_fruits = ["Apple","banana","pineapple","mango","kiwi"]
#new_list = [item(i) for items(i) in "collection name"]
new_list = [x for x in list_fruits if "e" in x]
print(new_list)'''

#print the new list without "Banana" from the existing list_fruits'''
'''list_fruits = ["Apple","Banana","pineapple","mango","kiwi"]
new_list = [x for x in list_fruits if  x != "Banana"]
print(new_list)'''

#create list of numbers from 0 to 20?
'''n=[]
for x in range(21):
    n.append(x)
print(n)'''

'''n=[x for x in range(21)]
print(n)'''

#from above if i want to even numbers in newlist then create new list with even number

'''n=[x for x in range(21) if x%2 == 0]
print(n)'''
#creste new list with odd numbers

'''n=[x for x in range(21) if x%2 != 0]
print(n)'''

#Note :- So LC can offer shorter syntax and also it is time eddicient.

#create a new list of numbers in the range of 20 the output must be in the multiple of 2.

'''n=[x*2 for x in range(21)]
print(n)'''

