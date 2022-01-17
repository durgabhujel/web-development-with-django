#Inheritance is a way to create new classes based on existing classes
#IT is very reuse code .
#inheritance is the capability of one class 
#Inheritance is the mechanism of devriving a new class from and old class (existing class ) such as that the new class 
#>......inherit all the members (variable and methods)of old class is called inheritance
#inheritance is the capability one class to device or inherit the properties(data member/attributes and methods )
#>........from another class
#>All classes in python are built from a single super class called 'object' so when ever we create clas in python ,object will become super class for them internally 
# super class and base class:
#old class is refferred as super class and a new class is called sub class
#super class >=base class and parent class
#sub class>=child class and Derived class

class person:
    def __init__(self,name):
        self.name=name
        print("my name is deepen")
        
    def getName(self):
        return self.name
        
    def isEmpolyee(self):
        return False
        
#p1=person('ram')
#p1.getName() #store here "ram"
#print(p1.getName())        # it is a simple method to create object      
#p1.isEmpolyee()
#print(p1.isEmpolyee())

#Inherited or Sub class note base class in brackts

class Empolyee(person):               #base class or super clas most be in brackts 
    def isEmpolyee(self):
        return True

#p2=person("deepen")
#p2.getName() 
#print(p2.getName())
#p2.isEmpolyee()
#print(p2.isEmpolyee())

p2=Empolyee("deepen")
p2.getName()
p2.isEmpolyee()
print(p2.getName()) 
print(p2.isEmpolyee())       

