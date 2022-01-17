#Inheritance constructor overriding
#in this case we write constructor in classes
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
        #person.__init__(self, name, idnumber)
        # or using super()
        super().__init__(name, idnumber)

    def display2(self):
        #print(self.name)
        #print(self.idnumber)
        print(self.salary)
        print(self.post)

    def __str__(self):
        return f'{self.name} {self.idnumber} {self.salary} {self.post}'






p1=Employee("Deepen",123,20000,"python Developer")
p1.display()   
p1.display2() 
c=p1.__str__()
print(c)
print(type(c))


