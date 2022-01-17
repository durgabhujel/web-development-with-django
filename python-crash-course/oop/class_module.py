class Car:
    # data members/attributes:
    a = 'BMW'
    b = 'Audi'
    c = 'Mercedes'
    # members functions/methods:
    def bmw(self):
        print(f'Hello, I am a {self.a}!')
    def audi(self):
        print(f'Hello, I am a {self.b}!')
    def mercedes(self):
        print(f'Hello, I am a {self.c}!')
    def tesla(self):
        print(f'Hello, I am a Tesla!')

def add(a,b):
    return a+b