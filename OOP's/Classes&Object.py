# ----------------------- 1. How to Create a Class -------------------------

# class -> Keyword
# syntax -> class Class_name:
#               class_body.......


# ---------------------2.__init__ Method(Constructor) ------------------
# class Class_name:
#     def __init__(self):
#         pass

# # ---------------------3. Objects(Instance Variable) -------------------
# class Employee:
#     def __init__(self, id, fname, lname, salary,):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#
#
# e1 = Employee(1,"Ashish", "Lulla", 10000)
# e2 = Employee(2, "Bhavesh", "Lulla", 20000)
# e3 = Employee(3, "Somesh", "Patil", 30000)
# print(e1.fname)
# print(e2.fname)
# print(e3.fname)

# ---------------------------------- 4.Class Variable ----------------------------------
# class Employee:
#     company  = "xyz"
#     def __init__(self, id, fname, lname, salary,):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#
#
# e1 = Employee(1,"Ashish", "Lulla", 10000)
# e2 = Employee(2, "Bhavesh", "Lulla", 20000)
# e3 = Employee(3, "Somesh", "Patil", 30000)
# print(e1.company)
# print((e2.company))
# print(e3.company)

# ----------------------------- 5. Class Methods -------------------------------

# class Employee:
#     company = "xyz"
#
#     def __init__(self, id, fname, lname, salary, ):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#
#     def employee_info(self):
#         print(f"-----------Employee Information----------\n"
#               f"Company: {Employee.company}\n"
#               f"Id no: {self.id}\n"
#               f"Name : {self.fname} {self.lname}\n"
#               f"Salary :{self.salary}\n"
#               f"------------------------------------------")
#
#
# e1 = Employee(1, "Ashish", "Lulla", 10000)
# e2 = Employee(2, "Bhavesh", "Lulla", 20000)
# e3 = Employee(3, "Somesh", "Patil", 30000)
# e1.employee_info()
# e2.employee_info()
# e3.employee_info()



# --------------------Exercise on Class and Objects ---------------------

# 1. Create a Circle class and compute a area, circumference

# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def circumference(self):
#         return 2*self.radius*Circle.pi
#
#     def area(self):
#         return Circle.pi*self.radius**2
#
#
#
# c1 = Circle(5)
# print(c1.area())
# print(c1.circumference())

# 2. Create a Mobile Class

# class Mobile:
#     discount = 10
# 
#     def __init__(self, brand, model, name, price):
#         self.brand = brand
#         self.model = model
#         self.name = name
#         self.price = price
# 
#     def info(self):
#         return f"----------Mobile Information--------------" \
#                f"Brand: {self.brand} \n" \
#                f"Model: {self.model}\n" \
#                f"Name: {self.name}\n" \
#                f"Price: {self.price}"
# 
#     def apply_discount(self):
#         return f"Original Price: {self.price}\n" \
#                f"Discount : {Mobile.discount}% \n" \
#                f"Final Price: {self.price - (self.price * (Mobile.discount / 100))}"
# 
# 
# m1 = Mobile("Samsung", "A7-1234", "A7", 10000)
# print(m1.info())
# print(m1.apply_discount())
