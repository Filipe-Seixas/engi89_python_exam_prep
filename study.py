# W3Schools - https://www.w3schools.com/python/exercise.asp?filename=exercise_syntax1

# Create a list 1-5 and iterate through it
mlist = [1, 2, 3, 4, 5]
for x in mlist:
    print(x)
# Print the 3rd number
print(mlist[2])
# Print list backwards
print(mlist[::-1])
# Create a dictionary with key value firstname and lastname
mydict = {"firstname": "Filipe", "lastname": "Silva"}
# Add a key to it
mydict["color"] = "red"
print(mydict)
# Print value of lastname
print(mydict["lastname"])
# Create a class called student, initialise the class and create an object of the class
class Student:
    def __init__(self, name):
        self.name = name

std = Student("Filipe")
print(std.name)
# Use super() in a class
class Advanced(Student):
    def __init__(self):
        super().__init__()

# Do an if statement
if std == True:
    print("Hello")
else:
    print("Yes")
# Do a while and for loop
y = "HELLO WORLD"
while y == "HELLO WORLD":
    for x in y:
        print(x)
        continue
    break

# select the correct syntax for method/function
# 1- definition job():
# 2- def job(): ****************
# 3- method job():
# 4- python function:
#
# select the correct syntax for INHERTING a class
# 1 - Parent_Class person:
# 2 - class child_class (Parent_Class): ****************
# 3 - class child_class person(parent_class)
# 4 - class child_class person(parentclass)
#
# what is tuple and list the syntax of them as well as the difference between them
# - A tuple is a data type in python used to store collections of data. Syntax: mytuple = ("item1", "item2", "item3")
# - A list is a data type in python used to store collections of data. Syntax: mylist = ["item1", "item2", "item3"]
# - A list is mutable, meaning the data inside can be changed, while a tuple is immutable
# - They are also both ordered

# what is the difference between function and method
# - A method is like a function, except it is attached to an object.
# - A method may alter an object’s state, but a function usually only operates on it, and then prints something
# - or returns a value.

# built in methods - dict = [4,5,6,7,8] - add a 5 at the end of this list - indexing
ldict = [4, 5, 6, 7, 8]
ldict.append(5)
print(ldict)

# declare 4 methods that take 4 arguments - no class is needed - specific functionality - method to return % of the 2
# values give
def first(a, b, c, d):
    return a % b

def second(e, f, g, h):
    return (e * 100) / f

def third(i, j, k, l):
    pass

def fourth(m, n, o, p):
    pass

print(first(45, 13, 3, 3))
print(second(5, 200, 6, 6))