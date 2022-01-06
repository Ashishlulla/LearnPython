# Initializing a string
# a = "abcdef"
#
# # find length of String
# print(len(a))

# Concatenate two strings

# a = "abc"
# b = "def"
#
# print(a+""+b)


# Capitalize or title a string:
# i = "bhavesh lulla"
# print(i.title())

# Convert a string into a lower case:
# a = "Bhavesh"
# print(a.casefold())

# Count Number of time element occurs:
# a = "abbcccdddd"
# print(a.count("d"))

# print a string in a centre:
# print(a.center(100))

# Upper case and lower case

# print(a.upper())
# print(a.lower())

#  isalpha(), isnumeric(), isalnum(), isupper(), islower(),endswith(), startswith()

# a = "ashish123"
# print(a.endswith('3'))
# print(a.startswith("a"))
# print(a.isalnum())
# print(a.isnumeric())
# print(a.isalpha())
# print(a.isupper())
# print(a.islower())


# Replace function in string
# a = "abcdef"

# print(a.replace("def", "xyz"))

# Delete a element using replace function :
# print(a.replace("def", ""))

# --------------------- Format Specifier --------------------------------
#
# age = 20
#
# print("hello , My name is John and my age is ", age)
# #
# print(f"hello , My name {age} is John and my age is ")

# ------------------------ Escape Character -----------------------
# #
# print("Hello! this is abc,\t"
#       "I am a B-tech Student,\t"
#       "Studying in TY-IT.")

#  --------------------------Indexing-------------------------------:
#
# +ve   0 1 2 3 4 5
# a = " P Y T H O N "
# -ve  -6-5-4-3-2-1


# -------------------------------------Slicing in String--------------------------
# Syntax ->  str_name[ start_posn : end_posn : steps] or str_name[strt:end]


# a = "Python"
# Print thon
# print(a[2:])

# print thon with negative indexing
# print(a[-4:])

# Print reverse of string using string stepping
# print(a[::-1])

# print even  and odd from a string
# b = "1234567"
# print(b[::2])  # Output : Odd numbers (1,3,5,7)
# print(b[1::2])  # Output : Even numbers (2,4,6)

# -------------------------------- split() ------------------------------

# a = "We are a learning Python"
# print(a.split())
# ------------------------ Looping in string ----------------------------

# ---------------------------for loop to get value ----------------------

# a = "abcdef"
# for i in a:
#     print(i)

# ---------------------------for loop to get value through index ----------------------

# a = "abcdef"
# for i in range(len(i)):
#     print(a[i])

#  ------------------------------- if, in , is --------------------------------

# a = "abcdef"
# b = "defabc"

# ---------------- To check whether the two strings are equal -----------------

# if a is b:
#     print(True)
# else:
#     print(False)

# -----------------to check whether the value is present in list ----------------------

# if "c" in a:
#     print(True)
# else:
#     print(False)
