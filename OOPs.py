#Classes and Objects
#why we are creating the classes and objects?


#how to create a class?
#use the keyword "Class"

"""class customer:
    pass
#object creation
c1=customer()
print(c1)"""

#what is __main__?
#is nothing but from which file the class is coming from--------parameter
# x="helo"
# print(dir(x))

"""Attributes:these are 2 types
1.class attribute-->comes from class and these attributes accessible by every objects (common attributes)
2.object attribute-->means unique attributes that can be appicable to particular object"""

"""class customer:
    #create class attributes--> creating a varaibles inside the class
    Bank_Name = "HFC Bank"
    Branch = "Mumbai"
    State = "Maharsthra"
    ISFC  = "HFC0000023"
#create a object
c1=customer()
c2=customer()
#how can an object access class attribute?
print(c1.Bank_Name)
print(c2.ISFC)"""

#create a methods for class customer
#what is method?
#methods can be created inside the class.
#methods are nothing but creating functions inside the class.



#create a class
class customer:
    #create class attributes--> creating a varaibles inside the class
    Bank_Name = "HFC Bank"
    Branch = "Mumbai"
    State = "Maharsthra"
    ISFC  = "HFC0000023"
    #before creating object attributes we need to initiate object attributed inside the class
    def __init__(self,name,age,intial_amount,acc_No):
        #what is __init__?
        #when you create an object by default it runs with init method--->initialisation method
        self.name = name
        self.age = age
        self.intial_amount = intial_amount
        self.acc_No = acc_No

    #creating the methods
    def welcome(self):
        print(f"hello {self.name} and welcome to {self.Bank_Name},{self.Branch}")
    def check_balance(self):
        print(f'your current balance is {self.intial_amount}')
    def deposit(self,amount):
        self.intial_amount += amount   #---> intial_amount =intial_amount + amount
        print(f"Trnsaction is completed."
              f"{amount} has been credited to your {self.acc_No}"
              f"The updated balance is {self.intial_amount}")
    def withdraw(self,amount):
        if amount <= self.intial_amount:
            self.intial_amount -= amount
            print(f"Trnsaction is completed."
                  f"{amount} has been deducted to your {self.acc_No}"
                  f"The updated balance is {self.intial_amount}")
        else:
            print("insufficient balance")
            self.check_balance()
# create a object
c1=customer("Python",28,10000,123456789)
c2=customer("vaishu",21,10000,234567801)
# how can we access the particular methods
# c1.welcome()
# c2.welcome()
# c1.deposit(10000)
c1.withdraw(20000)
c2.withdraw(5000)
# how can an object access class attribute?
# print(c1.Bank_Name)
# print(c2.ISFC)

# how can an object access object attributes
# print(c1.intial_amount)

# step1--> create an class-->customer-->bank
# step2-->created a object by using varaibles for ex--> c1=customer()
# step3-->creating class attributes inside the class -->these are common attributes
# step4-->how to access class attributes by particular object-->print(c1.Bank_Name)
# step5--->created methods inside the class which are nothing but functions inside class
""""ex--> welcome(),check_balance(),deposit(),withdraw()"""
# step6--->how to access particular method by particular object-->c1.welcome().c1.deposit()

# class
# object
# methods
# inheritance:- The child object can acquire all the properties and behaviour of parent object.
# polymorphism:-  One task can ba PERFORMED IN MANY WAYS
# Data Abstraction:- data abstraction and encapsulation both are like synonyms
# Encapsulation:-

# what is self?
# it is a extra parameter in the method defination
# class.method(object)
# self act as a pointer/ reference to access the objects

class tester:
    def __init__(self, id):
        self.id = str(id)
        id = "224"


temp = tester(12)
print(temp.id)





