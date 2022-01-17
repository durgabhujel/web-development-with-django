#Inheritance constructor overriding
#constructor # Constructor of the parent class is available in the child class.
# But if we write constructor in both classes, parent and child class then parent class constructor is not available to the child class.
#in this case only child class constructor is accessible which means child class constructor is replacing parent class constructor
#in this case only child class constructor is accessible which means child class class constructor replacing the value of parent class
# Calling Constructor of the parent class in the child class is called constructor overriding.
# Constructor with super() => super() is a function that is used to call the constructor of the parent class.

'''
class father:
    def __init__(self):
        self.money=1000
        print("father is a base class constructor")

    def show(self):
        print("father class instance method")

class son(father):
    def __init__(self):        #it is a child classs constructor
        self.money=6000
        self.car="bmw"

    def disp():
        print("son class is  instance methods")


p1=son()  
print(p1.money)   #print(self.money)  in this case child class constructor replace the parent class constructor 
print(p1.car)      


'''


class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)



#p1=person("Deepen",12345)#>it is simple calling method of constructor
#p1.display()
class Employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary   #we dont need a self.name and self.idnumber because it is child class of person class
        self.post=post
        # invoking the __init__ of the parent class
        #person.__init__(self, name, idnumber)   #it is use for pass the name and argument in child class 
                                                    #if we write this we don't needto write print(self.name and self.id num) and don,t need to write p1.display()
        # or using super()
        #super().__init__(name, idnumber)

    def display2(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)

    def __str__(self):
        return f'{self.name} {self.idnumber} {self.salary} {self.post}'






p1=Employee("Deepen",123,20000,"python Developer")
#p1.display()   
p1.display2() 
c=p1.__str__()
print(c)  #it s print Deepen 123 20000 python developer
print(type(c)) 


