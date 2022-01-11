# Defining a function

# def func_name(parameters):
#     func body ...

# Function calling

# func_name(arguments)

# Example 1 : Demonstration of Function Definition,
# Function body, function calling

# def func(x):
#     print("User has passed a parameter", x)
#
# func(10)


# ---------------------------Argument-----------------------

# Example 1: Passing Multiple Arguments(Addition Function)

# def addition(num1, num2):
#     add = num1 + num2
#     print("Addition of Two numbers is : ", add)
#
# addition(10, 20)

# Example 2: *args(arguments tuple)
# def addition(*nums):
#     add = 0
#     for i in nums:
#         add = add + i
#     print(add)
#
# addition(10, 20, 30, 40)

# ------------------ Keyword Arguments ----------------------

# Example 1: def greetings():
#
# def greetings(first_name, last_name):
#     print(f"Hello {first_name}, {last_name}, Good Evening!")
#
# greetings(first_name="Ashish", last_name="Lulla")


# Example 2 : **kwargs (def car_info(**info):)

# def car_info(**info):
#     print(info)
#     for i in info:
#         print(f"{i} = {info[i]} ")
#
# a = car_info(brand= "Tata",model= "Harrier",year= 2017, name = "Ashish")
# b = car_info(brand= "Hyundai",model= "Creta",year= 2018, name = "SOmesh")
# print(a)
# print(b)
# def car_info(**info):
#     for key in info:
#         print(f"{key} = {info[key]}")
#
# car_info(fname= "Ashish", lname ="lulla")

# -----------------------Default Arguments----------------------

# Example 1 : def country_name(name="India"):
# def country_name(name="India"):
#     print(name)
#
# country_name("America")

# Example 2: def area_circle():

# def area_circle(radius, pi=3.14):
#     print(pi*radius**2)
#
# area_circle(10)


# ----------------List as an Argument-----------------

# Example : def my_sum(lst):
# def my_sum(lst):
#     add = 0
#     for i in lst:
#         add = add + i
#     print(add)
#
# my_sum([1,2,3,4,5])

# ----------------Return Values---------------------
# Example 1:
# def country_name(name="India"):
#     return name
#
# print(country_name())


# Example 2:

# def country_name(name="India"):
#     print("line 1 executed")
#     print("line 2 executed")
#     print("Inside print statement: ", name)
#     return name
#
# print(f"Function returning a value : {country_name('Ammerica')}")



# ----------------Pass statement--------------------

# Example:
# def unknown():
#     pass
#
# unknown()

# ---------------------Lambda Function -------------
# Example 1:
#  syntax = lambda parameter(multiple) : expression(single)

# a = lambda x, y,z : x+y+z
# print(a(10,20,30))

# ------------------- Map Function -----------------

# Example 1: def sqaure()
# map(func, iterababe)   # iterables = list, set , dict, string, tuple

# def square(lst):
#     square_lst = []
#     for i in lst:
#         square_lst.append(i**2)
#     return square_lst
#
#
# print(square([1,2,3,4,5]))
#
# def square(x):
#     return x**2
#
# print(list(map(square, [1, 2, 3, 4, 5])))


# Example 2: def even()
# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
# print(list(map(even,[1,2,3,4,6,7,8])))


# -------------------- Filter Function---------------

# Example 1: def even , odd
# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
# def odd(x):
#     if x % 2 == 1:
#         return True
#     else:
#         return False
#
# even_lst = filter(even, [1,2,3,4,5,6])
# print(list(even_lst))
# odd_lst = filter(odd, [1,2,3,4,5,6,7])
# print(list(odd_lst))
# -------------------- Zip Function -----------------

# Example: fname, lname
# fname = ["Ashish", "Somesh"]
# lname = ["Lulla", "Patil"]
# age = [10,20]
# zip_variable = dict(zip(fname, lname))
# # print(zip_variable)
# # print(list(zip_variable))
#
# print(set(zip_variable))
# print(tuple(zip_variable))
