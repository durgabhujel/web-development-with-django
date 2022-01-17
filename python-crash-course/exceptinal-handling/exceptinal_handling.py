#Exceptional handling

# The try statement lets you test a block of code for errors.
# The except statement lets you handle the error.
# Different types of errors are
# Errors:
# SyntaxError: Raised when there is a syntax error in Python code
# NameError: Raised when a variable is not found
# TypeError: Raised when a variable is used incorrectly
# ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero
# IndexError: Raised when an index of a sequence is out of range
# KeyError: Raised when a key is not found in a dictionary
# AttributeError: Raised when an attribute that doesn't exist is accessed
# ImportError: Raised when an import statement fails
# ModuleNotFoundError: Raised when a module is not found
# FileNotFoundError: Raised when a file is not found
# ValueError: Raised when a variable is assigned a value that has an inappropriate type
# AssertionError: Raised when an assert statement fails
# EOFError: Raised when the input() function hits an EOF
# KeyboardInterrupt: Raised when the user hits the interrupt key (normally Ctrl+C or Ctrl+D) during input()
# IndentationError: Raised when the Python code is not properly indented
# TabError: Raised when the wrong number of tabs or spaces are used for indentation
# SystemError: Raised when the interpreter finds an internal problem, but cannot be specifically identified
# SystemExit: Raised when Python interpreter is quit by calling the sys.exit() function
# Warning: Raised when the interpreter encounters a possible problem
# DeprecationWarning: Raised when the interpreter encounters a deprecated feature



'''
try :
    #statements in try block
except :
    #executed when error in try block
'''

# a=5
# b=0
# print(a/b)



# try:
#     a=5
#     b=1
#     print(a/b)
# except:
#     print('Some error occurred.')

# print("Out of try except blocks.")




# try:
#     a=5
#     b='0'
#     print(a+b)
# except TypeError:
#     print('Unsupported operation')
# print ("Out of try except blocks")




# try:
#     a=5
#     b=0
#     print (a/b)
# except TypeError:
#     print('Unsupported operation')
# except ZeroDivisionError:
#     print ('Division by zero not allowed')

# print ('Out of try except blocks')


'''
try:
    #statements in try block
except:
    #executed when error in try block
else:
    #executed if try block is error-free
finally:
    #executed irrespective of exception occured or not
'''



# try:
#     print('try block')
#     x=int(input('Enter a number: '))
#     y=int(input('Enter another number: '))
#     z=x/y
# except ZeroDivisionError:
#     print("except ZeroDivisionError block")
#     print("Division by 0 not accepted")
# else:
#     print("else block")
#     print("Division = ", z)
# finally:
#     print("finally block")
#     x=0
#     y=0

# print("Out of try, except, else and finally blocks." )



# # raise an exception



try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
         raise ValueError(x)
except ValueError:
     print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")