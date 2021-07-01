# 1. Declare a function called username that takes one argument as a string and return the name
def username(name1):
    return name1


print(username("Filipe"))

# 2. Declare a list with number 1 - 5. Iterate through the list and display the list

list_1 = [1, 2, 3, 4, 5]
for x in list_1:
    print(x)

# 3. AND - && & == Which one returns a bool value?
# ==

# 4. What is the difference between a list and a tuple?
# A list is mutable, and is defined with []
# A tuple is immutable, and is defined with ()

# 5. Can we add an element to a list? Yes.
#    Can we add an element to a tuple? No.
#    Can the element of tuple be different types? Yes.

# 6. Create a dictionary with key value firstname and lastname
dict = {'firstname': "Filipe", 'lastname': "Silva"}
print(type(dict))

# 7. Add a course key to dict
dict['course'] = 'devops'
print(dict)

# 8. Print value of lastname
print(dict['lastname'])

# 9. Create a class called student, initialise the class and create an object of the class
class Student:
    def __init__(self):
        pass


student = Student()

# 10. Create two functions that take two arguments each, function 1 called add_values, function 2 called subtract_values
# and return the addition and subtraction
def add_values(num1, num2):
    return num1 + num2


def subtract_values(num1, num2):
    return num1 - num2


print(add_values(2, 4))
print(subtract_values(4, 2))

# 11. Declare a dictionary with three shopping items with cost, eggs £1.20, milk £2.30, bread £1.00
#     Write a function that returns the total value
shopping = {"eggs": 1.2, "milk": 2.3, "bread": 1.0}


def total_value():
    return sum(shopping.values())


print(total_value())
#
# # OR
#
#
def total_value():
    return shopping["eggs"] + shopping["milk"] + shopping["bread"]


print(total_value())

# 12. Prompt the user to enter an integer, declare a function that checks if the number is odd or even and display back
# to the user with the message "The number is odd/The number is even"

num = input("Please enter an integer:  ")

def check_odd(num):
    if int(num) % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


check_odd(num)

# 13. select the correct syntax
# 1 -super.__init().
# 2- super()__init().
# 3 super().__init().
# 4 - super().__init__()
# super().__init__()

# 14. Declare a tuple with 3 values of your choice, iterate through the tuple and display the values

my_tuple = ("this", "is", 5)
for x in my_tuple:
    print(x)

# 15. Delete the last index of the tuple
# YOU CAN'T because they are immutable

# 16. Create a class called student with one method called student data that returns studentname
#     Create a class called DevOps student which inherits the Student class and print student name
class Student:
    def student_data(self):
        return "Filipe"

class DevOpsStudent(Student):
    def __init__(self):
        super().__init__()


ds = DevOpsStudent()
print(ds.student_data())

# 17. Declare a variable called city, declare a method that takes city as argument and value of the city as London and
# method check if value is London, then true or false

city = "London"


def check_city_name(city1):
    if city1 == "London":
        return True
    else:
        return False


print(check_city_name(city))

# 18. import sys module, import math and with math print the random method
#     create a function with 2 args, calculates the percentage of 2 args
import sys
import math
import random


def percentage(num1, num2):
    return (num1 * 100) / num2


print(percentage(random.randint(1, 100), random.randint(1, 100)))

