# Constructor, __init__, Class Variables, Instance Variables, __str__
# Construcor is a special method that is called when an object is created.
# It is used to initialize the state of the object.

# Class variable is a variable that is shared by all the objects of a class.
# Class variable is accessible by all the objects of the class.
# Class variable is not a part of the object.
# Class variable is also known as static variable.

# Instance variables are variables whose value is assigned inside a constructor or method with self
# Instance variables are accessible by all the objects of the class.
# Instance variable is a part of the object.
# Instance variable is not shared by all the objects of the class.

#__str__ is a special method that is called when an object is converted to a string.
# It is used to return a string representation of the object.
'''
class vehicle():     #class
       def __init__(self,name,model):    
         self.name=name
         self.model= model

p1=vehicle('hundai','i10')
print(p1.name)
print(p1.model)
'''


#oject method
'''
class vehicle:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("hello im "+ self.color)

p1 =vehicle("hundai", "red")
p1.myfunc()
'''

class Vehicle:
    # Class Variable
    Vehicle_type = 'Car'

    # The init method or constructor
    def __init__(self, company):   #self = Obj1 , company = "BMW"
        # Instance Variable
        self.company = company   # Obj1.company = "BMW"

    # Adds an instance variable
    def setColor(self, color):  # def setColor(obj1, "brown"):
        self.color = color  # Obj1.color = "brown"

    # Retrieves instance variable
    def getColor(self):	   # def getColor(Obj1):
        return self.color  # return Obj1.color

    def __str__(self):
        return f'{self.company} {self.Vehicle_type}'


# obj1 = Vehicle()  # object creation or instance creation
# obj1.setColor('red')  # Vehicle.setColor(obj1, "red")
Obj2=Vehicle('audi')
print(Obj2.company)


 

Obj1 = Vehicle("BMW")  #=> Vehicle.__init__(obj1, "BMW")
Obj1.setColor("brown")  #=> Vehicle.setColor(Obj1, "brown")
print(Obj1.company)

print(Obj1.getColor())  #=> Vehicle.getColor(Obj1)
print(Obj1.Vehicle_type)
#print(Obj1.vahicle)
# # accessing class variable using class name
# print(Vehicle.vehicle_type)  #=> "Ca     
r= Obj1.__str__()
print(r)
print(type(r))