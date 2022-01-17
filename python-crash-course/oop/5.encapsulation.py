# Encapsulation
# Public, private, protected access modifiers
#   - public: accessible from anywhere
#   - private: accessible only from inside the class 
#   - protected: accessible only from inside the class and from its subclasses but also can be accessed from outside the class but it a convention not to call protected methods from outside the class
#  -private: created using __ (two underscores) before the variable name
#  -protected: created using _ (one underscore) before the variable name



# class Student:
#     schoolName = 'Coursly Nepal' # class attribute

#     def __init__(self, name, age):
#         self.name=name # instance attribute
#         self.age=age # instance attribute



# std = Student("Yogesh", 20)
# print(std.schoolName)
# print(std.name)
# print(std.age)
# std.age = 21
# print(std.age)




# class Student:
#     _schoolName = 'Coursly Nepal' # protected class attribute
    
#     def __init__(self, name, age):
#         self._name=name  # protected instance attribute
#         self._age=age # protected instance attribute

# std = Student("Ujwal", 20)
# print(std._schoolName)
# print(std._name)
# std._age = 21
# print(std._age)




class Student:
    __schoolName = 'Coursly Nepal' # private class attribute

    def set(self, name, age):
        self.__name=name  # private instance attribute
        self.__age=age # private instance attribute

    def __display(self):  # private method
	    print('This is private method.')
    def display2(self):
        print(self.__name)
        print(self.__age)
        return self

std = Student()
std.set('dipen', 20)
#print(std.__schoolName)
#print(std.__name)
print(std.display2())

#name mangling
# print(std._Student__schoolName)