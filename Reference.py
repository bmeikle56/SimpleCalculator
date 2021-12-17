#Quick documentary for reference

#the last printed expression is assigned to the variable _

#Strings can be in ' ' or in " "

#Strings can be concatenated (glued together) with the + operator
#and repeated with *: 3 * 'un' + 'ium' = 'unununium'

#String literals next to each other are automatically concatenated

#Strings can be indexed like in C --> word = 'Python', word[0] = 'Py='
#Indices can be negative, to start counting from the right
#so word[-6] = 'P, and word[-2] = 'o'
#Note that since -0 is the same as 0, negative indices start from -1
#-1 = end of list (or index = size-1)

#slicing allows you to obtain substring
#word[0:2] = "Py", word[2:5] = 'tho'

#Slice indices have useful defaults; an omitted first index defaults to zero
#an omitted second index defaults to the size of the string being sliced.
#word[:2] = 'Py', word[4:] = word[-2:] = 'on'

#Strings are immutable, so if you need to change one, create a new one

#len() returns length of String

#print('%(language)s has %(number)03d quote types.' %
#     {'language': "Python", "number": 2})

#List
#squares = [1, 4, 9, 16, 25]
#can be indexed and sliced
#support concatenation
#squares + [36, 49, 64, 81, 100]
#Lists are mutable

#append() adds to the end of a list

#len() returns length of List too

#Fibonacci sequence sample program
# a, b = 0, 1
#while a < 10:
#    print(a)
#    a, b = b, a+b

#User input
# x = int(input("Please enter an integer: "))

#if statement syntax
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

#For loop
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

#delete obj_name
# del obj_name

#class MyClass:
#   a = 10
#   def func(self):
#       print('Hello')

# deleting MyClass
#del MyClass

#range() function
#range(3) == [0, 1, 2]
# OR range([start], [stop], [step])

#sum() function
#sum(range(4)) --> 0 + 1 + 2 + 3 = 6

#Sample code for finding prime numbers from 2-9
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

#continue and break work as in Java

#pass
#pass can be used is as a place-holder for a function or conditional
#body when you are working on new code, allowing you to keep
#thinking at a more abstract level. The pass is silently ignored

#match is the same as switch in Java
# def http_error(status):
 #   match status:
 #       case 400:
 #           return "Bad request"
 #       case 404:
 #           return "Not found"
 #       case 418:
 #           return "I'm a teapot"
 #       case _:
 #           return "Something's wrong with the internet"

 #can combine some cases like:
 # case 401 | 403 | 404:
 #     return "Not allowed"

 #tuples and classes
 #class Point:
 #   x: int
 #   y: int


# __init__() function gets called whenever a new object of a class
# is instantiated --> constructor in Java

#class ComplexNumber:
#    def __init__(self, r, i):
#        self.real = r
#        self.imag = i

#    def get_data(self):
#        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
#num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
#num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
#num2 = ComplexNumber(5)
#num2.attr = 10

# Output: (5, 0, 10)
#print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
#print(num1.attr)

#Exceptions in Python
#try ... except block instead of try ... catch block in Java

