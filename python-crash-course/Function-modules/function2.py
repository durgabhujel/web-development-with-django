#import calculator    #we can also write from calculator import * (* means everything)
#from calculator import add,subtract # in this case we only import add and subtract from calculator
from calculator import *  # >in this case we canot need write module name like calcultor.
a=19
b=5

#r=calculator.add(a,b)
#r2=calculator.subtract(a,b)

r=add(a,b)
r2=subtract(a,b)

print(f"the result of adding {a} and {b} is in {r}")
print(f"the result of subtractis {a} and {b} is in {r2}")