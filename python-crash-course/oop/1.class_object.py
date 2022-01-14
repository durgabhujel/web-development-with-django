#class is a user defined data type/structure
#class contains data member and member function
#data members are variable that are part of class also called attributes
#member function are function that are the part of class ,also called method

#object:-  object are instance of a class
#All the object of class share the same data and member function


#A single class can have multiple objects
#All the object of a class share the same data member and member 

""""

class syntax:
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
object creation:
object_name = ClassName()

"""

class car:
    #data member and attributes
    a='Bmw'
    b='audi'
    c='TATA'
     
    #member function and methods
    def Bmw(self):
        print(f'hello,i am {self.a}!')

    def audi(self):
        print(f'hello i am {self.b}!')    
  
    def TATA(self):
        print(f'hello, i am {self.c}!')
    def tesla(self): 
     print(f'hello, i am tesla')
obj1=car()  #it is a creating object or creation or instance creation
obj2=car()   #it is a second object creation it means a class have multiple object
c=obj1.Bmw()
print(c)   # if nothing retuen in function or method it is auto >return none 
obj1.audi()   # it means car.tesla(ob1)    it means called audi function of car class and passed the obj1
obj1.TATA()
obj1.tesla()
print(obj1.a)   # it direct show output of a variable
print(type(obj1))


         